# wikivector

[![PyPI version](https://badge.fury.io/py/wikivector.svg)](https://badge.fury.io/py/wikivector)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4453878.svg)](https://doi.org/10.5281/zenodo.4453878)

Tools for encoding Wikipedia articles as vectors.

The [wiki2USE method](https://doi.org/10.1523/JNEUROSCI.2034-19.2021), which is implemented in this project, makes it possible to quantify the conceptual similarity of any familiar stimuli (such as well-known people, places, or things) without having to collect massive datasets of similarity ratings from participants. 

Conceptual similarity estimates can then be used to inform psychology and cognitive neuroscience experiments by providing information about general prior knowledge that participants may have about stimuli before beginning an experiment. Snapshots of Wikipedia at different times can be used to reflect changing public knowledge.

<div align="center">
  <div style="max-width:500px; margin:0 20px;">
    <img src="https://github.com/mortonne/wikivector/blob/master/images/wikivector.png" alt="schematic showing how Wikipedia entries are used to estimate conceptual similarity of two famous people, Julia Roberts and Barack Obama" width="500px">
    <div style="text-align:left; padding:10px 0;">
    Schematic illustrating the wiki2USE method. First, each item of interest is matched to a corresponding Wikipedia article. Next, the text for each article is extracted and encoded using the universal sentence encoder to create a 512-dimensional vector that reflects the meaning of the information contained in the Wikipedia article. Finally, the vectors for different items are compared to estimate their conceptual similarity. Item similarity can be visualized using multidimensional scaling, which places items such that their relative distance reflects their relative dissimlarity. Model similarity correlates with human ratings of conceptual similarity.
    </div>
  </div>
</div>

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
wiki_header wiki_dir
```

where `wiki_dir` is the path to the output from `WikiExtractor`. 
This will create a CSV file called `header.csv` with the title of each 
article and the file in which it can be found.

To extract specific articles, write a CSV file with two columns: "item"
and "title". The "title" for each item must exactly match an article
title in the Wikipedia dump. We refer to this file as the `map_file`.

If you are working with an older Wikipedia dump, it can be difficult to 
find the correct titles for article pages, as page titles may have changed
between the archive and the current online version of Wikipedia. To help 
identify mismatches between the map file and the Wikipedia dump, you can 
run:

```bash
wiki_check_map header_file map_file
```

to display any items whose article is not found in the header file. You 
can then use the Bash utility `grep` to search the header file for correct 
titles for each missing item.

When your map file is ready, extract the text for each item:

```bash
export_articles header_file map_file output_dir
```

where `map_file` is the CSV file with your items, and `output_dir` is
where you want to save text files with each item's article. Check the
output carefully to ensure that you have the correct text for each item
and that XML tags have been stripped out.

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

## Citation

If you use wikivector, please cite the following paper:

Morton, NW*, Zippi, EL*, Noh, S, Preston, AR. 2021.
Semantic knowledge of famous people and places is represented in hippocampus and distinct cortical networks.
Journal of Neuroscience. 41(12) 2762-2779.
doi:[10.1523/JNEUROSCI.2034-19.2021](http:doi.org/10.1523/JNEUROSCI.2034-19.2021). *authors contributed equally
