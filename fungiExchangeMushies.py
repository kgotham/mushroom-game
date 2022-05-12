#Ksusha Gotham 
#Fungi game code
#Summary-Explorer finds a mysterious list of msuhroom ingredients , curious of what they are for, starts collecting. It is revealed the list was lost by a soup chef making a very important soup for the queen. Soup chef Anders offers you rubies for the ingredients. 

def main():

#Creating the narrative
    playerName = input("What is your character's name? ")
    print(playerName,"explores Witchblood Woods in hopes of finding an exciting new adventure.")
    print("After just a few minutes of looking around,", playerName, "finds a list of what seem to be ingredients.")
    
    questOffer = input("Hmm... I am kind of hungry.. should I try to find everything on this list? (Enter y/n) ")
    if questOffer == "y":
        print("Let's see, hen of the woods and portobello mushrooms, I'm sure there are some around here.")
    elif questOffer == "n":
        print("Nahhh, I'd rather go to the tavern, maybe next time.")
        exit()
    else:
        print("Invalid input, try again.")
        main()

#if player accepts the quest they collect mushrooms. for story location accuracy purposes shiitake = maitake(hen of the woods)
    cont1 = input("Press enter to continue...")
    print("After an hour of searching " + playerName, "rounds up their fungi findings..")
    numHen = int(input("How many hen of the woods did you find? "))
    numPorto = int(input("How many portobello mushrooms did you find? "))

    #soup chef encounter
    print('From the distance you hear a human voice calling out to you, "Heyyy...Hey, you!".')
    #easter egg
    if playerName == "The Queen":
        print('"Oh."')
        exit()
    cont2 = input("Press enter to continue...")
    print("The winded person catches up to you and says,",  end = ' ')
    print('"Hello, my friend. I see you have found my list. My name is Anders - personal soup chef of the Queen. I was foraging for mushrooms when a pack of wolves chased me away. The Queen wants her mushroom soup and I am desperate."')
    
    tradeOffer = input('"Will you sell me the mushrooms you found?" (y/n) ')
    if tradeOffer == "y":
        print('"Yes, I will", says' ,playerName)
    elif tradeOffer == "n":
        print("No, I am selfish and I hate you, stinky soup chef *" + playerName, "runs away with", numHen, "hen of the woods and", numPorto, "portobello mushrooms*")
        exit()
    else:
        print("Invalid input, try again.")
        main()


#defining the chef's exchange rate
    numHenTrade = int(input("How many hen of the woods would you like to trade? "))
    numPortoTrade = int(input("And how many portobello mushrooms? "))

    if numHenTrade > numHen or numPortoTrade > numPorto:
        print("You can't trick me. *robs you*")
        exit()
    elif numHenTrade + numPortoTrade <=0:
        print('Anders says, "I do not deal with imaginary mushrooms."*walks away*')
        exit()
    elif numHenTrade < 10 and numPortoTrade < 5:
        print('Anders says, "I will give you', 2*numHenTrade, 'rubies."')
        numRubies = 2*numHenTrade 
    elif numHenTrade < 10 and numPortoTrade >= 5:
        print('Anders says, "I will give you', 3*numPortoTrade, 'rubies."')
        numRubies = 3*numPortoTrade
    elif numHenTrade % 12 == 0 and numHenTrade % 24 != 0 and numPortoTrade >= 20:
        print('Anders says, "I will give you', 4*numPortoTrade, 'rubies."')
        numRubies =  4*numPortoTrade
    elif numHenTrade % 12 == 0 and numHenTrade % 24 != 0 and numPortoTrade < 20:
        print('Anders says, "I will give you', numPortoTrade, 'rubies."')
        numRubies = numPortoTrade
    else:
        print('Anders says, "I will give you', 5 * numHen, 'rubies."')
        numRubies = 5 * numHen
        
#conclusion of trade
    tradeAccept = input("Do you accept the trade? (y/n) ")

    if tradeAccept == "y":
        print('"Thank you so much my friend." *'+ playerName, "walks away with", numRubies, "rubies as well as", numHen - numHenTrade, "hen of the woods and", numPorto - numPortoTrade, "portobello mushrooms*.")
    elif tradeAccept == "n":
        print("You are really a terrible person and should think about your actions. *"+playerName,"walks away with", numHen, "hen of the woods,", numPorto, "portobello mushrooms, and a guilty consience*.")
    else:
        print("Invalid input, try again.")
        main()
        
#restart option  
    restart = input("Do you want to play again? (y/n) ")
                    
    if restart == "y":
        main()
    else:
        print("Thanks for playing!")
        exit()
        
#code starts here 
main()





