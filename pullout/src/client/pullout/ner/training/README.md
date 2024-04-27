To train a pre-existing model specify it in config file in the [initialize] section, e.g.
```
[initialize]
vectors = "lt_core_news_lg"
init_tok2vec = null
vocab_data = null
lookups = null
before_init = null
after_init = null
```

You also need to specify train and dev files.
These are the data that you will be sending to train and recognize. It ends with `.spacy` extension

To generate these, edit the `corpus.py` and launch `prepare_data.py`

`train` is all of the data in the corpus

`dev` is 10%-20% of train data. this is for validation in the training

the dev data is used for the evaluation displayed during training, to select the best model, and for early stopping (the early stopping setting is called patience). If train is too small, dev will take 20%, which might be 0 and it will mean it can't validate. That's why if you see score 0, then that is most likely the case.

To train the model, navigate to this directory and run
```bash
poetry run python -m spacy train config_lt.cfg --output lt_model
```