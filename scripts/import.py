#!/usr/bin/env python3

import os
import re
import glob
import argparse
import json
import yaml



def import_post(filepath, dest_dir_path, cfg):
    with open(filepath, 'r') as fin:
        txt = fin.read()
        body, meta = parse_markdown_with_metadata(txt)

        if 'skip-drafting-strategy' in meta and meta['skip-drafting-strategy']:
            print(f"skipping {filepath}")
            return

        url = meta['url']
        meta['old_draft'] = meta['draft']
        meta['draft'] = False
        meta['leth_url'] = url

        # build translation map of URLs
        path_map = build_url_map(cfg)
        LETH_BASE = 'https://lethain.com'

        posts_cfg = cfg['posts']
        section = 'uncategorized'
        if url in posts_cfg:
            overrides = posts_cfg[url]

            if 'section' in overrides:
                section = overrides['section']
                del overrides['section']

            for key, value in overrides.items():
                meta[key] = value

        basename = os.path.basename(filepath)
        section_dir_path = os.path.join(os.path.expanduser(dest_dir_path), section)
        os.makedirs(section_dir_path, exist_ok=True)
        dest_path = os.path.join(section_dir_path, basename)

        with open(dest_path,'w') as fout:
            cleaned = add_image_descriptions(body)
            cleaned = remove_divs(cleaned)
            cleaned = update_urls(cleaned, LETH_BASE, path_map)
            updated_txt = generate_markdown_with_metadata(cleaned, meta)
            fout.write(updated_txt)


def add_image_descriptions(text: str) -> str:
    # Pattern to match Markdown image syntax: ![alt text](image_url)
    pattern = re.compile(r'!\[(.*?)\]\((.*?)\)')

    def replacer(match):
        alt_text = match.group(1)
        image_markdown = match.group(0)
        return f"{image_markdown}\n\n<p class=\"img-desc i tc f6\">{alt_text}</p>"

    # Replace each image with the image followed by its alt text in a <p> tag
    return pattern.sub(replacer, text)


def update_urls(body: str, base_url: str, path_map: dict[str, str]) -> str:
    def replace_link(match: re.Match) -> str:
        text, path = match.groups()
        if path in path_map:
            new_path = path_map[path]
        elif path.startswith('/static/'):
            new_path = path
        else:
            new_path = f"{base_url}/{path.lstrip('/')}"

        return f"[{text}]({new_path})"

    # Regex to match markdown links with paths like [text](/path/)
    pattern = re.compile(r'\[([^\]]+)\]\((/[^\)]+)\)')
    return pattern.sub(replace_link, body)


def build_url_map(cfg) -> dict[str, str]:
    posts_cfg = cfg['posts']
    url_map = {}
    for old_url in posts_cfg:
        meta = posts_cfg[old_url]
        new_url = meta.get('url', old_url)
        url_map[f'/{old_url}/'] = f'/{new_url}/'
        url_map[f'/{new_url}/'] = f'/{new_url}/'

    return url_map


def remove_divs(html_text):
    # Pattern to match div tags with any attributes and their content
    div_pattern = re.compile(r'<div.*?>.*?#eng-strategy-book.*?<\/div>', re.DOTALL)

    # Remove divs and their content
    cleaned_text = re.sub(div_pattern, '', html_text)
    return cleaned_text


def setup_sections(dest_dir_path, cfg):
    sections = cfg['sections']
    for section, meta in sections.items():
        section_dir = os.path.join(os.path.expanduser(dest_dir_path), section)
        os.makedirs(section_dir, exist_ok=True)
        section_path = os.path.join(section_dir, '_index.html')
        meta['slug'] = section
        txt = generate_markdown_with_metadata("", meta)
        with open(section_path, 'w') as fout:
            fout.write(txt)


def generate_markdown_with_metadata(body, metadata):
    header = yaml.safe_dump(metadata, sort_keys=False).strip()
    return f"---\n{header}\n---\n\n{body.strip()}"


def parse_markdown_with_metadata(markdown_text):
    # Check for metadata header
    if markdown_text.startswith('---'):
        # Split the header and body
        parts = markdown_text.split('---', 2)
        if len(parts) >= 3:
            _, header, body = parts
            metadata = yaml.safe_load(header.strip())
            return body.strip(), metadata

        # No metadata header found
        return markdown_text.strip(), {}


def get_files_by_extension(directory, extension):
    # Expand '~' to the full user directory path
    directory = os.path.expanduser(directory)

    # Create a search pattern
    search_pattern = os.path.join(directory, f'*.{extension.lstrip(".")}')

    # Use glob to find all matching files
    files = glob.glob(search_pattern)
    return files


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Import files from blog to book.")
    parser.add_argument("--src_path", help="Source path")
    parser.add_argument("--dest_path", help="Destination path")
    parser.add_argument('--config-file', help="Path to configuration file", default="book.yaml")
    return parser.parse_args()


def load_config(path):
    with open(path, 'r') as fin:
        return yaml.safe_load(fin)


def main():
    """Main function to run the program."""
    args = parse_arguments()
    src_path = args.src_path
    dest_path = args.dest_path

    cfg = load_config(args.config_file)
    if src_path is None:
        src_path = cfg['src_path']
    if dest_path is None:
        dest_path = cfg['dest_path']

    setup_sections(dest_path, cfg)

    src_files = get_files_by_extension(src_path, "md")
    for filepath in src_files:
        import_post(filepath, dest_path, cfg)





if __name__ == "__main__":
    main()
