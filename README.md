# Topological Methods in Machine Learning: A Tutorial for Practitioners

**Authors**: [Baris Coskunuzer](https://personal.utdallas.edu/~bxc190014/) (University of Texas at Dallas, USA) , [Cuneyt Gurcan Akcora](akcora.github.io) (University of Central Florida, USA)

This repository contains the code and resources for the tutorial ["Topological Methods in Machine Learning: A Tutorial for Practitioners"](https://github.com/cakcora/TopologyForML/blob/main/tutorial.pdf) This tutorial provides an introduction to topological data analysis (TDA) techniques, focusing on **Persistent Homology** and the **Mapper algorithm**, with practical applications in machine learning.

## Table of Contents

- [Persistent Homology](#persistent-homology)
- [Mapper Algorithm](#mapper-algorithm)
- [Applications](#applications)
- [References](#references)

## Introduction

As datasets become increasingly complex, traditional machine learning methods may not capture critical topological structures inherent in the data. Topological Machine Learning (TML) leverages concepts from **algebraic topology** to analyze complex data structures at multiple scales. 

In this tutorial, we cover two main tools of TML:
- **Persistent Homology**: This technique detects and quantifies clusters, loops, and voids across different scales of data.
- **Mapper Algorithm**: This algorithm constructs an interpretable graph to summarize high-dimensional data.

### Key Features
- A hands-on introduction to **Persistent Homology** and **Mapper**.
- Step-by-step examples for applying these techniques to real-world data.
- Practical implementations using Python libraries.

### Entry Points
If you do not have any experience with Python, first install an IDE such as [PyCharm](https://www.jetbrains.com/pycharm/download/). If you have a university email, you can download and use the professional version of PyCharm. Next, clone this GitHub repo using PyCharm.  Python is used within a project workspace (as was common in the CS in the old days) or in a notebook. We follow the notebook approach because it allows us to see the outputs quickly.

There are a few popular notebooks, such as Jupyter and Google Colab. PyCharm should ask to install the Jupyter notebook plugin within itself once the *.ipynb files are encountered. You can follow the on-screen tips from PyCharm to install the notebook. Once installed:
There are two main entry points in this repository:
- The **Persistent Homology** tutorial can be found in the notebook [`persistentHomology.ipynb`](https://github.com/cakcora/TopologyForML/blob/main/code/PersistentHomology.ipynb).

- The **Mapper Algorithm** tutorial can be found in the notebook [`mapper.ipynb`](https://github.com/cakcora/TopologyForML/blob/main/code/Mapper.ipynb).
 
## Setup

Whenever the code uses a Python library, we have provided the command to install the necessary libraries. For example, 

```bash
!pip install numpy matplotlib gudhi persim
```
will install all these libraries. If you know Python well, you can create virtual environments, but we assumed the worst case and used simple pip commands.


## Applications

We provide case studies from several domains that demonstrate how **Topological Data Analysis** techniques can be applied to practical problems, such as:

- **Shape Recognition**: Using **Persistent Homology** to detect shapes in point clouds.
- **Cancer Diagnosis**: Employing topological techniques to improve cancer diagnosis from histopathological images.
- **Drug Discovery**: Applying **Multiparameter Persistence** to drug discovery tasks.

## Slides
We do not yet have the slides for the tutorial, but we used this [slide deck](https://github.com/cakcora/TopologyForML/blob/main/AkcoraUnified.pptx) for a previous tutorial on Topology and Graphs.
## References

For further reading, please refer to:

```bibtex
@misc{coskunuzer2024tml,
  author = {Baris Coskunuzer and C{\"u}neyt G{\"u}rcan Ak{\c{c}}ora},
  title = {Topological Methods in Machine Learning: A Tutorial for Practitioners},
  year = {2024},
  eprint = {5833867},
  archivePrefix = {arXiv},
  primaryClass = {cs.LG},
  url = {https://github.com/cakcora/TopologyForML},
  comment = {54 pages, 35 figures},
  license = {http://creativecommons.org/licenses/by/4.0/}
}

