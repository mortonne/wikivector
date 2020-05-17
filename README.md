# wikivector
Tools for encoding Wikipedia articles as vectors.

## Installation

Get a clone of the repository, then run:

```bash
python setup.py install
```

## Exporting Wikipedia text

First, run [WikiExtractor](https://github.com/attardi/wikiextractor)
on a Wikipedia dump. This will generate a directory with many 
subdirectories and text files within each subdirectory. Next, build 
a header file with a list of all articles in the extracted text data:

```bash
wiki_header wiki_dir header_file
```

where `wiki_dir` is the path to the output from `WikiExtractor`. 
The `header_file` will be a CSV file with the title of each article
and the file in which it can be found.

To extract specific articles, write a CSV file with two columns: "item"
and "title". The "title" for each item must exactly match an article
title in the Wikipedia dump. To extract the text for each item:

```bash
export_articles header_file map_file output_dir
```

where `map_file` is the CSV file with your items, and `output_dir` is
where you want to save text files with each item's article.
