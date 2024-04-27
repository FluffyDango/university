import spacy
from spacy.tokens import DocBin
from spacy.pipeline.entityruler import EntityRuler
import warnings
from pathlib import Path
import os
import re
from pprint import pprint
from random import shuffle

from pullout import src_path
from .corpus import corpus_lt as corpus


# It should look like this:
# TRAIN_DATA = [
#     ("Grafo (H) Dvaras kavinė UAB \"Hovalta\" Algirdo g. 9b Maišiagala, Vilniaus raj. 4 Mob.: +37065945402, +37065590907 El.paštas: info@grafodvaras.lt www.grafodvaras.lt",
#      {"entities": [(19, 26, "ORG"), (55, 64, "STREET"), (66, 76, "CITY"), (78, 89, "REGION"), (101, 114, "TEL"), (116, 128, "TEL"), (130, 154, "EMAIL"), (155, 170, "URL")]}
#     ),
# ]

nlp = spacy.blank("lt")
ruler = nlp.add_pipe("entity_ruler")

TRAIN_DATA = []
pattern = re.compile(r"\{(.+?)\}\((.+?)\)")

for index, card in enumerate(corpus):
    if card == "":
        continue
    entity_ruler_patterns = []

    matches = pattern.finditer(card)
    for matched in matches:
        word = matched.group(1)
        label = matched.group(2)
        # remove the curly braces and entity_name from the card
        card = card.replace("{" + word + "}" + "(" + label + ")", word)

        entity_ruler_patterns.append({"label": label, "pattern": word})
    
    ruler.add_patterns(entity_ruler_patterns)

    print("\ncard number:", index)
    print(card)
    doc = nlp(card)
    entities = [(ent.start_char, ent.end_char, ent.label_) for ent in doc.ents]
    # print(entities)
    if entities == []:
        warnings.warn("No entities found in sentence")
    else:
        # Print the card and its entities for double cheking
        for ent in entities:
            start, end, label = ent
            print([card[start:end], {"label": label}])
        # Append the card and its entities to the training data
        TRAIN_DATA.append([card, {"entities": entities}])

# pprint(TRAIN_DATA)

print("\n")

def convert(lang: str, TRAIN_DATA, output_path: Path):
    nlp = spacy.blank(lang)
    db = DocBin()
    for text, annot in TRAIN_DATA:
        doc = nlp.make_doc(text)
        ents = []
        for start, end, label in annot["entities"]:
            span = doc.char_span(start, end, label=label)
            if span is None:
                msg = f"Skipping entity [{start}, {end}, {label}] in the following text because the character span '{doc.text[start:end]}' does not align with token boundaries:\n\n{repr(text)}\n"
                warnings.warn(msg)
            else:
                ents.append(span)
        doc.ents = ents
        db.add(doc)
    db.to_disk(output_path)
    print("Successfully created training data at " + str(output_path))


shuffle(TRAIN_DATA)
# Calculate the index that corresponds to 20% of the data
index = int(len(TRAIN_DATA) * 0.2)
DEV_DATA = TRAIN_DATA[:index]

file_path = os.path.abspath(os.path.dirname(__file__))
convert("lt", TRAIN_DATA, os.path.join(file_path, 'lt_train.spacy'))
convert("lt", DEV_DATA, os.path.join(file_path, "lt_dev.spacy"))
# convert("en", TRAIN_DATA, os.path.join(file_path, "en_train.spacy"))
# convert("en", DEV_DATA, os.path.join(file_path, "en_dev.spacy"))