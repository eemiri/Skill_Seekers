import os
import re
import requests
from bs4 import BeautifulSoup

targets = [
    ("developer-handoff", "adobe-xd-design-specs", "https://helpx.adobe.com/xd/help/publish-design-specs.html"),
    ("developer-handoff", "interaction-design-design-handoffs", "https://www.interaction-design.org/literature/topics/design-handoffs"),
    ("developer-handoff", "logrocket-design-specs", "https://blog.logrocket.com/ux-design/creating-design-specs-developer-handoff/"),
    ("developer-handoff", "uxpin-design-to-dev", "https://www.uxpin.com/studio/blog/10-ways-to-improve-design-to-development-handoff/"),
    ("design-ux-review", "eleken-design-qa", "https://www.eleken.co/blog-posts/design-qa-checklist-to-test-ui-and-prepare-for-design-handoff"),
    ("motion-design", "google-motion-meaningful", "https://design.google/library/making-motion-meaningful"),
    ("motion-design", "medium-easing-curves", "https://medium.com/@ryan_brownhill/crafting-easing-curves-for-user-interfaces-34f39e1b4a43"),
    ("motion-design", "easings-net", "https://easings.net/"),
    ("motion-design", "mdn-css-easing", "https://developer.mozilla.org/en-US/docs/Web/CSS/easing-function"),
    ("ab-testing", "cxl-ab-test-calculator", "https://cxl.com/ab-test-calculator/"),
    ("internationalization-localization", "w3c-bp-i18n-specdev", "https://w3c.github.io/bp-i18n-specdev/"),
    ("internationalization-localization", "centus-rtl-translation", "https://centus.com/blog/right-to-left-languages-translation"),
    ("internationalization-localization", "smartling-translate-rtl", "https://www.smartling.com/blog/translate-rtl-languages")
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0 Safari/537.36"
}

out_dir = os.path.join("tmp", "fetched")
os.makedirs(out_dir, exist_ok=True)

for skill, slug, url in targets:
    print(f"Fetching {url}")
    try:
        resp = requests.get(url, headers=headers, timeout=60)
        resp.raise_for_status()
    except Exception as e:
        print(f"  ERROR fetching {url}: {e}")
        continue

    soup = BeautifulSoup(resp.text, "html.parser")
    main = soup.select_one("article, main, div[role='main'], .content, .main-content, .article-content, .post-content, .page-content")
    if not main:
        main = soup.body
    text = main.get_text("\n") if main else soup.get_text("\n")
    text = re.sub(r"\n{2,}", "\n\n", text)
    text = re.sub(r"[\t\r]", " ", text)
    text = text.strip()
    if len(text) > 10000:
        text = text[:10000] + "\n\n[Content truncated]"
    filename = f"{skill}__{slug}.txt"
    with open(os.path.join(out_dir, filename), "w", encoding="utf-8") as f:
        f.write(f"URL: {url}\n\n")
        f.write(text)
    print(f"  Saved to {filename} ({len(text)} chars)")
