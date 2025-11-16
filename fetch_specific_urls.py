#!/usr/bin/env python3
"""
Fetch specific URLs and add them to scraped data
"""
import requests
from bs4 import BeautifulSoup
import json
import os
import time
import re

def clean_text(text):
    """Clean and normalize text"""
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def detect_language(code_text, class_attr=""):
    """Detect programming language from code block"""
    if class_attr:
        if 'java' in class_attr.lower():
            return 'java'
        if 'python' in class_attr.lower():
            return 'python'
        if 'javascript' in class_attr.lower() or 'js' in class_attr.lower():
            return 'javascript'

    # Simple heuristics
    if 'def ' in code_text or 'import ' in code_text:
        return 'python'
    if 'function' in code_text or 'const ' in code_text:
        return 'javascript'
    if 'public class' in code_text or 'import java' in code_text:
        return 'java'

    return ''

def fetch_url(url):
    """Fetch and extract content from a URL"""
    print(f"  Fetching: {url}")

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Try different content selectors
        content = None
        for selector in ['article', 'main', 'div[role="main"]', 'div.content', 'div.entry-content', 'div.post-content']:
            content = soup.select_one(selector)
            if content:
                break

        if not content:
            content = soup.body

        # Extract title
        title_elem = soup.find('h1') or soup.find('title')
        title = title_elem.get_text() if title_elem else url.split('/')[-1]
        title = clean_text(title)

        # Extract text content
        text_content = clean_text(content.get_text())

        # Extract code blocks
        code_blocks = []
        for pre in content.select('pre'):
            code_elem = pre.find('code') or pre
            code_text = code_elem.get_text()
            class_attr = code_elem.get('class', [''])[0] if code_elem.get('class') else ''
            language = detect_language(code_text, class_attr)

            code_blocks.append({
                'language': language,
                'code': code_text.strip()
            })

        return {
            'title': title,
            'url': url,
            'content': text_content[:5000],  # Limit content length
            'code_blocks': code_blocks[:10],  # Limit code blocks
            'patterns': []
        }

    except Exception as e:
        print(f"    [ERROR] Error fetching {url}: {e}")
        return None

def main():
    urls = [
        "https://www.w3.org/WAI/standards-guidelines/wcag/",
        "https://www.w3.org/WAI/ARIA/apg/",
        "https://web.dev/learn/accessibility",
        "https://github.com/dequelabs/axe-core",
        "https://www.a11yproject.com/checklist/"
    ]

    output_dir = "output/accessibility-testing_data"
    pages_dir = os.path.join(output_dir, "pages")

    # Create directories
    os.makedirs(pages_dir, exist_ok=True)

    print("\n============================================================")
    print("FETCHING SPECIFIC URLs")
    print("============================================================\n")

    pages_data = []

    for i, url in enumerate(urls):
        data = fetch_url(url)
        if data:
            # Save individual page
            page_file = os.path.join(pages_dir, f"page_{i:04d}.json")
            with open(page_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            pages_data.append({
                'title': data['title'],
                'url': data['url']
            })

            print(f"    [OK] Saved to {page_file}")

        time.sleep(1)  # Rate limiting

    # Update summary
    summary = {
        'name': 'accessibility-testing',
        'total_pages': len(pages_data),
        'base_url': urls[0],
        'pages': pages_data
    }

    summary_file = os.path.join(output_dir, 'summary.json')
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    print(f"\n[SUCCESS] Fetched {len(pages_data)} pages")
    print(f"[SUCCESS] Updated {summary_file}")
    print(f"\nNext step: python cli/doc_scraper.py --config configs/accessibility-testing.json --skip-scrape\n")

if __name__ == '__main__':
    main()
