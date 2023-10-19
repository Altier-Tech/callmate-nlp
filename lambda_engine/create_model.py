import pickle
import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

# Load the English language model from spaCy
nlp = spacy.load("en_core_web_sm")

# Sample labeled dataset (sentence, action)
training_data = [
    ("Set a reminder for tomorrow at 10 AM", "set_reminder"),
    ("Send an email to John", "send_email"),
    ("I have a meeting tomorrow at 3 PM", "set_reminder"),
    ("I will not be able to answer calls from 2 PM today", "set_auto_answer"),
    ("i will be busy from 10 am to 2 pm today", )
    # TODO Add more labeled data as needed
]

# Extract features (POS tags) and labels from the training data
X_train = [" ".join([token.pos_ for token in nlp(sentence)]) for sentence, _ in training_data]
y_train = [action for _, action in training_data]

# Create a pipeline with CountVectorizer and RandomForestClassifier
pipeline = Pipeline([
    ("vectorizer", CountVectorizer()),
    ("classifier", RandomForestClassifier())
])

# Train the classifier
pipeline.fit(X_train, y_train)

# Save the model
with open("../bin/lambda_model.pkl", "wb") as f:
    pickle.dump(pipeline, f)
