# chunkerlib

Python library to chunk records of variable size

The following limits exist for the library
suitably sized for delivery to a system which has following limits:

 

* maximum size of output record is 1 MB, larger records are discarded

* maximum size of output batch is 5 MB

* maximum number of records in an output batch is 500

## Usage

```python
>>> from chunkerlib import chunker
>>> listing = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> items = chunker.Chunker(listing, max_batch_size=2)
>>> items.chunk()
[['a', 'b'], ['c', 'd'], ['e', 'f'], ['g']]
```