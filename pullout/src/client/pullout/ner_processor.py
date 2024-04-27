import re
import os

import spacy
# displacy for more visual display rather than just text
from spacy import displacy
# fastlang contains the language detector
import spacy_fastlang

from pullout import src_path
from pullout import DEBUG
from pprint import pprint

# Remove usesless warning from spacy_fastlang
# safe to do according to https://github.com/facebookresearch/fastText/issues/1056
import fasttext
fasttext.FastText.eprint = lambda x: None

lt_model = os.path.join(src_path, 'ner', 'lt_model')
en_model = os.path.join(src_path, 'ner', 'lt_model')

def get_entities(text_all) -> list:
    if not text_all or text_all == "":
        return None
    import time
    start = time.time()
    
    modified_text = format_phone_numbers(text_all)
    nlp = spacy.load(lt_model, disable=['tagger','parser', 'senter', 'lemmatizer'])
    doc = nlp(modified_text)

    result = {}
    for ent in doc.ents:
        text = ent.text
        if ent.label_ == "EMAIL" and not is_email_correct(text):
            continue
        elif ent.label_ == "TEL" and not is_telephone_correct(text):
            continue
        elif ent.label_ == "FAX" and not is_telephone_correct(text):
            continue
        elif ent.label_ == "URL" and not is_url_correct(text):
            continue
        elif ent.label_ == "FN" or ent.label_ == "ORG" or ent.label_ == "TITLE" or ent.label_ == "ROLE":
            text = text.title()

        result[ent.label_] = text

    end = time.time()
    if DEBUG:
        print("NER took: ", end - start, "seconds\n")
        print("----------[OCR] scanned text with formatted phones----------")
        print(modified_text)
        print("----------[NER] found entities------------------------------")
        pprint(result)
        print("------------------------------------------------------------")

    return result

# Find all numbers and remove any "()- ", leave plus
def format_phone_numbers(text: str):
    # Define a pattern to match phone numbers
    pattern = re.compile(r'(?:\+)?[\d\s()-.]{8,20}')

    modified_text = text

    # Find all matches in the text
    matches = pattern.findall(text)
    for matched in matches:
        cleaned_number = ' ' + re.sub(r'[^\d+]', '', matched) + ' '
        modified_text = modified_text.replace(matched, cleaned_number)

    return modified_text

def is_email_correct(email: str) -> bool:
    """Check if email was scanned correctly"""
    regex = r'[\w.+-]+@([\w_-]+(?:(?:\.[\w_-]+)+))'

    if(re.fullmatch(regex, email)):
        return True
    else:
        return False

def is_telephone_correct(tel: str) -> bool:
    """Check if it contains something else besides "+-() " and digits"""
    regex = r'^\+?[\d]{6,12}$'

    if(re.fullmatch(regex, tel)):
        return True
    else:
        return False
    
def is_url_correct(url: str) -> bool:
    """Check if it contains (https://)?(www.)?word.word(/query_params))"""
    # Regex gotten from https://stackoverflow.com/questions/6038061/regular-expression-to-find-urls-within-a-string
    # Edited to recognize www.url.com or just url.com
    regex = r'(?:http(?:s)?:\/\/)?(?:www\.)?([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])'

    if(re.fullmatch(regex, url)):
        return True
    else:
        return False
