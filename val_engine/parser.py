from datetime import datetime
import spacy
from dateutil import parser
import parsedatetime

# Load the English language model from spaCy
nlp = spacy.load("en_core_web_sm")


# Initialize parsedatetime.Calendar() instance
cal = parsedatetime.Calendar()

# Function to extract date, time, and day of the week from input string
def extract_date_time(input_string):
    # Process the input string using spaCy
    doc = nlp(input_string)

    # Initialize variables to store date, time, and day of the week
    extracted_date = None
    extracted_time = None
    extracted_day = None

    # Extract entities (including date, time, and day of the week) using spaCy's NER
    for ent in doc.ents:
        if ent.label_ == "DATE":
            # Parse the date using parsedatetime
            time_struct, parse_status = cal.parse(ent.text)
            # Convert time.struct_time to datetime object
            extracted_date = datetime(*time_struct[:6])
            # Extract the day of the week from the parsed date
            extracted_day = extracted_date.strftime("%A")
        elif ent.label_ == "TIME":
            # Parse the time using parsedatetime
            time_struct, parse_status = cal.parse(ent.text)
            # Convert time.struct_time to datetime object
            extracted_time = datetime(*time_struct[:6])
            # Format the time in 24-hour format
            extracted_time = extracted_time.strftime("%H:%M:%S")

    # Return the extracted date, time, and day of the week
    return extracted_date, extracted_time, extracted_day


# Example input string
input_str = "Hey, I have a meeting next friday at 10 am."

# Extract date, time, and day of the week from input string
ext_date, ext_time, ext_day = extract_date_time(input_str)

# Print the extracted date, time, and day of the week
print("Extracted date:", ext_date)
print("Extracted time:", ext_time)
print("Extracted day:", ext_day)
