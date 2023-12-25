## Introduction

We discuss recent advanceemnts in Natural Language Processing models using different supervised learning methods with emphasis on deep learning architectures. We begin with a brief review of the main components of Language modelling by introducing main terms and concepts, and discuss language modelling methods which existed before Bidirectional Encoder Representation Transformers (BERT). In the source folder of the repository, we include examples of models developed for basic text and document mining tasks. For instance, we train a Long Term Short Memory (LSTM) and Recurrent deep Neural Networks (RNNs). The goal is to gently introduce the rise of transformer models and their performance in language processing applications. To this end, we identify a few significant results which paved the way for BERT and mention fewer modifications which led to well known applications. Moreover, I also discuss model pre-training and fine-tuning which are vital in adaptive learning.

To reproduce the examples discussed in this repository, the following Tech stack are required:

#### Tech Stack
- Python 3.10.+ (Anaconda for env management, pip etc)
- Tensorflow
- Pytorch
- scikit-learn
- pandas
- matplotlib
- transformers
### Life before BERT
We explore the use of LSTMs and RNNs for natural language processing problems. 

### Life After BERT
Project Structure
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
