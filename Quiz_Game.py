import time
#Variables
ans1 = ''
ans2 = ''
ans3 = ''
ans4 = ''
ans5 = ''
options = ['a','b','c','d']
score = 0 
'''Final score is revealed at the end. 
You can modify that to display a correct answer after a user inputs their choice and increase their score.'''

#Introduction to game
print("Welcome to my quizgame!")

#Give user option to start game
accept = input("Are you ready to play? ")
if accept == "yes": #User started the game
    print("Great! Let's play!") 
    time.sleep(1)
   
elif accept == "no": #User quits the game
    print("Goodbye!") 
    time.sleep(1)
    quit()

#Question 1
print() #Print left in blank to have some space between questions while executing program.
print("1) ?") #Empty print to write your own question.
time.sleep(2)

print("a. ")
print("b. ")
print("c. ")
print("d. ")


while True:
    print()
    ans1 = input("Choose your letter answer: ").lower()
    if ans1 not in options: 
        print("Processing ...")
        time.sleep(2)
        print("Not a valid answer. Please pick again.")
        time.sleep(1)
        continue
#Above statement used in case the user writes a letter not in the options list or a word, phrase, etc...
    else:
        print("Processing...")
        time.sleep(2)
        print("Valid answer.")
        time.sleep(1)
        print("Onto the next question.")
        break
#Above statement used time.sleep() for theatrics. You can delete them if needed.

if ans1 == 'a': #This is where you would pick which answer is right.
    score = score + 1
#Above statement adds a point to our user's score.
    

#Question 2
print()
print("2) ?")
time.sleep(2)

print("a. ")
print("b. ")
print("c. ")
print("d. ")


while True:
    print()
    ans2 = input("Choose your letter answer: ").lower()
    if ans2 not in options:
        print("Processing ...")
        time.sleep(2)
        print("Not a valid answer. Please pick again.")
        time.sleep(2)
        continue
    else:
        print("Processing...")
        time.sleep(2)
        print("Valid answer.")
        time.sleep(2)
        print("Onto the next question.")
        break

if ans2 == '':
    score = score + 1

#Question 3
print()
print("3) ?")
time.sleep(2)

print("a. ")
print("b. ")
print("c. ")
print("d. ")

while True:
    print()
    ans3 = input("Choose your letter answer: ").lower()
    if ans3 not in options:
        print("Processing...")
        time.sleep(2)
        print("Not a valid answer. Please pick again.")
        time.sleep(2)
        continue
    else:
        print("Processing...")
        time.sleep(2)
        print("Valid answer.")
        time.sleep(2)
        print("Onto the next question.")
        break

if ans3 == '':
    score = score + 1

#Question 4
print()
print("4) ?")
time.sleep(2)

print("a. ")
print("b. ")
print("c. ")
print("d. ")


while True:
    print()
    ans4 = input("Choose your letter answer: ").lower()
    if ans4 not in options:
        print("Processing...")
        time.sleep(2)
        print("Not a valid answer. Please pick again.")
        time.sleep(2)
        continue
    else:
        print("Processing...")
        time.sleep(2)
        print("Valid answer.")
        time.sleep(2)
        print("Onto the next question.")
        break

if ans4 == '':
    score = score + 1


print()
print("5) ?")
time.sleep(2)

print("a. ")
print("b. ")
print("c. ")
print("d. ")


while True:
    print()
    ans5 = input("Choose your letter answer: ").lower()
    if ans5 not in options:
        print("Processing...")
        time.sleep(2)
        print("Not a valid answer. Please pick again.")
        time.sleep(2)
        continue
    else:
        print("Processing...")
        time.sleep(2)
        print("Valid answer.")
        time.sleep(2)
        break

if ans5 == '':
    score = score + 1

#Aquí finaliza el juego
print("¡Congratulations for making it until the end!")
time.sleep(2)
print("Let us look at your results now...")
time.sleep(2)

#Here we show results and final message
print("You scored...")
time.sleep(2)

time.sleep(2)
print(str(score) + " out of 5!" )

if score < 3:
    time.sleep(1)
    print("Too bad :(. You lost, but you can always try again.") #These messages can be edited to whatever you want.
else:
    print("You've won!")