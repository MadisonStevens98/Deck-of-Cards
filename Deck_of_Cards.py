import random #importing random module, which allows to use random commands

deck = [] #list of cards, uses card objects will have 52 cards

class Card(): #This is our card class
  
  def __init__(self, rank, suit):  #initializing, creating our object
    self.rank = rank #rank, example ace, king, 5, 10 etc.
    self.suit = suit #4 suits, hearts, diamonds, spades, clubs
    deck.append(self) #adds card to the deck
  
    
  def display(self):
    print("Card: " + str(self.rank) + " of " + self.suit)
  

########################################################################################
#making deck
###################################################################################
#for loop to make all hearts
for i in range(1, 14):  #for loop, from 1-13
  #for loop to make all hearts
  
  if i == 1: #checking if i = 1 then its an ace
    newcard = Card("ace", "hearts")
  
  elif i == 11: #elif = else if
    newcard = Card("jack", "hearts")
  
  elif i == 12: #elif = else if
    newcard = Card("queen", "hearts")
  
  elif i == 13: #elif = else if
    newcard = Card("king", "hearts")
  
  else:  
    newcard = Card(i, "hearts") #creating card objects
  
  #newcard.display() #showing card object


for i in range(1, 14):  #for loop, from 1-13
 
  if i == 1: #checking if i = 1 then its an ace
    newcard = Card("ace", "diamonds")
  
  elif i == 11: #elif = else if
    newcard = Card("jack", "diamonds")
  
  elif i == 12: #elif = else if
    newcard = Card("queen", "diamonds")
  
  elif i == 13: #elif = else if
    newcard = Card("king", "diamonds")
  
  else:  
    newcard = Card(i, "diamonds") #creating card objects
  
 # newcard.display() #showing card object
  



for i in range(1, 14):  #for loop, from 1-13
  if i == 1: #checking if i = 1 then its an ace
    newcard = Card("ace", "spades")
  
  elif i == 11: #elif = else if
    newcard = Card("jack", "spades")
  
  elif i == 12: #elif = else if
    newcard = Card("queen", "spades")
  
  elif i == 13: #elif = else if
    newcard = Card("king", "spades")
  
  else:  
    newcard = Card(i, "spades") #creating card objects
  #newcard.display() #showing card object
  

  
for i in range(1, 14):  #for loop, from 1-13

  if i == 1: #checking if i = 1 then its an ace
    newcard = Card("ace", "clubs")
  
  elif i == 11: #elif = else if
    newcard = Card("jack", "clubs")
  
  elif i == 12: #elif = else if
    newcard = Card("queen", "clubs")
  
  elif i == 13: #elif = else if
    newcard = Card("king", "clubs")
  
  else:  
    newcard = Card(i, "clubs") #creating card objects
  
  #newcard.display() #showing card object


########################################################################################
#draw function, this lets us randomly pick a card from deck
###################################################################################
def draw(deck): #draw, pick a random card
   #deck has 52 cards
  drawncard = deck[random.randint(1, 51)] #picking a card from the deck list
      #deck[random number in between 1-51]
     #print(drawncard.suit + str(drawncard.rank)) #printing out drawn card

  drawncard.display() #displays random card
  
  return drawncard #drawncard #returns the random card drawn



########################################################################################
#War game definition
###################################################################################
ourwins = 0 #keeping track of how many times we win in war
computerwins = 0 #how many times computer wins in war
ties = 0 #how many ties happen

#plays game of war, must be passed counters x3
def war(ourwins, compwin, ties): #creating the war definition/game

  print("Your Card: ")
  playerscard = draw(deck) #PICKING RANDOM CARD for player
  
  print("Computer's Card: ")
  computerscard = draw(deck) #picking the computers card
  
  #if player's card rank(2-10, ace, king etc) is equal to the computers card rank
  if playerscard.rank == computerscard.rank: #you tied
    print("Tie")
    ties += 1 #incrementing our tie score
    print(ties)
    
  elif playerscard.rank > computerscard.rank: #you won
    print("You win")
    ourwins += 1 #incrementing our win score
    print(ourwins)
    
  else: #you lost
    print("Computer Won")
    compwin += 1 #incrementing computer win score
    print(compwin)
    
  playerschoice = input("Would you like to play again?") #asking if they want to loop/play again
  if playerschoice == "yes" or playerschoice == "Yes": #if yes then recurse/loop
    war(ourwins, compwin, ties) #calling the def war(), recursive
  else:
    main()
  
#calling draw

