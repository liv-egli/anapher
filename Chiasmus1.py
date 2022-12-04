import spacy

print("Please enter desired file below:")
file = input("")
# das gewünschte Dokument muss unter dem Output eingefügt werden (z. B. Faust.txt)
print("Searching", file, "for chiasmus, please wait a moment :-)")
nlp = spacy.load("de_core_news_sm")
f = open(file, "r")
content = f.read()
doc = nlp(content)

NORMAL = "\033[0m"
BLUE = "\033[94m"
RED = "\033[91m"
YELLOW = "\033[93m"

counter = 0
leftRootToken = None
leftCjToken = None
rightRootToken = None
rightCjToken = None
rootToken = None
hasRootToken = False
cjToken = None
hasCjToken = False
isSentEnd = None
for sent in doc.sents:
    for token in sent:
        if len(sent) < 45:
            if token.dep_ == "ROOT":
                hasRootToken = True
                rootToken = token
            if token.dep_ == "cj":
                hasCjToken = True
                cjToken = token
                if hasRootToken is True and hasCjToken is True:
                    if rootToken.pos_ == cjToken.pos_:
                        isLeftOk = False
                        isRightOk = False
                        if rootToken.n_lefts > 0 and cjToken.n_lefts > 0 and rootToken.n_rights > 0 and cjToken.n_rights > 0:
                            leftRootToken = next(rootToken.lefts)
                            leftCjToken = next(cjToken.lefts)
                            rightRootToken = next(rootToken.rights)
                            rightCjToken = next(cjToken.rights)
                            if rightRootToken.dep_ == leftCjToken.dep_ or rightRootToken.pos_ == leftCjToken.pos_:
                                isRightOk = True
                                if leftRootToken.pos_ != "SPACE":
                                    if leftRootToken.dep_ == rightCjToken.dep_ or leftRootToken.pos_ == rightCjToken.pos_:
                                        isLeftOk = True
                        elif rootToken.n_lefts == 0 and rootToken.n_rights > 0 and cjToken.n_rights > 0 and cjToken.n_lefts > 0:
                            rightRootToken = next(rootToken.rights)
                            rightCjToken = next(cjToken.rights)
                            leftCjToken = next(cjToken.lefts)
                            leftRootToken = "PUNCT"
                            if rightCjToken.pos_ == leftRootToken:
                                isRightOk = True
                                if rightRootToken.dep_ == leftCjToken.dep_ or rightRootToken.pos_ == leftCjToken.pos_:
                                    isLeftOk = True
                        if isLeftOk is True and isRightOk is True:
                            print("\n----\n", BLUE + str(leftRootToken), RED + str(rootToken),
                                  YELLOW + str(rightRootToken), YELLOW + str(leftCjToken),
                                  RED + str(cjToken), BLUE + str(rightCjToken), "\n",
                                  NORMAL + str(leftRootToken.sent))
                            counter = counter + 1

print("\n(:----------------END----------------:)\n", "\nfound", counter, "chiasmi in", file)