import spacy
from dateutil.relativedelta import relativedelta
from datetime import datetime
from dateutil import parser

# Load the English language model from spaCy
nlp = spacy.load("en_core_web_sm")


# Function to extract date, time, and day of the week from input string
def extract_date_time(input_string):
    # Process the input string using spaCy
    doc = nlp(input_string)

    # Get the current date and time
    current_datetime = datetime.now()

    # Initialize variables to store date, time, and day of the week
    extracted_date = None
    extracted_time = None
    extracted_day = None

    # Extract entities (including date, time, and day of the week) using spaCy's NER
    for ent in doc.ents:
        if ent.label_ == "DATE":
            # Parse the date using dateutil.parser
            extracted_date, tokens = parser.parse(ent.text, fuzzy_with_tokens=True)
            # Extract the day of the week from the parsed date
            extracted_day = extracted_date.strftime("%A")
        elif ent.label_ == "TIME":
            # Parse the time using dateutil.parser
            extracted_time, tokens = parser.parse(ent.text, fuzzy_with_tokens=True)

    # Return the extracted date, time, and day of the week
    return extracted_date, extracted_time, extracted_day


# Example input string
input_str = "Hey, I have a meeting this thursday at 10 am."

# Extract date, time, and day of the week from input string
ext_date, ext_time, ext_day = extract_date_time(input_str)

# Print the extracted date, time, and day of the week
print("Extracted date:", ext_date)
print("Extracted time:", ext_time)
print("Extracted day:", ext_day)
