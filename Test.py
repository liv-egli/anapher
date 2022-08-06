import spacy

nlp = spacy.load("de_core_news_sm")
doc = nlp("Das Schiffchen fliegt, der Webstuhl kracht.")

for token in doc:
    print(token.text, token.dep_, token.pos_)
