# TSSAlgorithm

A Python implementation of the TSS algorithm proposed in the article "Discovering Small Target Sets in Social Networks: A Fast and Effective Algorithm" [[arXiv:1610.03721]]

## Technology
* [Python 2.7.x]
* [The Python interface of SNAP]: SNAP is a general purpose, high performance system for analysis and manipulation of large networks

## How it works
1. The "GraphChecking" folder contains a script that checks if a given dataset represent a direct or undirect graph. (Optional)
2. The "LoadCustomizeSave" folder contains a script that adds the threshold value on each node. It produces a ".graph" which is necessary for the TSS algorithm.
3. The "TSS" folder contains the TSS algorithm.

## Datasets
The "Datasets" folder contains some datasets that have been used to test the algorithm. 






[arXiv:1610.03721]: <https://arxiv.org/abs/1610.03721>
[The Python interface of SNAP]: <http://snap.stanford.edu/snappy/index.html>
[Python 2.7.x]: <https://www.python.org/about/>
