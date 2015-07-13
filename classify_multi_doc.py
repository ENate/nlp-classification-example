import os, re
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.svm import SVC
from sklearn.svm.classes import LinearSVC
from nltk.corpus import reuters as rt0
from nltk.corpus import stopwords
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
from numpy import*
from pylab import*
stop = stopwords.words("english")

def obtain_topic_tags(test_docs):
    """
    Open the topic list file and import topic names
    taking care to strip the trailing "\n" from each word.
    """
    os.chdir( "/home/nath/reutersInfo/reuters" )
    cats_file = "cats.txt"
    topics = open(cats_file, 'r')
    lines = topics.readlines()
    topics.close()
    topics = [t.strip() for t in lines]
    split_topics =[topix1.split()[1:] for topix1  in topics]
    train_topics = split_topics[len(test_docs):]
    return topics,train_topics
#Normalized text and regex for non alphanumeric characters
def normalized_words(open_file):
    doc_text=[re.sub('[^A-Za-z0-9]+', '', item) for item in open_file]
    return doc_text
# Convert all text in each document to lower case
def func_lower(txt1):
    d_1=[item.lower() for item in txt1[0]]
    return d_1

def remove_slash(txt0):
    item0=[item_doc.replace('\n','') for item_doc in txt0[0]]
    return  item0

def list_doc_topics(doc_test_topics,doc_train_topics):
    """
    creates a list of two-tuples
    that contain a single feature entry and the body text. 
    """    
    ref_docs = []
    ref_docs_test=[]
    for d in doc_train_topics:
        t1=d.split()[1:]
        d0 = rt0.raw(d.split()[0])
        d0= d0.replace('\n','')
        for t in t1:
            d_tup = (t, d0)
            ref_docs.append(d_tup)
            
    for d in doc_test_topics:
        t2=d.split()[1:]
        d00 = rt0.raw(d.split()[0])
        d00= d00.replace('\n','')
        for t in t2:
            d_tup = (t, d00)
            ref_docs_test.append(d_tup)
    return ref_docs,ref_docs_test

def vectorise_training_test_data(docs,docs_test):
    """
    Creates a document corpus list (by stripping out the
    class labels), then applies the TF-IDF transform to this
    list. 

    class label vector (y) and the corpus token/feature matrix (X) are returned.
    """
    # Create the training data class labels for test and training set
    y = [d[0] for d in docs]
    y1 = [d01[0] for d01 in docs_test]
    # Create the document corpus list for test and training sets
    corpus = [d[1] for d in docs]
    corpus_test = [d1[1] for d1 in docs_test]
    
    # Create the TF-IDF vectoriser and transform the corpus
    vectorizer = TfidfVectorizer(min_df=1)
    X1 = vectorizer.fit_transform(corpus)
    XtestVal = vectorizer.transform(corpus_test)
    #XtestVal = mlb().fit_transform(corpus_test)
    return X1, y,XtestVal,y1

def train_data_SVC(X, y):
    """
    Create and train the Support Vector Machine.
    """
    classif = OneVsRestClassifier(LinearSVC())
    classif.fit(X,y)
    return classif


if __name__ == "__main__":
    # Create the list of Reuters data separate the test and training data
    docs=[]
    train_docs = list(filter(lambda doc: doc.startswith("train"),rt0.fileids()));
    test_docs = list(filter(lambda doc: doc.startswith("test"),rt0.fileids()));
    topics,train_topics = obtain_topic_tags(test_docs)
    doc_train_topics=topics[len(test_docs):]
    doc_test_topics = topics[0:len(test_docs)]
    #documents_train = [(func_lower(d), c) for (d,c) in documents_train]
    #docs = [(remove_slash(item_doc),c) for (item_doc,c) in documents_train]
    #documents_train = [(normalized_words(d), c) for (d,c) in docs]
   
    # a list so that it can be printed out to the console
    # Obtain the topic tags and filter docs through it 
    
    ref_docs,ref_docs_test = list_doc_topics(doc_test_topics,doc_train_topics)
    
    # Vectorise and TF-IDF transform the corpus 
    #first for the training set and then for the test set
    X, y,XtestVal,y1 = vectorise_training_test_data(ref_docs,ref_docs_test)
   
    # Create the training-test split of the data
    X_train,X_test, y_train,ytest = train_test_split(X,y, test_size=0.2, random_state=42)

    # Create and train the Support Vector Machine
    classif = train_data_SVC(X_train,y_train)

    # Print the metrics for the test set
    pred1 = classif.predict(X_test)     # test set
    pred = classif.predict(XtestVal)    # validation set
    # Scores for test and validation sets
    print accuracy_score(y1, pred)
    print accuracy_score(ytest, pred1)
    print(classif.score(XtestVal,y1))
    # Print precision, f-measure and other useful metrics
    print(classification_report(y1, pred))
    #print the confusion matrix
    conf_arr = confusion_matrix(y1,pred)
    norm_conf = []
    for i in conf_arr:
        a = 0
        tmp_arr = []
        a = sum(i,0)
        for j in i:
                tmp_arr.append(float(j)/float(a))
        norm_conf.append(tmp_arr)
#Plot the confusion matrix to analyze categories
fig = plt.figure()
ax = fig.add_subplot(111)
res = ax.imshow(array(norm_conf), cmap=cm.jet, interpolation='nearest')    
for i, ij in enumerate(conf_arr):
    for j, cj in enumerate(ij):
        if cj>0:
            plt.text(j-.2, i+.2, cj, fontsize=14)
cb = fig.colorbar(res)
plt.show(cb)
print(conf_arr)