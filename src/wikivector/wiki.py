"""Access information from a Wikipedia dump."""

import os
import glob
import re
import pandas as pd
from selectolax.parser import HTMLParser


def file_titles(text_file):
    """Get all page titles in a text file."""
    pattern = re.compile('title="(.*)"')
    file_titles = []
    with open(text_file, 'r') as f:
        for line in f:
            if line.startswith('<doc'):
                m = re.search(pattern, line)
                file_titles.append(m.group(1))
    return file_titles


def dump_pages(dump_dir):
    """Get paths to all pages in a dump directory."""
    wiki_titles = []
    wiki_files = []
    sub_dir_match = glob.glob(os.path.join(dump_dir, '[A-Z]*'))
    for sub_dir in sorted(sub_dir_match):
        text_match = glob.glob(os.path.join(sub_dir, 'wiki_[0-9]*'))
        for text_file in sorted(text_match):
            all_titles = file_titles(text_file)
            for title in all_titles:
                wiki_titles.append(title)
                wiki_files.append(text_file)
    df = pd.DataFrame({'title': wiki_titles, 'file': wiki_files})
    return df


def article_file(header, title):
    """Find which file has text for an article."""
    row = header.query(f'title == "{title}"')
    if row.size == 0:
        raise RuntimeError(f'Article "{title}" not found.')
    return row['file'].iloc[0]


def article_text(text_file, title):
    """Extract article text from a text dump file."""
    with open(text_file, 'r') as f:
        full_text = f.read()
    tree = HTMLParser(full_text)
    articles = tree.css('doc')
    titles = [art.attributes['title'] for art in articles]
    if title not in titles:
        raise RuntimeError(f'Article "{title}" not found in file: {text_file}')
    raw = articles[titles.index(title)].text()
    article = raw.replace('\n', ' ').strip()
    return article
