import spacy

print("Please enter desired file below:")
file = input("")
# das gewünschte Dokument muss unter dem Output eingefügt werden (z. B. Raeuber.txt)
print("Searching", file, "for parallelism, please wait a moment :-)")
nlp = spacy.load("de_core_news_sm")
f = open(file, "r")
content = f.read()
doc = nlp(content)

NORMAL = "\033[0m"
BLUE = "\033[94m"
RED = "\033[91m"
YELLOW = "\033[93m"
BOLD = "\033[1m"


# Artikel zählen nur als Anapher wenn sie auf die gleiche Art und Weise gebraucht werden, also die gleiche Dependency haben.
# für alle anderen Wörter spielt die Abhängikeit keine Rolle => return True
def has_same_dependency(first_tkn, tkn):
    # das Lemma von "der", "die" or "das" ist immer "der"
    if tkn.lemma_ == "der":
        if tkn.dep_ == first_tkn.dep_:
            return True
        else:
            return False
    else:
        return True


counter = 0
# previousToken = "."
# das erste Wort in einem Dokument soll als Satzanfang beachtet werden, weshalb das vorherige ein Satzzeichen sein muss.
firstToken = None
for token in doc:
    # folgende Anweisungen werden für jedes Token im Dokument durchgeführt
    if token.is_space is False:
        # Leerschläge und Umschläge sollen nicht beachtet werden
        if token.is_sent_start:
            # nur wenn das previousToken ein Satzzeichen ist, wird das folgende Wort zum firstToken
            if (firstToken is not None) and \
                    (token.is_space is False) and \
                    (firstToken.is_space is False) and \
                    (token.is_punct is False) and \
                    (firstToken.is_punct is False) and \
                    has_same_dependency(token, firstToken) and \
                    (token.lower_ == firstToken.lower_) and \
                    (token.lemma_ == firstToken.lemma_) and \
                    token.text is not firstToken.sent and token.text is not token.sent:
                # Leerschläge und Satzzeichen sollen nicht beachtet werden
                # die zuvor erstellte Funktion wird hier ins Programm eingebaut
                # zwei aufeinanderfolgende Token nach einem Satzzeichen sollen in der Grundform und ohne Beachtung der Gross- und Kleinschreibung miteinander verglichen werden.
                counter = counter + 1
                print("\n", "------", "\n", "\n", "firstToken: ", YELLOW + firstToken.text, NORMAL)
                print("1", firstToken.sent)
                print("2", token.sent)
            firstToken = token
            # das Satzanfang-Token wird immer zum firstToken, um mit dem nächsten Satzanfang-Token verglichen werden zu können



print("\n", "found", BOLD + str(counter), "anapher", NORMAL + "in", file)