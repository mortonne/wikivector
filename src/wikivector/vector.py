"""Convert Wikipedia text to vector embeddings."""

import os
import numpy as np
import h5py


def read_text(items, text_dir):
    """Read text for a set of items."""
    text = []
    for item in items:
        wiki_file = os.path.join(text_dir, item + '.txt')
        if not os.path.exists(wiki_file):
            raise IOError(f'No text found for {item}.')

        with open(wiki_file, 'r') as f:
            item_text = f.read()
        text.append(item_text)
    return text


def embed_items_use(items, text_dir, model='normal'):
    """Calculate item embeddings based on Universal Sentence Encoder."""
    import tensorflow_hub as hub
    text = read_text(items, text_dir)
    if model == 'normal':
        hub_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
    elif model == 'large':
        hub_url = "https://tfhub.dev/google/universal-sentence-encoder-large/5"
    else:
        raise ValueError(f'Unknown model: {model}')
    embed = hub.load(hub_url)
    vectors = embed(text)
    return vectors


def save_vectors(vectors, items, h5_file):
    """Save vectors in an hdf5 file."""
    with h5py.File(h5_file, 'w') as f:
        # items
        dt = h5py.special_dtype(vlen=str)
        items = np.asarray(items)
        dset = f.create_dataset('items', items.shape, dtype=dt)
        for i, item in enumerate(items):
            dset[i] = item

        # vectors
        f.create_dataset('vectors', data=vectors)


def load_vectors(h5_file):
    """Load vectors from an hdf5 file."""
    with h5py.File(h5_file, 'r') as f:
        items = [item for item in f['items'].asstr()]
        vectors = f['vectors'][()]
    return vectors, items
