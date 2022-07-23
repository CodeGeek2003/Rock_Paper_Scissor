import random
score1=0
score2=0
list1 = ["r" , "p" , "s"]
while True:
    choice1 = input("choose r for rock, p for paper, s for scissor: ")
    po = random.randint(0,2)
    choice2=list1[po]
    if choice1 == choice2:
        score2+=1
    elif choice1 == 'p'and choice2 == 's':
        score2+=1
    elif choice1 == 's' and choice2 == 'r':
        score2+=1
    elif choice1 == 'p' and choice2 == 'r':
        score2+=1
    else:
        score1+=1
    print("your choice is: ", choice1, " and the computer choice is: ",choice2)
    play_again=input("do you want to play again y/n ").lower()
    if play_again=='n':
        break
if score2>score1:
    print("you lost ):")
elif score1==score2:
    print("Tie!")
else:
    print("YOU WIN :)")