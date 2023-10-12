import pickle
import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

# Create a pipeline with CountVectorizer and RandomForestClassifier
pipeline = Pipeline([
    ("vectorizer", CountVectorizer()),
    ("classifier", RandomForestClassifier())
])


# load model
with open("model.pkl", "rb") as f:
    pipeline = pickle.load(f)

while True:
    # Example input sentence to predict action
    input_sentence = input("Say: ")  # "Remind me to buy groceries tomorrow"

    if input_sentence == "end":
        exit()

    # Process the input sentence using spaCy and extract POS tags
    processed_sentence = " ".join([token.pos_ for token in nlp(input_sentence)])

    # Predict the action for the input sentence
    predicted_action = pipeline.predict([processed_sentence])

    print("Predicted Action:", predicted_action[0])
