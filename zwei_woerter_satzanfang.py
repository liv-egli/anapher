import token

import spacy

nlp = spacy.load("de_core_news_sm")
f = open('/Users/liv/Desktop/21000-0.txt', 'r')
content = f.read()
doc = nlp(content)



def afterComma():
    previousToken = "."
    firstToken = ""
    for token in doc:
        if previousToken == ',' or previousToken == ';' or previousToken == ':' or previousToken == '.' or previousToken == '!' or previousToken == '?' or previousToken == "_":
            if token.lower_ == firstToken:
                print("0", token.text)
                print("1", token.sent)
            firstToken = token.lower_
        previousToken = token.lower_


afterComma()



# Example: find two words
# currentToken = ""
# for token in doc:
#     if currentToken == token.text:
#         print(token)
#     currentToken = token.text



# Example: sent.start anapher



# previousToken = ""
# for token in doc:
#     if token.is_sent_start:
#         if previousToken == token.text:
#             print(token)
#         previousToken = token.text






# Example: enumerate sentences
# for sent_i, sent in enumerate(doc.sents):
#     for token in sent:
#         print(sent_i, token.i, token.text)



