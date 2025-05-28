# 🔍 Website Improvement Search Engine (Intern Project at Payoneer)

A custom-built search engine that scrapes, cleans, and indexes content from [skuad.io](https://www.skuad.io) to help analyze and improve website discoverability, metadata structure, and keyword tagging. Designed to support SEO teams and developers with actionable insights on page structure and keyword noise.

---

## 🚀 Features

- ✅ **Web Scraping**: Extracts metadata, URLs, and structured HTML content from 1650+ web pages
- 🧠 **NLP Tag Extraction**: Uses NLTK to extract, clean, and de-duplicate keyword tags
- ❌ **Noise Reduction**: Filters out boilerplate footer/header content and high-frequency junk terms
- 📦 **Elasticsearch Indexing**: Stores processed metadata for lightning-fast queries
- 📊 **Visualization**: Kibana dashboards to show keyword frequency and tag quality across pages

---

## 🛠 Tech Stack

- **Language**: Python
- **Libraries**: BeautifulSoup, NLTK, Regex, Requests, JSON
- **Search Engine**: Elasticsearch
- **Visualization**: Kibana
- **Bonus Tools**: Counter, re, custom stopword lists

---

## 📁 Core Scripts

| Script             | Role                                                             |
|--------------------|------------------------------------------------------------------|
| `skuad_scraper.py` | Scrapes full site content, titles, descriptions, and paragraphs |
| `clean_skuad_data.py` | Removes boilerplate & overused tags to generate useful keyword lists |
| `index_skuad.py`   | Pushes structured JSON to Elasticsearch for search & analysis   |
| `app.py` *(optional)* | Flask API or UI endpoint for querying                          |

---

## 📊 Output

Each indexed document includes:
- `url` (page link)
- `title` (SEO title)
- `meta_description` (from HTML meta tag)
- `path` (navigation path from root)
- `tags` (NLP-cleaned keyword list for that page)

---

## 🔍 Use Cases

- 🔎 Evaluate how well different parts of a site are keyword-optimized
- ⚠️ Identify duplicate or low-value tags hurting SEO
- 📊 View tag spread across all pages to target content gaps

---

## 📈 Dataset Summary

- 1650+ pages analyzed
- 200+ high-frequency noisy tags removed
- Tag quality improved using layered NLP filtering

---

## 🧾 Author

**Pulkit Yagyasaini**  
[LinkedIn](https://www.linkedin.com/in/pulkit-yagyasaini-03509831b)  
GitHub: [pulkit0609](https://github.com/pulkit0609)

---

## ✅ Future Improvements

- [ ] Add fuzzy search interface via Flask or React
- [ ] Export report summaries (e.g., top 50 weak pages)
- [ ] Add tag classification using ML (semantic clusters)
