# Introduction

We present the foundational concepts and implement deep learning models for recurrent (RNNs), Long short term memory (LSTMs) and convolutional neural networks (CNNs) with emphasis on deep learning oo. The main objective is to explore the basics of RNNs, LSTMs and CNN with examples and identify key applications where these architectures have been applied to solve problems. The examples presented in this repository are introductory given the fact that a vast literature exist on the theory and practical applications of RNNs, LSTMs and CNNs.

## Main Tech Stack

- Python and libraries (Numpy, Sklearn, Pandas etc)
- Tensorflow and Pytorch
- Opencv for computer vision examples
- Docker and kubernetes

### Util Tech
- Make file to manage and run docker and other commands
- Use bash script when necessary to manipulate useful assignments

### Main Notes

We revisit classical neural networks (NNs) and implement classification examples in python and tensorflow. The goal is to implement neural networks in text mining, machine translation, sequence-sequence language and similar examples. We discuss the  RNNs, LSTMs and CNNs architectures which are most suitable to the aforementioned tasks. 
To this end, we transform and train examples of use cases where both RNNs and LSTMs are most applicable via supervised learning.

The training data used is downloaded from different data sources (publicly available data sets). We begin with training data which are available in the ``` sklearn (scikit-learn) ``` and nltk packages.

## Contents

The repository consists of the following structure

```- misc_files:```  contains examples of text classification models implemented in Python and other ML frameworks.

``` - lstm_cnn_trainer ``` contains an example of using Long Short Term Memory (LSTM) deep learning architectures.

This folder contains LSTM and CNN examples implemented using Tensorflow, python, scikit-learn, text classification examples

To run, clone the repository using  `git clone <repo-name>` and supply the data assuming the environment has been properly configured.
You will create two separate DB Session objects and use them knowingly in the code - whether same name or not, you will adapt the ```.env``` and the code accordingly
you can even plug the same cli on multiple Astra organization
try astra config list
changing the code and providing different settings you can (you can create DB-specific and DB-generic tokens also).

## Useful Resources
Recent advancements in Machine Learning and their applications to various NLP tasks have been characterized by a large ecosystem of tools and frameworks. We identify some of the most popular ones and also admit that it is nearly impossible to list them in their entirety. My personal preference are as follows

### Local and Remote Development
- For IDEs, I will use Pycharm, VSCodium, Sublime Text, VSCode (If you cannot do without it), Vim (Yes on purpose) and more.
- Use of Gitpod, Space from Intellij, this Github etc
- Tensorflow and its corresponding tools and frameworks
- Pytorch and its corresponding tools and frameworks
- JAX and tools
- Mention (SKLearn, Pandas, Numpy etc)

### Implementation of airflow-mlflow-kafka example

- See the [example](https://github.com/MBKraus/incremental_training/blob/master/data/stream_sample.p)




