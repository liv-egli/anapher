import token

import spacy
from spacy.tokens import Token

nlp = spacy.load("de_core_news_sm")
doc = nlp("")
# f = open('/Users/liv/Desktop/21000-0.txt', 'r')
# content = f.read()
# doc = nlp(content)

# Example: find two words
# currentToken = ""
# for token in doc:
#     if currentToken == token.text:
#         print(token)
#     currentToken = token.text


currentToken = ""
for token in doc:
    if token.is_sent_start:
        if currentToken == token.text:
            print(token)
        currentToken = token.text


# for sent_i, sent in enumerate(doc.sents):
#     for token in sent:
#         print(token.i, token.text)

# def afterComma():
#     previousToken = ""
#     for token in doc:
#         if previousToken == ',' or previousToken == ';' or previousToken == ':':
#             print(token.text)
#         previousToken = token.text

# def afterComma():
#     previousToken = ""
#     for token in doc:
#         if previousToken == ',' or previousToken == ';' or previousToken == ':':
#             print(True)
#         previousToken = token.text
#
#
# afterComma()




