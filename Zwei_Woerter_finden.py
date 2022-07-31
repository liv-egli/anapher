import spacy
from spacy.tokens import Token

nlp = spacy.load("de_core_news_sm")
doc = nlp("Vielleicht steht die Idee Idee im Wettbewerb mit anderen Ideen. Vielleicht auch nicht.")

# currentToken = ""
# for token in doc:
#     if currentToken == token.text:
#         print(token)
#     currentToken = token.text

currentToken = ""
for token in doc:
    if currentToken == token.text:
        print(token)
    currentToken = token.text








