from Classes import Card, Hand
import random

'''c1=Card(x,y)
hand=Hand()
dhand=Hand()
def drawcard():
    suits="cdsh"
    Card(random.randint(1,13),random.choice(suits))
'''
print("Welcome to Serendipity")
hand=Hand()
dhand=Hand()
suits="cdsh"
x=input("Play BJ?\n Y/N\n").upper()

if x == "Y":
    card = []
    card.append(Card(random.randint(1,13),random.choice(suits)))
    card.append(Card(random.randint(1,13),random.choice(suits)))
    i = 0
    while   (i<len(card)):
            hand.addCard(card[i].bjValue())
            print(card[i].bjValue())
            i+=1
    if sum(hand.hand)==11 and (hand.hand[0]==1 or hand.hand[1]==1):
                print("BLACKJACK",
                      "\n************"
                      "\n  You Win!",
                      "\n************")
                exit()
    while True:
        print("you are at: \n", sum(hand.hand))
        option = input("1) Hit \n2) Stay\n")
        if 	option=="1":
            card.append(Card(random.randint(1,11),random.choice(suits)))
            hand.addCard(card[i].bjValue())
            j=0
            while   (j<len(card)):
                print(card[j].bjValue())
                j+=1
            if  (sum(hand.hand)>21):
                print("You lose sucker")
                break

        if	option=="2":
            while   (sum(dhand.hand)<17):
                    dhand.addCard(Card(random.randint(1,11),random.choice(suits)).bjValue())
            print("Dealer has: \n",sum(dhand.hand))
            if  (sum(dhand.hand)>21):
                print("Dealer Bust\nYou win")
                break
            elif(sum(hand.hand)>sum(dhand.hand) and sum(hand.hand)<=21):
                print("You win")
                break
            elif(sum(hand.hand)==sum(dhand.hand)):
                print("Draw")
                break
            else:
                print("You lose")
                break
        else:
            print("invalid input")
    else:
        exit()

