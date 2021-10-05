import random

stages = [  """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """
]
words=["hello", "catch", "basketball"]
word=random.choice(words)
blanks=''
for each in word :
    blanks+='-'
print(blanks)
j=len(stages)-1
while blanks!=word:
    if j==0:
        print("You have run out of guesses! Try again!")
        break
    letter=input("guess a character")
    i=0
    if letter in word and word.count(letter)==1:
        blanks=blanks[:word.index(letter)]+letter+blanks[word.index(letter)+1:]
        print(blanks)
    elif letter in word and word.count(letter)>1:
        occs=[i for i, x in enumerate(word) if x == letter]
        for each in occs :
            blanks=blanks[:each]+letter+blanks[each+1:]
        print(blanks)

    elif letter not in word :
        print("wrong guess!")
        print(stages[j])
        j-=1
if blanks==word:
    print("You have won!")
            
