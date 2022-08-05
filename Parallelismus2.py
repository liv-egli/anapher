import spacy

nlp = spacy.load("de_core_news_sm")
doc = nlp("Ich bin entdeckt, ich bin durchschaut.")


hasCj = False
hasRoot = False
cjToken = None
rootToken = None
for sent in doc.sents:
    for token in sent:
        if token.dep_ == "cj":
            hasCj = True
            cjToken = token
        if token.dep_ == "ROOT":
            hasRoot = True
            rootToken = token
    if hasRoot is True and hasCj is True:
        if cjToken.pos_ == rootToken.pos_:
            print(cjToken, rootToken, token.sent)


leftRoot = False
auxToken = "ROOT"
leftRootToken = None
if token.dep_ == auxToken:
    if (leftRootToken is not None) and \
            (token.is_space is False):
        leftRoot = True
    auxToken = token.dep_
leftRootToken = token

leftCj = False
auxToken = "cj"
leftCjToken = None
if token.dep_ == auxToken:
    if (leftCjToken is not None) and \
            (token.is_space is False):
        leftCj = True
    auxToken = token.dep_
leftCjToken = token

if leftRoot is True and leftCj is True:
    if leftCjToken.dep_ == leftRootToken.dep_:
        print(token.sent)

rightRoot = False
auxToken = None
rightRootToken = None
if token.dep_ == "ROOT":
    if (rightRootToken is not None) and \
            (token.is_space is False):
        rightRoot = True
        rightRootToken = token
    auxToken = token.dep_








