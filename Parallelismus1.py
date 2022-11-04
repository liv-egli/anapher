# myAge = str(18)
# print("Du bist " + str(int(myAge) + 1) + " in einem Jahr")
#
# Zoé = int(20)
# print("Zoé wird im Januar " +str(int(Zoé) + 1) + " Jahre alt.")
#
# print("Zoé und Liv sind zusammen " + str(int(Zoé) + int(myAge)) + " Jahre alt.")
# print("spam" + "spamspam")
#
# spam = 99
# print("I've eaten " + str(spam) + " Burger")
#
# spam = True
# print(spam)
# print(42 < 43)
# print("dog" == "cat")
# print(42 == 42.0)
#
# print(str(myAge) < str(Zoé))
#
# print(True and False)
#
# print(5<6 or 6<5)
#
# myAge = 17
# myName = "Jonas"
# if myName == "Liv":
#     print("Hei Liv :)")
# else:
#     print("Hei Glüngi!")
#
#
# myAge = 20
# myName = "Zoé"
# if myName == "Liv":
#     print("Hei Liv :)")
# elif myAge < 18:
#     print("Du bist ein riesen Glüngi!")
# elif myAge == 20:
#     print("Salut Grögi")
# elif myName == "Zoé":
#     print("Salut Kumpi!")
# else:
#     print("Hei Glüngi!")
#
#
# spam = 0
# if spam < 5:
#     print('Hello, liv.')
#     spam = spam + 1
#
# spam = 0
# while spam < 5:
#     print('Hello, world.')
#     spam = spam + 1
#
#
#
# print("My name is")
# for i in range(4):
#     print("Jimmy Four Times (" + str(i) + ")")
#
# total = 0
# for num in range(101):
#     total = total + num
#     print(total)
#     if total > 55:
#         break
#
# print('My name is')
# i = 0
# while i < 5:
#     print('Jimmy Five Times (' + str(i) + ')')
#     i = i + 1
#
# total = 0
# for num in range(4, 10):
#     total = total + num
#     print(total)
#
# tot = 0
# for i in range(0, 10, 2):
#     tot = tot - i
#     print(tot)
#
# for i in range(5, -1, -1):
#     print(i)
#
# import random, sys, os, math
# for i in range(5):
#     print(random.randint(1, 10))
#
# import random
# secretNumber = random.randint(1, 20)
# print('I am thinking of a number between 1 and 20.')
# for guessesTaken in range(1, 7):
#     print('Take a guess.')
#     guess = int(input())
# if guess < secretNumber:
#     print('Your guess is too low.')
# elif guess > secretNumber:
#         print('Your guess is too high.')
# else:
#     if guess == secretNumber:
#         print('Good job! You guessed my number in ' + str(guessesTaken) + 'guesses!')
#     else:
#         print('Nope. The number I was thinking of was ' + str(secretNumber))

# def hello(name):
#     print('Hello, ' + name)
#
# hello('Alice')
# hello('Bob')
#
# def afterComma(ok):
#     previousToken = ""
#     for token in doc:
#         if previousToken == ',' or previousToken == ';' or previousToken == ':':
#             print(token.text + ok)
#         previousToken = token.text
#
#
# afterComma("True")

# import spacy

# nlp = spacy.load("de_core_news_sm")
# doc = nlp("Ich schreibe jetzt, ich schreibe, was ich will, ich schreibe für mein Leben gern.")

# for token in doc:
#   print(token.text, token.lower_)
#
# f = open('21000-0.txt', 'r')
# content = f.read()
# print(content)
# f.close()

import spacy
import token as token

nlp = spacy.load("de_core_news_sm")
doc = nlp("Ich bin entdeckt, ich bin durchschaut.")

previousToken = token.is_sent_start
tokenNum = 0
sentNum = -1
for sent_i, sent in enumerate(doc.sents):
    for token in sent:
        if (sent_i == sentNum + 1) and \
            (token.i == tokenNum):
            if (token.dep_ == previousToken.dep_):
                print(token.text, token.dep_)
                print(previousToken.text, previousToken.dep_)
            previousToken = token
            tokenNum = token.i + 1
            sentNum = sent_i - 1
        sentNum = sent_i








# previousNum = 0
# for token in doc.sents:
#     if len(token) == previousNum:
#         print(token.sent)
#     len(token) == previousNum








