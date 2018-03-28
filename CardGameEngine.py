import random as r

class card:
  def __init__(self, suitNumber):
    self.i = suitNumber

class playerHand:
  def __init__(self):
    self.cards = []
  def draw(self,deck):
    self.cards.append(deck.pop(r.randint(0,len(deck)-1)))

deck = []
for x in range(1,14):
  deck.append(card([x,'of Spades']))
  deck.append(card([x,'of Hearts']))
  deck.append(card([x,'of Diamonds']))
  deck.append(card([x,'of Clubs']))

boyo = playerHand()
billy = playerHand()


for x in range(5):
  boyo.draw(deck)
  billy.draw(deck)

dectionary = {card.i[0] : card for card in deck}

def play(deck=deck):
  hand,ehand = deal(deck)
  score = 0
  eScore = 0
  while len(deck) > 0:
    take = True
    while take and len(deck) > 0:
      hand = sorted(hand, key = lambda hand:hand.i[0])
      display(hand,score)
      take = askFor(hand,ehand,deck)
      score = calcScore(hand,score)
      """
      print('ehand')
      display(ehand,score)
      """
    display(hand,score)
    eTurn(hand,ehand,deck)
    calcScore(ehand,eScore,False)
    #return hand,ehand


#make scorey boi for ehand
def calcScore(hand,score,who=True):
  k = []
  for card in hand:
    k.append(card.i[0])
  for x in k:
    if k.count(x) > 3:
      a = x
      score += 1
      print(5*"-"+(not who)*"Your opponent played the"+who*" You played the "+str(a)+"'s!"+5*"-")     
      for card in hand:
        if card.i[0] == a:
          hand.remove(card)
      break
  #hand.count(card for card in hand)
  return score

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
  take = False
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
    print('You can go again.')
    take = True  
  else:
    print('Go fish!')
    draw(hand,deck)
  return(take)
    
def deal(deck):
  hand = []
  ehand = []
  for x in range(5):
    draw(hand,deck)
    draw(ehand,deck)
  return hand,ehand

def eTurn(hand,ehand,deck):
  req = ehand[r.randint(0,len(ehand)-1)].i[0] #this will be an int
  lies = input("Do you have a "+str(req)+"?")
  k = [card.i[0] for card in hand]
  m = []
  if req in k:
    for card in hand:
      if card.i[0] == req:
        print("You gave your opponent the",card.i)
        hand.remove(card)
        m.append(card)
    ehand.extend(m)
  else:
    print("You say Go Fish!")
    draw(ehand,deck)
