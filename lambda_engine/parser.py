import pickle
import spacy

# Load the English language model from spaCy
nlp = spacy.load("en_core_web_sm")

# load model
with open("../bin/lambda_model.pkl", "rb") as f:
    pipeline = pickle.load(f)


async def


if __name__ == '__main__':
    while True:
        # Example input sentence to predict action
        input_sentence = input("Say (or q to exit): ")  # "Remind me to buy groceries tomorrow"

        if input_sentence == "q":
            exit()

        # Process the input sentence using spaCy and extract POS tags
        processed_sentence = " ".join([token.pos_ for token in nlp(input_sentence)])

        # Predict the action for the input sentence
        predicted_action = pipeline.predict([processed_sentence])

        print("Predicted Action:", predicted_action[0])
