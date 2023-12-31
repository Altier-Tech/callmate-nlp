import pickle
import spacy

# Load the English language model from spaCy
nlp = spacy.load("en_core_web_sm")

# load model
with open("../bin/lambda_model.pkl", "rb") as f:
    pipeline = pickle.load(f)


def parse_action(text: str):
    processed_sentence = " ".join([token.pos_ for token in nlp(text)])

    predicted_action = pipeline.predict([processed_sentence])

    return predicted_action[0]


if __name__ == '__main__':
    while True:
        # Example input sentence to predict action
        input_sentence = input("Say (or q to exit): ")  # "Remind me to buy groceries tomorrow"

        if input_sentence == "q":
            exit()

        print("Predicted Action:", parse_action(input_sentence))
