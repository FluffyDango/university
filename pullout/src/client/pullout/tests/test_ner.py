import unittest

from pullout.ner_processor import get_entities, detect_language

def check_entities(self, entities, all_entities):
    verified_entities = {key: [] for key in all_entities}
    for ent in entities:
        if ent.label_ not in all_entities:
            continue
        if ent.text in all_entities[ent.label_]:
            verified_entities[ent.label_].append(ent.text)
    
    result = {}
    for key in verified_entities:
        result[key] = [item for item in all_entities[key] if item not in verified_entities[key]]

    if result:
        err_msg = "Failed to find " + str(result)
        self.fail(err_msg)


class TestNER(unittest.TestCase):
    def test_detect_language(self):
        text = "This is an English sentence."
        self.assertEqual(detect_language(text), "en")

        text = "Čia yra lietuviškas sakinys."
        self.assertEqual(detect_language(text), "lt")

    def test_get_entities_1(self):
        text = """
            Twitter is an American microblogging and social networking
            service on which users post and interact with messages known as tweets.
            Elon Musk is not only the CEO of Tesla but also Twitter.
            """
        all_entities = {
            "ORG": ["Tesla", "Twitter"],
            "PERSON": ["Elon Musk"]
        }
        entities = get_entities(text, "en")
        check_entities(self, entities, all_entities)


    def test_get_entities_2(self):
        text = """
            LINE-X
            PROTECTIVE COATINGS
            GENADIJUS KAREIVA
            Pardavimų vadovas
            UAB "Line-x" LT
            V.Bielskio g. 6, LT-76126
            Siauliai, Lietuva
            Tel: +370 698 58 099
            el.p. genadijus@line-x.lt
            www.line-x.lt
            APSAUGINES / HIDROIZOLIACINES / GRINDŲ DANGOS PASTATŲ ŠILTINIMAS
            """
        all_entities = {
            "ORG": ["Line-x"],
            "PERSON": ["GENADIJUS KAREIVA"],
            "TEL": ["+370 698 58 099"],
            "EMAIL": ["genadijus@line-x.lt"],
            "URL": ["www.line-x.lt"],
            "ADDR": ["V.Bielskio g. 6, LT-76126 Siauliai, Lietuva"],
            "TITLE": ["Pardavimų vadovas"],
        }
        entities = get_entities(text, "lt")
        check_entities(self, entities, all_entities)

    def test_get_entities_3(self):
        text = """
            CD-R/RW, DVD +/-R/RW, BD-R/RE, FLASH
            Kompiuteriai ir komponentai
            Skaitmenine technika
            MediaSpektras
            LED ekranai
            Stovai, deklai, dezutes
            Maitinimo blokai, laidai, ausinės
            Piotr Jasinski
            direktorius
            UAB "MediaSpektras", Pylimo g. 49-3, 01137 Vilnius
            Tel./Fax +370 5 260 82 60
            Mob.+370 676 04754
            El.p. piotrjasinski@dvadr.lt, skype: piotrjasO0 
            """
        all_entities = {
            "ORG": ["MediaSpektras"],
            "PERSON": ["Piotr Jasinski"],
            "TEL": ["+370 5 260 82 60", "+370 676 04754"],
            "EMAIL": ["piotrjasinski@dvadr.lt"],
            "ADDR": ["Pylimo g. 49-3, 01137 Vilnius"]
        }
        entities = get_entities(text, "lt")
        check_entities(self, entities, all_entities)

    def test_get_entities_4(self):
        text = """
            Grafo (H) Dvaras
            kavinė
            UAB "Hovalta"
            Algirdo g. 9b
            Maigiagala, Vilniaus raj. 4
            Mob.: +37065945402, +37065590907
            El.paštas: info@grafodvaras.lt
            www.grafodvaras.lt
            """
        all_entities = {
            "ORG": ["Hovalta"],
            "PERSON": ["Piotr Jasinski"],
            "TEL": ["+370 5 260 82 60", "+370 676 04754"],
            "EMAIL": ["info@grafodvaras.lt"],
            "URL": ["www.grafodvaras.lt"],
            "ADDR": ["Algirdo g. 9b, Maigiagala, Vilniaus raj. 4"]
        }
        entities = get_entities(text, "lt")
        check_entities(self, entities, all_entities)
        
