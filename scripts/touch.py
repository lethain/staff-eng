#!/usr/bin/env python3

import glob
import os
import argparse
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the second occurrence of '---'
    split_parts = content.split('---')
    if len(split_parts) < 3:
        print(f"Skipping {filepath}: less than 2 '---' found")
        return

    # Rebuild up to second '---' unchanged
    pre_content = '---'.join(split_parts[:2]) + '---'
    post_content = '---'.join(split_parts[2:])

    # Normalize newlines only once
    if '\n\n\n' in post_content:
        post_content = post_content.replace('\n\n\n', '\n\n', 1)
    elif '\n\n' in post_content:
        post_content = post_content.replace('\n\n', '\n\n\n', 1)

    new_content = pre_content + post_content

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"Processed: {filepath}")

def main():
    parser = argparse.ArgumentParser(description='Normalize newlines in files after second "---".')
    parser.add_argument('pattern', type=str, help='Glob pattern for files (e.g., "./*.txt")')
    args = parser.parse_args()

    for filepath in glob.glob(args.pattern, recursive=True):
        process_file(filepath)

if __name__ == '__main__':
    main()
