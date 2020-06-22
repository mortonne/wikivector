# wikivector
Tools for encoding Wikipedia articles as vectors.

## Installation

To get the latest stable version:

```bash
pip install wikivector
```

To get the development version:

```bash
pip install git+git://github.com/mortonne/wikivector
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

## Universal Sentence Encoder

Once articles have been exported, you can calculate a vector embedding
for each item using the Universal Sentence Encoder.

```bash
embed_articles map_file text_dir h5_file
```

This reads a map file specifying an item pool (only the "item" field is 
used) and outputs vectors in an hdf5 file. To read the vectors, in 
Python:

```python
from wikivector import vector
vectors, items = vector.load_vectors(h5_file)
```
