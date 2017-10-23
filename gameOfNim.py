# -*- coding: utf-8 -*-

from functools import *

def nimSum (piles):
    # performs the xor operation on numbers in "piles"
    if piles == []:
        return 0
    else:
        return piles[0] ^ nimSum(piles[1:])

def findTopBit(num):
    # returns the deximal conversion of the most significant bit (of a binary string)
    binaryNum = bin(num)
    binaryNum = binaryNum[2:]

    for i in range(len(binaryNum)):
        if binaryNum[i] == "1":
            return pow(2, len(binaryNum) - i - 1)

def computerTakes(piles):
    # brains of the nimSum game, computer player playing its turn
    if nimSum(piles) == 0:
        # returns a list of non-zero indexes
        greaterThanZero = list(filter(lambda x: piles[x] > 0, range(len(piles))))
        return [greaterThanZero[0], 1]
    else:
        pileIndex = list(filter(lambda x: (piles[x] & findTopBit(nimSum(piles))) != 0, range(len(piles))))[0]
        return (pileIndex, piles[pileIndex] - (piles[pileIndex] ^ nimSum(piles)))

def printPiles(coins):
    # prints contents of all coin piles
    print("------------------------")
    for i in range(len(coins)):
        print("Pile " + str(i) + " has " + str(coins[i]) + " coins")
    print("------------------------")

def initialiseGame():
    # function to run at beginning of game to set number of piles and number of coins in each pile
    correctInput = True
    coinsArray = []
    print()
    print("Welcome to Nim! I'm probably going to win...")

    # input for number of piles
    while (correctInput):
        print()
        print("How many piles would you like?")
        piles = input()
        try:
            piles = int(piles)
            assert(piles > 0) 
            break
        except (ValueError, AssertionError):
            print()
            print("oops! try again, inputs must be > 0")
            continue

    numCoinsCounter = piles # to iteratre through piles and input coins
    
    # input for number of coins in each piles
    while (numCoinsCounter > 0):
        print()
        print("How many coins in pile " + str(piles - numCoinsCounter) + " ?")
        numCoins = input()
        try:
            numCoins = int(numCoins)
            assert(numCoins > 0)
            coinsArray.append(numCoins)
            numCoinsCounter -= 1
        except (ValueError, AssertionError):
            print()
            print("oops! try again, input must be > 0")
            continue
        print(coinsArray)

    return [piles, coinsArray]

def userTurn(numberOfPiles, coinsArray):
    # function for all user interactions in game
    playing = True
    correctInput = True
    while (playing):
        # user turn for selecting which pile to take from
        print()
        print("Which pile would you like to remove from?")
        userPileChoice = input()
        try:
            userPileChoice = int(userPileChoice)
            assert(userPileChoice < numberOfPiles and userPileChoice > 0 )
        except (ValueError, AssertionError):
            print()
            print("oops! try again, input must be from 0 to "  + str(numberOfPiles - 1))
            continue
        break

    while (playing):
        # user turn for selecting how many coins to remove
        print()
        print("How many coins do you wish to remove from pile " + str(userPileChoice) + " ?")
        userCoinChoice = input()
        try:
            userCoinChoice = int(userCoinChoice)
            assert(userCoinChoice <= coinsArray[userPileChoice] and userCoinChoice > 0)
        except (ValueError, AssertionError):
            print()
            print("oops! try again, input must be from 1 to "  + str(coinsArray[userPileChoice]))
            continue
        break
    
    coinsArray[userPileChoice] = coinsArray[userPileChoice] - userCoinChoice # update piles
    printPiles(coinsArray) # print updated piles
    return coinsArray
    

def computerTurn(numberOfPiles, coinsArray):
    # function for all computer interactions in game
    computerChoice = computerTakes(coinsArray) # returns a tuple (pileIndex, numCoins)
    print(computerChoice)
    coinsArray[computerChoice[0]] = coinsArray[computerChoice[0]] - computerChoice[1] 
    print()
    print("I remove " + str(computerChoice[1]) +  " coins " + "from pile " + str(computerChoice[0]))
    printPiles(coinsArray)
    return coinsArray

def gameCont(coinsArray):
    # funciton for checking if computer has won and asking user to continue game or not
    playing = True
    cont = ""

    while (playing):
        print("Would you like to play again? y / n")
        cont = input()
        try:
            assert(cont == "y" or cont == "n") 
            break
        except (ValueError, AssertionError):
            print("oops! try again, input must be y / n")
            continue

    return cont

def main():
    # the game of nim!
    playAgain = True # for outside while-loop 
    correctInput = True

    while (playAgain):
        # retrieves number of piles and coins in each pile 
        [numPiles, coins] = initialiseGame()

        playing = True # for inside while-loop that continues taking turns in game
        
        while (playing):
            # gameplay
            coins = computerTurn(numPiles, coins)
            if (all(x == 0 for x in coins)): # checks if all coin piles are == 0
                print()
                print("I win!")
                # asking user to continue or not
                if (gameCont(coins) == "n"):
                    print("Thanks for playing!")
                    playing = False
                    playAgain = False
                    break
                else: 
                    break
            coins = userTurn(numPiles, coins)
            if (all(x == 0 for x in coins)): # checks if all coin piles are == 0
                print()
                print("Congrats! You won!")
                break
                # asking user to continue or not
                if (gameCont(coins) == "n"):
                    print("Thanks for playing!")
                    playing = False
                    playAgain = False
                    break
                else:
                    break

    print("ye bro it work")

main()

# run gameOfNim