#!/usr/bin/env python3
"""
Merge multiple context pack builder documentation sources into a unified skill
"""

import json
import os
import shutil
from pathlib import Path

def merge_context_pack_data():
    """Merge data from multiple context pack builder documentation sources"""

    sources = [
        "microsoft-semantic-kernel",
        "aws-agent-orchestration",
        "ibm-context-window",
        "agenta-context-management",
        "azure-api-design"
    ]

    unified_name = "bmad-orch-context-pack-builder"
    output_data_dir = f"output/{unified_name}_data"
    output_skill_dir = f"output/{unified_name}"

    # Create output directories
    os.makedirs(output_data_dir, exist_ok=True)
    os.makedirs(output_skill_dir, exist_ok=True)

    # Merge all scraped pages
    all_pages = []
    unified_summary = {
        "name": unified_name,
        "description": "Context pack builder and agent orchestration with optimization techniques for LLM context management",
        "sources": [],
        "total_pages": 0,
        "categories": {}
    }

    for source in sources:
        source_data_dir = f"output/{source}_data"
        summary_file = os.path.join(source_data_dir, "summary.json")

        if os.path.exists(summary_file):
            with open(summary_file, 'r', encoding='utf-8') as f:
                summary = json.load(f)

            unified_summary["sources"].append({
                "name": source,
                "description": summary.get("description", ""),
                "pages": summary.get("total_pages", 0),
                "base_url": summary.get("base_url", "")
            })

            # Copy all page files
            pages_dir = os.path.join(source_data_dir, "pages")
            if os.path.exists(pages_dir):
                for page_file in os.listdir(pages_dir):
                    if page_file.endswith('.json'):
                        # Read and modify the page file to include source info
                        page_path = os.path.join(pages_dir, page_file)
                        with open(page_path, 'r', encoding='utf-8') as f:
                            page_data = json.load(f)

                        # Add source information
                        page_data['source'] = source

                        # Save to unified directory
                        unified_page_file = f"{source}_{page_file}"
                        unified_page_path = os.path.join(output_data_dir, "pages", unified_page_file)
                        os.makedirs(os.path.dirname(unified_page_path), exist_ok=True)

                        with open(unified_page_path, 'w', encoding='utf-8') as f:
                            json.dump(page_data, f, indent=2, ensure_ascii=False)

                        all_pages.append(page_data)

    unified_summary["total_pages"] = len(all_pages)

    # Save unified summary
    with open(os.path.join(output_data_dir, "summary.json"), 'w', encoding='utf-8') as f:
        json.dump(unified_summary, f, indent=2, ensure_ascii=False)

    print(f"Merged {len(all_pages)} pages from {len(sources)} sources")
    print(f"Data saved to: {output_data_dir}")

    return output_data_dir, output_skill_dir

if __name__ == "__main__":
    merge_context_pack_data()