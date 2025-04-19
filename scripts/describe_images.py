#!/usr/bin/env python3

import argparse
import base64
import glob
import os
import re
from pathlib import Path
from urllib.parse import urljoin, urlparse
from urllib.request import urlopen

from openai import OpenAI

# Initialize OpenAI client
client = OpenAI()

# Encode an image to base64 from a URL using urllib
def encode_image_from_url(image_url):
    with urlopen(image_url) as response:
        return base64.b64encode(response.read()).decode("utf-8")

# Call GPT-4.1 Vision to describe the image
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

# Process a single markdown file
def process_markdown_file(input_path, output_path, base_url):
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to match markdown images: ![alt](url)
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

    new_content = image_pattern.sub(replace_image, content)

    output_file = Path(output_path) / Path(input_path).name
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Saved processed file to: {output_file}")

# Main function
def main():
    parser = argparse.ArgumentParser(description="Replace markdown images with GPT-4.1 Vision descriptions.")
    parser.add_argument("markdown_glob", help="Glob path for markdown files to process")
    parser.add_argument("output_dir", help="Path to output processed markdown files")
    parser.add_argument("base_url", help="Base URL to prefix to relative image URLs")

    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    files = glob.glob(args.markdown_glob, recursive=True)

    for file_path in files:
        process_markdown_file(file_path, args.output_dir, args.base_url)

if __name__ == "__main__":
    main()
