### TF-IDF(term frequency – inverse document frequency) - Tần số xuất hiện - Tần suất tài liệu nghịch đảo ### 

# Syntax: TF-IDF = Term Frequency (TF) * Inverse Document Frequency (IDF)

# TF(Tần số xuất hiện): là tỷ lệ giữa số lần từ xuất hiện trong một tài liệu so với tổng số từ trong tài liệu đó.
# TF(t, d) = (số lần từ t xuất hiện trong văn bản d) / (tổng số từ trong văn bản d)

# IDF(Tần suất tài liệu nghịch đảo): là những từ hiếm khi xuất hiện trong ngữ liệu có điểm IDF cao. Nó là nhật ký của tỷ lệ giữa số lượng tài liệu với số lượng tài liệu có chứa từ.
# IDF(t, D) = log_e( Tổng số văn bản trong tập mẫu D/ Số văn bản có chứa từ t )

# Sample TF-IDF

#Importing required module
import numpy as np
import nltk
nltk.download('punkt')

from nltk import word_tokenize
 
#Example text corpus for our tutorial
text = ['Topic sentences are similar to mini thesis statements.\
        Like a thesis statement, a topic sentence has a specific \
        main point. Whereas the thesis is the main point of the essay',\
        'the topic sentence is the main point of the paragraph.\
        Like the thesis statement, a topic sentence has a unifying function. \
        But a thesis statement or topic sentence alone doesn’t guarantee unity.', \
        'An essay is unified if all the paragraphs relate to the thesis,\
        whereas a paragraph is unified if all the sentences relate to the topic sentence.']
 
#Preprocessing the text data
sentences = []
word_set = []
 
for sent in text:
    x = [i.lower() for  i in word_tokenize(sent) if i.isalpha()]
    sentences.append(x)
    for word in x:
        if word not in word_set:
            word_set.append(word)
 
#Set of vocab 
word_set = set(word_set)
#Total documents in our corpus
total_documents = len(sentences)
 
#Creating an index for each word in our vocab.
index_dict = {} #Dictionary to store index for each word
i = 0
for word in word_set:
    index_dict[word] = i
    i += 1

#Create a count dictionary
 
def count_dict(sentences):
    word_count = {}
    for word in word_set:
        word_count[word] = 0
        for sent in sentences:
            if word in sent:
                word_count[word] += 1
    return word_count
 
word_count = count_dict(sentences)

#Term Frequency
def termfreq(document, word):
    N = len(document)
    occurance = len([token for token in document if token == word])
    return occurance/N

#Inverse Document Frequency
 
def inverse_doc_freq(word):
    try:
        word_occurance = word_count[word] + 1
    except:
        word_occurance = 1
    return np.log(total_documents/word_occurance)   

def tf_idf(sentence):
    tf_idf_vec = np.zeros((len(word_set),))
    for word in sentence:
        tf = termfreq(sentence,word)
        idf = inverse_doc_freq(word)
         
        value = tf*idf
        tf_idf_vec[index_dict[word]] = value 
    return tf_idf_vec
    
#TF-IDF Encoded text corpus
vectors = []
for sent in sentences:
    vec = tf_idf(sent)
    vectors.append(vec)
 
print(vectors[0])