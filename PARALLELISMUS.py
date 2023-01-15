import spacy

print("Please enter desired file below:")
file = input("")
# das gewünschte Dokument muss unter dem Output eingefügt werden (z. B. Faust.txt)
print("Searching", file, "for parallelism, please wait a moment :-)")
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
for sent in doc.sents:
    for token in sent:
    # die Schlaufe ist pro Satz im Dokument und pro Token im Satz
        if len(sent) < 45:
            # der Satz soll nicht länger als 45 Zeichen sein
            if token.dep_ == "ROOT":
                hasRootToken = True
                rootToken = token
            if token.dep_ == "cj":
                hasCjToken = True
                cjToken = token
                # ein Parallelismus besitzt je ein Root- und ein cj-Token: muss True sein
                if hasRootToken is True and hasCjToken is True:
                    if rootToken.pos_ == cjToken.pos_:
                        # Root- und cj-Token müssen die gleiche Wortart haben
                        isLeftOk = False
                        isRightOk = False
                        # nun wird geschaut, ob es links und rechts davon ein Token hat:
                        if file == "Raeuber.txt":
                            if rootToken.n_lefts > 0 and cjToken.n_lefts > 0:
                                leftRootToken = next(rootToken.lefts)
                                leftCjToken = next(cjToken.lefts)
                                if leftRootToken.pos_ != "SPACE":
                                    # dieses Token soll kein Leerschlag sein
                                    if leftRootToken.dep_ == leftCjToken.dep_ or leftRootToken.pos_ == leftCjToken.pos_:
                                        isLeftOk = True
                                        # es soll entweder die Abhängigkeit oder die Wortart beider linken Wörter gleich sein
                            if rootToken.n_rights > 0 and cjToken.n_rights > 0:
                                rightRootToken = next(rootToken.rights)
                                rightCjToken = next(cjToken.rights)
                                if rightRootToken.dep_ == rightCjToken.dep_ or rightRootToken.pos_ == rightCjToken.pos_:
                                    # gleiches Verfahren mit dem Token rechts
                                    if leftRootToken is not None:
                                        if (rightCjToken.i - leftRootToken.i) < 27 and (sent.end - rightCjToken.i) < 16:
                                            # die beiden weites entfernten untersuchten Wörter sollen nicht zu weit voneinander weg sein
                                            # das letzte untersuchte Wort soll nicht zu weit vom Satzende entfernt sein
                                            # nur für "Die Raeuber" wegen ungenügender Satztrennung
                                            isRightOk = True
                                            # stimmen diese Bedingungen wird auch das rechte "True" ausgewertet
                            elif cjToken.n_rights == 0 and rootToken.n_rights > 0 and rootToken.n_lefts > 0 and cjToken.n_lefts > 0:
                                # Sonderfall: cj-Token bildet das Satzende
                                rightCjToken = "punct"
                                rightRootToken = next(rootToken.rights)
                                leftRootToken = next(rootToken.lefts)
                                leftCjToken = next(cjToken.lefts)
                                if (cjToken.i - leftRootToken.i) < 26:
                                    if rightCjToken == rightRootToken.dep_:
                                        # die rechte Abhängikeit soll gleich sind: beide sollen Satzzeichen sein
                                        isRightOk = True
                                    if leftRootToken.pos_ != "SPACE":
                                        if leftRootToken.dep_ == leftCjToken.dep_ or leftRootToken.pos_ == leftCjToken.pos_:
                                            isLeftOk = True
                            if isLeftOk is True and isRightOk is True:
                                print("\n----\n", BLUE + str(leftRootToken), RED + str(rootToken),
                                      YELLOW + str(rightRootToken), BLUE + str(leftCjToken),
                                      RED + str(cjToken), YELLOW + str(rightCjToken), "\n",
                                      NORMAL + str(leftRootToken.sent))
                                counter = counter + 1

                        else:
                            if rootToken.n_lefts > 0 and cjToken.n_lefts > 0:
                                leftRootToken = next(rootToken.lefts)
                                leftCjToken = next(cjToken.lefts)
                                if leftRootToken.pos_ != "SPACE":
                                    if leftRootToken.dep_ == leftCjToken.dep_ or leftRootToken.pos_ == leftCjToken.pos_:
                                        isLeftOk = True
                            if rootToken.n_rights > 0 and cjToken.n_rights > 0:
                                rightRootToken = next(rootToken.rights)
                                rightCjToken = next(cjToken.rights)
                                if rightRootToken.dep_ == rightCjToken.dep_ or rightRootToken.pos_ == rightCjToken.pos_:
                                    isRightOk = True
                            elif cjToken.n_rights == 0 and rootToken.n_rights > 0 and rootToken.n_lefts > 0 and cjToken.n_lefts > 0:
                                rightCjToken = "punct"
                                rightRootToken = next(rootToken.rights)
                                leftRootToken = next(rootToken.lefts)
                                leftCjToken = next(cjToken.lefts)
                                if (cjToken.i - leftRootToken.i) < 26:
                                    if rightCjToken == rightRootToken.dep_:
                                        isRightOk = True
                                    if leftRootToken.pos_ != "SPACE":
                                        if leftRootToken.dep_ == leftCjToken.dep_ or leftRootToken.pos_ == leftCjToken.pos_:
                                            isLeftOk = True
                            if isLeftOk is True and isRightOk is True:
                                print("\n----\n", BLUE + str(leftRootToken), RED + str(rootToken), YELLOW + str(rightRootToken), BLUE + str(leftCjToken),
                                      RED + str(cjToken), YELLOW + str(rightCjToken), "\n", NORMAL + str(leftRootToken.sent))
                                counter = counter + 1

print("\n(:----------------END----------------:)\n", "\nfound", counter, "parallelismi in", file)