import spacy
from dateutil.relativedelta import relativedelta
from datetime import datetime
from dateutil import parser

# Load the English language model from spaCy
nlp = spacy.load("en_core_web_sm")


# Function to extract date and time from input string
def extract_date_time(input_string):
    # Process the input string using spaCy
    doc = nlp(input_string)

    # Get the current date and time
    current_datetime = datetime.now()

    # Initialize variables to store date and time
    extracted_date = None
    extracted_time = None

    # Extract entities (including date and time) using spaCy's NER
    for ent in doc.ents:
        if ent.label_ == "DATE":
            # Parse the date using dateutil.parser
            extracted_date = parser.parse(ent.text).date()
        elif ent.label_ == "TIME":
            # Parse the time using dateutil.parser
            extracted_time = parser.parse(ent.text).time()
        elif ent.text.lower() == "tomorrow":
            # Calculate tomorrow's date based on the current date
            extracted_date = current_datetime.date() + relativedelta(days=+1)

    return extracted_date, extracted_time


# Example input string
input_str = "Hey, I have a meeting tomorrow at 10 am."

# Extract date and time from the input string
ext_date, ext_time = extract_date_time(input_str)

# Print the extracted date and time
print("Extracted Date:", ext_date)
print("Extracted Time:", ext_time)
