import random as r

class card:
    def __init__(self, suitNumber):
      self.i = suitNumber

deck = []
for x in range(1,14):
  deck.append(card([x,'of Spades']))
  deck.append(card([x,'of Hearts']))
  deck.append(card([x,'of Diamonds']))
  deck.append(card([x,'of Clubs']))

dectionary = {card.i[0] : card for card in deck}

def play(deck=deck):
  hand,ehand = deal(deck)
  score = 0
  while len(deck) > 0:
    hand = sorted(hand, key = lambda hand:hand.i[0])
    display(hand,score)
    #display(ehand)
    askFor(hand, ehand, deck)
    #return hand,ehand

def calcScore(hand):
  return hand.count(card for card in hand)

def display(hand,score=0):
  print('Score: '+str(score))
  print("This is your hand:")
  i = 1
  for card in hand:
    print(card.i)
    i += 1
    
def askFor(hand,ehand,deck):
  """
  Prompts you input the index of the card you want. 
  If your opponent has that number, you take all the cards
  with the number of the card you asked for. Otherwise, the
  program prints 'go fish'.
  """
  print("Input card # you would like to ask for.")
  reqNum = int(input())
  handInts = [x.i[0] for x in hand]
  while reqNum not in handInts: #testing for valid input
    reqNum = int(input('Please input a number \n'))
  #reqNum = hand[req-1].i[0] #the number of the card being asked for, an int
  eNum = [card.i[0] for card in ehand] #this will be a list of ints
  if reqNum in eNum:
    cardTake = [card for card in ehand if card.i[0]==reqNum]
    for card in cardTake:
        print("You got a",card.i,"!")
        hand.append(card)
        ehand.remove(card)      
  else:
    print('Go fish!')
    hand = draw(hand,deck)
    
def deal(deck):
  hand = []
  ehand = []
  for x in range(5):
    hand = draw(hand,deck)
    ehand = draw(ehand,deck)
  return hand,ehand

def draw(hand,deck):
  hand.append(deck.pop(r.randint(0,len(deck)-1)))
  return hand
