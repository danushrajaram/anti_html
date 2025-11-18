import sys
import requests
import re



def strip_html_tags(html):
    # Remove script and style blocks
    html = re.sub(r'<(script|style).*?>.*?(</\1>)', '', html, flags=re.DOTALL)
    # Replace ALL tags with ONE SPACE (THIS IS THE FIX)
    text = re.sub(r'<[^>]+>', ' ', html)
    # Collapse multiple spaces into one
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def main():
    if len(sys.argv) != 2:
        print("Usage: python -m anti_html <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()
        print(strip_html_tags(response.text))
    except Exception as e:
        print(f"Error: {e}")
