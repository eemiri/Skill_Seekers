#!/usr/bin/env python3
"""
Fetch additional URLs and add them to existing scraped data.
"""

import json
import os
import sys
import time
import requests
from bs4 import BeautifulSoup
from pathlib import Path

def extract_content(soup, selectors):
    """Extract content from page using CSS selectors."""
    # Try each selector until we find content
    main_selectors = selectors.get('main_content', 'article, main').split(', ')
    content_elem = None

    for selector in main_selectors:
        content_elem = soup.select_one(selector.strip())
        if content_elem:
            break

    if not content_elem:
        return None

    # Get title
    title_elem = soup.select_one(selectors.get('title', 'h1, title'))
    title = title_elem.get_text(strip=True) if title_elem else "Untitled"

    # Get text content
    text = content_elem.get_text(separator='\n', strip=True)

    # Get code blocks
    code_blocks = []
    code_selectors = selectors.get('code_blocks', 'pre, code').split(', ')
    for selector in code_selectors:
        for code_elem in content_elem.select(selector.strip()):
            code_text = code_elem.get_text(strip=True)
            if code_text and len(code_text) > 10:  # Skip tiny snippets
                code_blocks.append(code_text)

    return {
        'title': title,
        'text': text,
        'code_blocks': code_blocks
    }

def fetch_url(url, selectors, rate_limit=1.0):
    """Fetch and parse a URL."""
    print(f"  Fetching: {url}")

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        content = extract_content(soup, selectors)

        if content:
            print(f"    [OK] {content['title']}")
            time.sleep(rate_limit)
            return {
                'url': url,
                'title': content['title'],
                'content': content['text'],
                'code_blocks': content['code_blocks']
            }
        else:
            print(f"    [SKIP] No content extracted")
            return None

    except Exception as e:
        print(f"    [ERROR] {e}")
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python fetch_additional_urls.py <config_file>")
        sys.exit(1)

    config_file = sys.argv[1]

    # Load config
    with open(config_file, 'r') as f:
        config = json.load(f)

    name = config['name']
    additional_urls = config.get('additional_urls', [])
    selectors = config.get('selectors', {})
    rate_limit = config.get('rate_limit', 1.0)

    if not additional_urls:
        print("No additional_urls found in config")
        sys.exit(0)

    data_dir = Path(f"output/{name}_data")
    pages_dir = data_dir / "pages"
    summary_file = data_dir / "summary.json"

    # Create directories if needed
    pages_dir.mkdir(parents=True, exist_ok=True)

    # Load existing summary
    if summary_file.exists():
        with open(summary_file, 'r') as f:
            summary = json.load(f)
    else:
        summary = {
            'name': name,
            'total_pages': 0,
            'base_url': config['base_url'],
            'pages': []
        }

    print(f"\n{'='*60}")
    print(f"FETCHING ADDITIONAL URLs: {name}")
    print(f"{'='*60}")
    print(f"URLs to fetch: {len(additional_urls)}")
    print()

    # Fetch each URL
    new_pages = 0
    for url in additional_urls:
        page_data = fetch_url(url, selectors, rate_limit)

        if page_data:
            # Save page data
            page_num = summary['total_pages'] + new_pages
            page_file = pages_dir / f"page_{page_num:04d}.json"

            with open(page_file, 'w', encoding='utf-8') as f:
                json.dump(page_data, f, indent=2, ensure_ascii=False)

            # Add to summary
            summary['pages'].append({
                'title': page_data['title'],
                'url': page_data['url']
            })

            new_pages += 1

    # Update summary
    summary['total_pages'] += new_pages

    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    print()
    print(f"[SUCCESS] Added {new_pages} pages")
    print(f"Total pages: {summary['total_pages']}")
    print()
    print("Run the scraper with --skip-scrape to rebuild the skill:")
    print(f"  python cli/doc_scraper.py --config {config_file} --skip-scrape")

if __name__ == '__main__':
    main()
