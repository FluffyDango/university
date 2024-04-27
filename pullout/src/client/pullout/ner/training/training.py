# Train the model and save it in the lt_model folder.
from pullout import src_path
from spacy.cli.train import train
import os
import shutil

language = "lt"

output_path = os.path.join(src_path, language+'_model')

training_folder_path = os.path.join(src_path, 'ner', 'training')
config_path = os.path.join(training_folder_path, 'config_'+language+'.cfg')

train_path = os.path.join(training_folder_path, language+'_train.spacy')
dev_path = os.path.join(training_folder_path, language+'_dev.spacy')

train_args = {
    "paths.train": train_path,
    "paths.dev": dev_path,
}

train(config_path=config_path, output_path=output_path, overrides=train_args)

# Move the best model to the ner folder where it is expected to be.
lang_model_path = os.path.join(src_path, 'ner', language+'_model')
if os.path.exists(lang_model_path):
    shutil.rmtree(lang_model_path)
shutil.move(os.path.join(output_path, 'model-best'), lang_model_path)
shutil.rmtree(output_path)