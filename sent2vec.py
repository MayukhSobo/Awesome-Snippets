from gensim.models import KeyedVectors
from sklearn.feature_extraction import stop_words
import numpy as np

def sent2vec(sentence, model, method='tfidf', **kwargs):
    """
    Generic function to convert a sentence to a vector using
    avg or TFIDF vecorization
    """
    
    ##### It is recommended to pass seperate stopwords #####
    stopwords = kwargs.get('stopwords')
    if stopwords is None:
        from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
        stopwords = ENGLISH_STOP_WORDS
    
    ##### It is recommended to pass seperate tokenizers #####
    tokenizer = kwargs.get('tokenizer')
    if tokenizer is None:
        from nltk.tokenize import RegexpTokenizer
        tokenizer = RegexpTokenizer(r'\w+')

    words = tokenizer.tokenize(sentence) # Tokenize the words
    words = {each for each in words if each not in stopwords} # Remove all the stopwords
    
    V = []
    
    for word in words: # Process over all the words in the sentence
        if model.__contains__(word):
            V.append(model[word])
    V = np.array(V)
    
    # If no words were present in the model
    # or blank sentence was passed, return a
    # word vector with all 0's
    if V.shape[0] == 0:
        # If model returns word2vec of different size
        # Default value is taken 300
        custom_shape = kwargs.get('shape', 300)
        return np.zeros(custom_shape)
    
    # If there is atleast one word in the sentence that
    # was vectoried properly
    
    if method.lower() == 'avg':
        V = V.sum(axis=0)
        return V / np.sqrt((V ** 2).sum())
    
    elif method.lower() == 'tfidf':
        tfidf_model = kwargs.get('tfidf_model') # Load the tfidf model
        if tfidf_model: # If model loaded sucessfully
            tfidf_vec = tfidf_model.transform([sentence]) # get TFIDF for the sentence
            indx = tfidf_model.vocabulary_.get(word, -1)
            tfidfs = []
            for word in words:
                if model.__contains__(word):
                    if indx != -1:
                        tfidfs.append(tfidf_vec[0, indx])
                    else:
                        tfidfs.append(0.0)
            tfidfs = np.array(tfidfs)
            denominator = tfidfs.sum()
            if denominator == 0.0: # No word is representred in tfidf and w2v both
                # Better than skipping that sentence
                denominator = tfidf_model.idf_.min() * 0.01
            numerator = V * tfidfs.reshape(V.shape[0], 1)
            numerator = numerator.sum(axis=0)
            return numerator / denominator
        else:
            raise ValueError('No tfidf model is present')

if __name__ == '__main__':
    text = 'Hello, how are you today?'
    model = KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary=True)
    vec = sent2vec(text, model, method='avg', 
             stopwords=stop_words.ENGLISH_STOP_WORDS)
    print(vec.shape)
    print(vec)