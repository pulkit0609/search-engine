import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin, urlparse
from collections import Counter
import re
import nltk

nltk.download('stopwords')
stopwords = set(nltk.corpus.stopwords.words('english'))

BASE_URL = "https://www.skuad.io"
visited = set()
results = []

def get_path_from_url(url):
    path = urlparse(url).path.strip('/')
    parts = path.split('/')
    if not parts or parts == ['']:
        return ["Home"]
    return ["Home"] + [part.replace("-", " ").capitalize() for part in parts]

def extract_tags(text):
    words = re.findall(r'\b\w+\b', text.lower())
    filtered = [w for w in words if w not in stopwords and len(w) > 2]
    counts = Counter(filtered)
    all_keywords = [word for word, freq in counts.items()]
    return ",".join(all_keywords)

def scrape_page(url):
    if url in visited or not url.startswith(BASE_URL):
        return
    print(f"Scraping: {url}")
    visited.add(url)

    try:
        res = requests.get(url, timeout=10)
        if res.status_code != 200:
            return
        soup = BeautifulSoup(res.text, 'html.parser')

        title = soup.title.string.strip() if soup.title else ""

        meta_description = ""
        desc_tag = soup.find("meta", attrs={"name": "description"})
        if desc_tag and desc_tag.get("content"):
            meta_description = desc_tag["content"].strip()

        paragraphs = soup.find_all('p')
        raw_content = " ".join(p.get_text().strip() for p in paragraphs if p.get_text().strip())

        tags = extract_tags(raw_content)

        path = get_path_from_url(url)

        results.append({
            "title": title,
            "path": " > ".join(path),
            "url": url,
            "meta_description": meta_description,
            "tags": tags
        })

        links = soup.find_all('a')
        for link in links:
            href = link.get('href')
            if not href or href.startswith('#') or href.startswith('mailto:'):
                continue
            full_url = urljoin(BASE_URL, href)
            if BASE_URL in full_url:
                scrape_page(full_url)

    except Exception as e:
        print(f"Error scraping {url}: {e}")

scrape_page(BASE_URL)

with open('skuad_meta.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f"Scraped {len(results)} pages. Data saved to skuad_meta_tags.json.")
