#!/usr/bin/env python3

import os
import yaml
import re

def load_book_metadata(book_yaml_path):
    print(f"Loading book metadata from: {book_yaml_path}")
    with open(book_yaml_path, 'r') as f:
        data = yaml.safe_load(f)
        print(f"Loaded chapters: {len(data.get('chapters', []))}")
        return data

def find_blog_posts(content_dir):
    print(f"Scanning blog posts in: {content_dir}")
    blog_posts = []
    for root, _, files in os.walk(content_dir):
        for file in files:
            if file.endswith('.md'):
                full_path = os.path.join(root, file)
                blog_posts.append(full_path)
                print(f"Found blog post: {full_path}")
    print(f"Total blog posts found: {len(blog_posts)}")
    return blog_posts

def extract_url_from_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    match = re.search(r'^url:\s*(.+)', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return None

def build_url_to_path_map(blog_posts):
    url_to_path = {}
    for path in blog_posts:
        url = extract_url_from_file(path)
        if url:
            url_to_path[url] = path
            print(f"Mapped URL '{url}' to file '{path}'")
        else:
            print(f"WARNING: No URL found in '{path}'")
    return url_to_path

def enrich_blog_post(path, weight, section_title):
    print(f"Enriching file: {path} with weight={weight}, section={section_title}")
    with open(path, 'r') as f:
        lines = f.readlines()

    start, end = None, None
    for i, line in enumerate(lines):
        if line.strip() == '---':
            if start is None:
                start = i
            elif end is None:
                end = i
                break

    if start is not None and end is not None and end > start:
        front_matter = yaml.safe_load(''.join(lines[start+1:end]))
        front_matter['weight'] = weight
        front_matter['book_section'] = section_title

        new_front_matter = yaml.dump(front_matter, sort_keys=False)
        new_lines = lines[:start+1] + [new_front_matter] + lines[end:]
        with open(path, 'w') as f:
            f.writelines(new_lines)
        print(f"✅ Updated front matter in: {path}")
    else:
        print(f"❌ Could not find valid YAML front matter in: {path}")

def enrich_content_with_metadata(book_yaml_path, content_dir):
    metadata = load_book_metadata(book_yaml_path)
    blog_posts = find_blog_posts(content_dir)
    url_to_full_path = build_url_to_path_map(blog_posts)

    url_to_path = {}
    for url, path in url_to_full_path.items():
        url = url.strip('"')
        slug = url.split('/')[-1]
        url_to_path[slug] = path

    print(url_to_path)

    counter = 0
    for chapter in metadata['chapters']:
        section_title = chapter['title']
        for section in chapter['sections']:
            slug = section['slug']
            path = url_to_path.get(slug)
            if path:
                enrich_blog_post(path, counter * 1000, section_title)
                counter += 1
            else:
                print(f"⚠️  No file found for slug '{slug}'")

if __name__ == "__main__":
    enrich_content_with_metadata('book.yaml', 'content')
