# import all necessary library

import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import pickle






#create the review model

class review_model():
    def __init__(self, model_file, vectorizer_file):
        with open('restaurant_review/model', 'rb') as model_file, open('restaurant_review/vectorizer', 'rb') as vectorizer_file:
            self.classifier = pickle.load(model_file)
            self.cv = pickle.load(vectorizer_file)
            self.data = None
            
    # Clean the data and create corpus   
    def clean_data(self, text_input):
        corpus = []
        review = re.sub('[^a-zA-Z]', ' ', text_input)
        review = review.lower()
        review = review.split()
        ps = PorterStemmer()
        all_stopwords = stopwords.words('english')
        all_stopwords.remove('not')
        review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
        review = ' '.join(review)
        corpus.append(review)
        vectorized_corpus = self.cv.transform(corpus).toarray()
        self.data = vectorized_corpus
            
    # Make predictions
    def predict(self): 
        if (self.data is not None): 
            pred = self.classifier.predict(self.data)[0]
            return pred
        
        

