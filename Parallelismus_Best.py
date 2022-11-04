import spacy

nlp = spacy.load("de_core_news_sm")
f = open("Faust.txt", "r")
content = f.read()
doc = nlp(content)

counter = 0
leftRootToken = None
leftCjToken = None
rightRootToken = None
rightCjToken = None
rootToken = None
hasRootToken = False
cjToken = None
hasCjToken = False
for sent in doc.sents:
    for token in sent:
        # if token.text == "~":
        #     break
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
                        if rootToken.n_lefts > 0 and cjToken.n_lefts > 0:
                            leftRootToken = next(rootToken.lefts)
                            leftCjToken = next(cjToken.lefts)
                            if leftRootToken.dep_ == leftCjToken.dep_ or leftRootToken.pos_ == leftCjToken.pos_:
                                isLeftOk = True
                        if rootToken.n_rights > 0 and cjToken.n_rights > 0:
                            rightRootToken = next(rootToken.rights)
                            rightCjToken = next(cjToken.rights)
                            if rightRootToken.dep_ == rightCjToken.dep_ or rightRootToken.pos_ == rightCjToken.pos_:
                                isRightOk = True
                        # elif cjToken.n_rights == 0 and rootToken.n_rights > 0 and rootToken.n_lefts > 0 and cjToken.n_lefts > 0:
                        #     rightCjToken = "punct"
                        #     rightRootToken = next(rootToken.rights)
                        #     leftRootToken = next(rootToken.lefts)
                        #     leftCjToken = next(cjToken.lefts)
                        #     if rightCjToken == rightRootToken.dep_:
                        #         isRightOk = True
                        #         if leftRootToken.dep_ == leftCjToken.dep_ or leftRootToken.pos_ == leftCjToken.pos_:
                        #             isLeftOk = True
                        if isLeftOk is True and isRightOk is True:
                            print("\n----\n", leftRootToken, rootToken, rightRootToken, leftCjToken, cjToken, rightCjToken,  "\n", leftRootToken.sent)
                            counter = counter + 1

print("found", counter, "parallelismi")




