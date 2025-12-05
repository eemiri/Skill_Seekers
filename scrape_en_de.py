#!/usr/bin/env python3
"""
Multi-URL scraper for EN-DE Best Practices
"""

import json
import os
import subprocess
import sys

def scrape_multiple_urls():
    """Scrape multiple URLs for EN-DE best practices"""

    urls = [
        "https://tcworld.info/e-magazine/technical-writing/guideline-for-technical-german-100/",
        "https://publications.europa.eu/code/en/en-000100.htm",
        "https://bdue.de/en/bdue",
        "https://ata-divisions.org/GLD/",
        "https://www.smartling.com/blog/what-is-dach-region",
        "https://www.internationalschooltutors.de/English/advice/language/differences/german2.html"
    ]

    skill_name = "en-de-best-practices"

    print(f"Creating {skill_name} skill from {len(urls)} sources...")
    print(f"Sources: {urls}")
    print()

    # Create individual configs for each URL
    for i, url in enumerate(urls):
        config_name = f"{skill_name}_{i}"
        config = {
            "name": config_name,
            "description": f"Part {i+1} of EN-DE translation best practices",
            "base_url": url,
            "selectors": {
                "main_content": "article, main, div[role='main'], .content, .post-content, .entry-content, .page-content, .site-content",
                "title": "h1, title",
                "code_blocks": "pre, code"
            },
            "url_patterns": {
                "include": [],
                "exclude": ["/search", "/tag/", "/category/", "/author/", "/feed/", "/comment", "/wp-admin/", "/wp-content/", "/wp-json/", ".pdf"]
            },
            "categories": {
                "translation_guidelines": ["guideline", "technical-german", "translation", "standards"],
                "technical_writing": ["technical-writing", "documentation", "style-guide"],
                "dach_region": ["dach", "austria", "switzerland", "germany", "localization"],
                "professional_standards": ["europa", "bdue", "ata", "standards", "certification"],
                "language_differences": ["differences", "comparison", "grammar", "vocabulary", "usage"]
            },
            "rate_limit": 1.0,
            "max_pages": 30,
            "timeout": 30
        }

        config_file = f"configs/{config_name}.json"
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)

        print(f"Created config: {config_file}")

        # Scrape this URL
        print(f"Scraping: {url}")
        try:
            result = subprocess.run([
                sys.executable, "cli/doc_scraper.py",
                "--config", config_file,
                "--enhance-local"
            ], capture_output=True, text=True, timeout=3600)

            if result.returncode == 0:
                print(f"  ✓ Success: {config_name}")
            else:
                print(f"  ✗ Error: {result.stderr}")
        except subprocess.TimeoutExpired:
            print(f"  ✗ Timeout after 1 hour")
        except Exception as e:
            print(f"  ✗ Exception: {e}")

    print(f"\nAll scraping completed!")
    print(f"Check the output/{config_name}_*/ directories for results.")

if __name__ == "__main__":
    scrape_multiple_urls()