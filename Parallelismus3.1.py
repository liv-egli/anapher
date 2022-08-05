import spacy

nlp = spacy.load("de_core_news_sm")
doc = nlp("Vertrauen ist gut, Kontrolle ist besser.")


rightRoot = False
depToken = None
auxRootToken = None
rightRootToken = None
for sent in doc.sents:
    for token in sent:
        if auxRootToken is not None:
            if depToken == "ROOT":
                rightRoot = True
                rightRootToken = token
                break
            depToken = token.dep_
        auxRootToken = token

rightCj = False
depToken = None
auxCjToken = None
rightCjToken = None
for sent in doc.sents:
    for token in sent:
        if auxCjToken is not None:
            if depToken == "cj":
                rightCj = True
                rightCjToken = token
                break
            depToken = token.dep_
        auxCjToken = token



leftRoot = False
auxToken = "ROOT"
leftRootToken = None
for sent in doc.sents:
    for token in sent:
        if token.dep_ == auxToken:
            if (leftRootToken is not None) and \
                    (token.is_space is False) and \
                    (token.is_punct is False):
                leftRoot = True
                break
            auxToken = token.dep_
        leftRootToken = token

leftCj = False
auxToken = "cj"
leftCjToken = None
for sent in doc.sents:
    for token in sent:
        if token.dep_ == auxToken:
            if (leftCjToken is not None) and \
                    (token.is_space is False) and \
                    (token.is_punct is False):
                leftCj = True
                break
            auxToken = token.dep_
        leftCjToken = token


if leftRoot is True and leftCj is True:
    if rightCj is True and rightRoot is True:
        if leftCjToken.dep_ == leftRootToken.dep_:
            if rightCjToken.dep_ == rightRootToken.dep_:
                if auxRootToken.pos_ == auxCjToken.pos_:
                    print(leftCjToken.sent)
                    print(leftRootToken.dep_, auxRootToken.pos_, rightRootToken.dep_, leftCjToken.dep_, auxCjToken.pos_, rightCjToken.dep_)








# if rightCj is True and rightRoot is True:
#     if auxRootToken.pos_ == auxCjToken.pos_:
#         if rightCjToken.dep_ == rightRootToken.dep_:
#             print(rightCjToken.sent, rightCjToken, rightRootToken)

# if leftRoot is True and leftCj is True:
#     if leftCjToken.dep_ == leftRootToken.dep_:
#         if auxRootToken.pos_ == auxCjToken.pos_:
#             print(leftCjToken.sent, leftCjToken, leftRootToken)







