# Data Structures and Algorithms

## Introduction

Practical data structures and algorithms, that are the core of computer science. If you’ve ever wanted to understand what computers can do, how they do it, and what they have difficulty doing, then you need a deep understanding of both.

## Prerequirements

knowledge of some programming language and some mathematics. Although the sample code is written in Python, you don’t need to know Python to follow what’s happening. Python is not hard to understand, if you’ve done some procedural and/or object-oriented programming. 

You’ll also need knowledge of how to find things on the Internet, download and install software, and run them on a computer. The instructions for downloading and running the visualization programs can be found in Appendix A of this book. The Internet has made it very easy to access a cornucopia of tools, including tools for learning programming and computer science. We expect readers to already know how to find useful resources and avoid sources that might provide malicious software.


## Data Structure Comparison

| Data Structure | Advantages | Disadvantages |
|----------------|-------------|---------------|
| Array | Simple. Fast insertion as long as index is known. Fast traversal. | Slow search, size must be known at beginning. Slow to grow. |
| Ordered array | Same as array but quicker search for items if looking by sort key. | Same as array. |
| Stack | Simple. Fast for last-in, first-out (LIFO) insertion and deletion. Fast traversal. | Slow search for items other than last-in, first-out. |
| Queue | Moderately complex. Fast for first-in, first-out (FIFO) insertion and deletion. Fast traversal. | Slow search for items other than first-in, first-out. |
| Linked List | Moderately complex. Fast insertion and deletion for a known position in list. Easy to grow and shrink. Fast traversal. | Slow search. |
| Binary tree | Moderately complex. Quick search, insertion, and deletion when tree is balanced. Easy to grow and shrink. Fast traversal. | Deletion algorithm is complex and balancing can be time-consuming. |
| Red-Black tree | Quick search, insertion, and deletion. Tree always balanced. Fast traversal. | Complex. |
| 2-3-4 tree | Quick search, insertion, and deletion. Tree always balanced. Similar trees are good for disk storage. Easy to grow and shrink. Fast traversal. | Complex. |
| Quadtree | Quick search, insertion, and deletion by 2-dimensional coordinates. Easy to grow and shrink. Fast traversal. | Complex. |
| Hash table | Fast search. Fast insertion and quick deletion in most cases. | Complex. Can take more space than other data structures. Traversal may be slightly slower than others. |
| Heap | Moderately complex. Quick insertion and deletion for items in sorted order. Fast traversal. | Slow search for items other than minimum or maximum. |
| Graph | Fast insertion and unordered traversal of nodes and edges. | Complex. Slow search (by label) and deletion. Traversal can be slow depending on path constraints. Can be slightly slower than other data structures. |