#for i in range(1, 14):  #for loop, from 1-13

#  newcard = Card(i, "spades") #creating card objects
#  newcard.display() #showing card object



########################################################################################
#BlackJack definition
###################################################################################
wins = 0
lose = 0
ties = 0

def BlackJack(wins, lose, ties): #deinition for blackjack
  #print("")
  #making our first card
  print("\n" + "Our Card 1: ")
  card1 = draw(deck) #card1
  
  #making our second card
  print("\n" +"Our Card 2: ")
  card2 = draw(deck) #card2
  
  #recursive (loops) for the player to either hit, or stand
  def hitorstand(score):
  
    #they went bust
    if score > 21:
      
      print("You lose!")
      main()
    
    #havent gone bust    
    else:
    #creates score to be added to when dealer draws cards
      
      playersmove = input("Would you like to hit, or stand?") #asking hit or stand
      print(playersmove) #print out their input
      
      if playersmove == "hit": #if they said hit
        newcard = draw(deck) #draw a new card
        
        #checking if a face card (ace, king, etc)      
        if newcard.rank == "ace" or  newcard.rank == "jack" or  newcard.rank== "queen" or newcard.rank== "king":
          newcardvalue = 10
          score += int(newcardvalue)
          
        else:
          newcardvalue = int(newcard.rank)
          score += int(newcardvalue)
        #creates number score
       
        print(str(score))
        hitorstand(score)
      
      elif playersmove == "stand":
        newcardvalue1 = 0
        print("\n" +"Dealer Card 1: ")
        dealercard1 = draw(deck)
      
        print("\n" +"Dealer Card 2: ")
        dealercard2 = draw(deck)
       
        if dealercard1.rank == "ace" or  dealercard1.rank == "jack" or  dealercard1.rank== "queen" or dealercard1.rank== "king":
          newcardvalue1 = 10
          
        else:
          newcardvalue1 = int(dealercard1.rank)
        
        if dealercard2.rank == "ace" or dealercard2.rank == "jack" or  dealercard2.rank== "queen" or dealercard2.rank== "king":
          newcardvalue2 = 10
          
        else:
          newcardvalue2 = dealercard2.rank
        
        dealerscore += int(newcardvalue1)
        dealerscore += int(newcardvalue2)
        print(newcardvalue2)
      
      #dealerscore = 0       
      print(str(dealerscore))
      
      if dealerscore >=17: #IF DEALER IS 17 OR MORE THEY STAND
        print(str(dealerscore))
        print("no new card for dealer")
        
      else:  #DEALER MUST DRAW
            
        print("\n" +"Dealer Card 3: ")
        dealernewcard = draw(deck) #draw a new card
        
        #checking if a face card (ace, king, etc)      
        if dealernewcard.rank == "ace" or dealernewcard.rank == "jack" or  dealernewcard.rank== "queen" or dealernewcard.rank== "king":
          dealernewcardvalue = 10
          
        else:
          dealernewcardvalue = int(dealernewcard.rank)
        
        #creates number score
          dealerscore += int(dealernewcardvalue)
          print(str(dealerscore))
          
          #THIS IS WHERE WE COMPARE SCORES
          
        
  #checks if card is a face (ace, king, queen, jack)
  if card1.rank == "ace" or card1.rank == "jack" or card1.rank == "queen" or card1.rank == "king":
    card1value = 10
  
  #else set card to its number rank (2, 3, 4, ..., 10)
  else:
    card1value = card1.rank
  
  if card2.rank == "ace" or card2.rank == "jack" or card2.rank == "queen" or card2.rank == "king":
    card2value = 10
    
  else:
    card2value = card2.rank
  
  #creates number score
  score = card1value + card2value
  #prints your score
  print("You're score: " + str(score))
  hitorstand(score) #Would you like to hit or stand?
  
 #if score > dealerscore:
#      print("you win!")
 # elif score == dealerscore:
  #  print("tie!")
  #elif score < dealerscore:
   # print("you lose")
  #else:
   # print("error")
  
  
  
def main():
  #asking player what they want to play
  playerinput = input("What game do you want to play? Write War or Blackjack")
  
  #if they say war call war
  if playerinput == "War" or playerinput == "war":
    war(ourwins, computerwins, ties)
  
  #else call blackjack
  elif playerinput == "BlackJack" or playerinput == "blackjack" or playerinput == "Blackjack":
    BlackJack(wins, lose, ties)
    
  else:
    print("try again")
    #recurse main
    main()

#calling main   
main()
#draw(deck)
