#!/usr/bin/env python3

import os
import base64
import glob
import argparse
import json
import yaml
import re
from urllib.parse import urljoin, urlparse
from urllib.request import urlopen

from openai import OpenAI

client = OpenAI()

BASE_URL = 'https://draftingstrategy.com'

def llm_prep_post(filepath, dest_dir_path, cfg):
    with open(filepath, 'r') as fin:
        txt = fin.read()
        body, meta = parse_markdown_with_metadata(txt)
        body_filters = [remove_divs, remove_extra_whitespace, replace_relative_urls, describe_images]
        cleaned_body = body
        for body_filter in body_filters:
            cleaned_body = body_filter(cleaned_body)

        url = BASE_URL
        path = meta['url'].strip()
        if not path.startswith('/'):
            url += '/'
        url += path
        new_body = "# " + meta['title'] + '\nurl: ' + url + '\n\n' + cleaned_body

        basename = os.path.basename(filepath)
        filename = f"{meta['weight']:05}_{basename}"
        expanded_dest_dir_path = os.path.expanduser(dest_dir_path)
        dest_path = os.path.join(expanded_dest_dir_path, filename)

        os.makedirs(expanded_dest_dir_path, exist_ok=True)
        with open(dest_path,'w') as fout:
            fout.write(new_body)


def describe_images(text):
    base_url = BASE_URL
    image_pattern = re.compile(r'!\[.*?\]\((.*?)\)')

    def replace_image(match):
        image_url = match.group(1)
        if not urlparse(image_url).scheme:
            image_url = urljoin(base_url, image_url)
        try:
            print(f"Processing image: {image_url}")
            base64_img = encode_image_from_url(image_url)
            description = describe_image(base64_img)
            return f"**Image Description:** {description}"
        except Exception as e:
            print(f"Failed to process {image_url}: {e}")
            return f"*Failed to describe image at {image_url}*"

    new_text = image_pattern.sub(replace_image, text)
    return new_text
    

            
def remove_extra_whitespace(text):
    return re.sub(r'\n{2,}', '\n\n', text)


def replace_relative_urls(markdown_text):
    base_url = BASE_URL    

    # Regex explanation:
    # \[([^\]]+)\]         : Matches the markdown link text inside brackets
    # \(\s*(/[^)\s]*)\s*\): Matches a URL starting with / (allowing whitespace after '(' and before ')')
    pattern = re.compile(r'\[([^\]]+)\]\(\s*(/[^)\s]*)\s*\)')

    def replacer(match):
        text = match.group(1)
        url = match.group(2)
        return f"[{text}]({base_url}{url})"

    return pattern.sub(replacer, markdown_text)

            
def remove_divs(html_text):
    # Pattern to match div tags with any attributes and their content
    div_pattern = re.compile(r'<div.*?>.*?#eng-strategy-book.*?<\/div>', re.DOTALL)    

    # Remove divs and their content
    cleaned_text = re.sub(div_pattern, '', html_text)
    return cleaned_text

            
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


def encode_image_from_url(image_url):
    with urlopen(image_url) as response:
        return base64.b64encode(response.read()).decode("utf-8")


def describe_image(base64_image):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    { "type": "text", "text": "Describe this image in detail." },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    },
                ],
            }
        ],
        max_tokens=300,
    )
    return response.choices[0].message.content.strip()

    
def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Import files from repo to build LLM-optimized input.")
    parser.add_argument('--config-file', help="Path to configuration file", default="book.yaml")
    return parser.parse_args()


def load_config(path):
    with open(path, 'r') as fin:
        return yaml.safe_load(fin)



def main():
    """Main function to run the program."""
    args = parse_arguments()
    cfg = load_config(args.config_file)
    src_path = cfg['llm_src_path']
    dest_path = cfg['llm_dest_path']

            
    src_files = get_files_by_extension(src_path, "md")
    for filepath in src_files:
        llm_prep_post(filepath, dest_path, cfg)


if __name__ == "__main__":
    main()
    
