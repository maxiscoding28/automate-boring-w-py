# imports
import random
from terminaltables import AsciiTable

# constants
X = "X"
O = "O"
VALID_SYMBOLS = [X, O]
HUMAN = "human"
COMPUTER = "computer"
VALID_PLAYERS = [HUMAN, COMPUTER]
GAME_BOARD = [
    ['   ', ' A ', ' B ', ' C '],
    [' 1 ', ' - ', ' - ', ' - '],
    [' 2 ', ' - ', ' - ', ' - '],
    [' 3 ', ' - ', ' - ', ' - ']
]
GAME_BOARD_INDEX = {
    "A1" : [1,1],
    "A2" : [2,1],
    "A3" : [3,1],
    "B1" : [1,2],
    "B2" : [2,2],
    "B3" : [3,2],
    "C1" : [1,3],
    "C2" : [2,3],
    "C3" : [3,3]
}
VALID_MOVES = list(GAME_BOARD_INDEX.keys())

# print the intro message to console
def introduction():
    print("\n")
    print("==========================================")
    print("~~~~~~~~~ Welcome To Tic Tac Toe ~~~~~~~~~")
    print("==========================================")
    print("\n") 

# send a pre-formatted message with game information
def gameMessage(message):
    print(str("=" * len(message)))
    print(message)
    print(str("=" * len(message)))

def startGame():
    introduction()
    pickSymbol()

# Pick a symbol
def pickSymbol():
    userInputSymbol = ""
    computerSymbol = ""

    gameMessage("Pick a symbol: X or O")
    userInputSymbol = input().upper()
    
    while userInputSymbol not in VALID_SYMBOLS:
        gameMessage("Must be X or O")
        #improvement, allow user to choose symbols
        userInputSymbol = input().upper()
    

    computerSymbol = VALID_SYMBOLS[VALID_SYMBOLS.index(userInputSymbol) - 1]

    symbolAssignmentHash = {HUMAN: userInputSymbol, COMPUTER: computerSymbol}

    gameMessage("You chose " + userInputSymbol + "!")
    gameMessage("Computer will play as " + computerSymbol + "!")

    pickFirstTurn(symbolAssignmentHash)

def pickFirstTurn(symbolAssignmentHash):
    firstTurnIndex = random.randint(0,1)
    firstTurn = VALID_PLAYERS[firstTurnIndex]

    if firstTurn == HUMAN:
        gameMessage("You will go first!")
    else:
        gameMessage(VALID_PLAYERS[firstTurnIndex].capitalize() + " will go first!")
    

    gamePlay(firstTurnIndex)

def isInputValidMove(userInput):
    return userInput in VALID_MOVES

def isSpaceAvailable(move):
    print("ayo")

def getHumanMove(activeGameBoard):
    isInputValidBool = False
    isSpaceAvailableBool = False
    gameMessage("Make a move!")
    rawInputMove = input().upper()
    validInputMove = ""
    
    
    # Is the input a valid move?
    while isInputValidBool == False:
        isInputValidBool = isInputValidMove(rawInputMove)

        if isInputValidBool == True:
                 # Is the space available
                #  while isSpaceAvailableBool = False
                    # isSpaceAvailableBool = isSpaceAvailable(activeGameBoard, validInputMove)

                # if isSpaceAvailableBool == True
                    # break
        
                # else
                    # "Space Must be available"
            
            validInputMove = rawInputMove
            break
        
        else:
            gameMessage("Not a valid move. E.X A1, C33")
            rawInputMove = input().upper()
    
    return validInputMove


def getComputerMove():
    print("Getting Computer Move")
    # whatSpacesAreAvailable()
    # select random space

def writeMoveToBoard(move, gameBoard):
    print(move, gameBoard)
    [print(GAME_BOARD)]

   
    # assign move to gameBoard
    # checkForWin()
    # checkForTie()
    # printGameBoard(win=false, tie=true)
    print("ay")


def gamePlay(firstTurnIndex):
    activeGameBoard = GAME_BOARD.copy()
    currentTurnIndex = firstTurnIndex
    gameOver = False
    
    while gameOver == False:
        print()
        print(VALID_PLAYERS[currentTurnIndex].capitalize() + " makes a move")
        
        if VALID_PLAYERS[currentTurnIndex] == HUMAN:
            getHumanMove(activeGameBoard)
        
        if VALID_PLAYERS[currentTurnIndex] == COMPUTER:
            print("Computer Move")
            # writeMoveToBoard(getComputerMove(), activeGameBoard)
       
        # added just to prevent infinite loop. gameOver needs to eventually be set true
        x = input()
        currentTurnIndex = 0 if currentTurnIndex == 1 else 1

        #breakdown of a move.
        ## HUMAN
        # Is it valid move input? (A1, C3 etc...)
            # If not, ask for input again
        # Is the space available?
            # if not, ask for another input, re-validate valid input, check for space again
        # If yes and yes
            #assign to board, check if win or all spaces full?
            # print board to console
        
        ## COMPUTER
            # What spaces are available?
            # Randomly assign to available space (can refine this later)
            # check if win or all spaces full?
            # Print board to console
        
        #IF win
            # print winner message
        #If full
            # print tie message
        # Ask if want to play again




startGame()
