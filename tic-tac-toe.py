# imports
import random
from terminaltables import AsciiTable

# constants
X = "X"
O = "O"
HUMAN = "human"
COMPUTER = "computer"
BLANK_CELL = ' - '

VALID_SYMBOLS = [X, O]
VALID_PLAYERS = [HUMAN, COMPUTER]
GAME_BOARD = [
    ['ಥ_ಥ', ' A ', ' B ', ' C '],
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

def printBoard(board):
    table = AsciiTable(board)
    print(table.table)

def startGame():
    introduction()
    pickSymbol()

def isSymbolValid(rawUserInputSymbol):
    return rawUserInputSymbol in VALID_SYMBOLS

def isInputValidMove(userInput):
    return userInput in VALID_MOVES

def isSpaceAvailable(move, activeGameBoard):
    spaceIndex = GAME_BOARD_INDEX[move]
    targetSpace = activeGameBoard[spaceIndex[0]][spaceIndex[1]]

    return targetSpace == BLANK_CELL

def writeMoveToBoard(move, activeGameBoard, symbol):
    spaceIndex = GAME_BOARD_INDEX[move]
    activeGameBoard[spaceIndex[0]][spaceIndex [1]] = " " + symbol + " "

# Pick a symbol
def pickSymbol():
    rawInputSymbol = ""
    validInputSymbol = ""
    computerSymbol = ""
    isSymbolValidBool = False
    symbolAssignmentHash = {}

    gameMessage("Pick a symbol: X or O")
    rawInputSymbol = input().upper()
    isSymbolValidBool = isSymbolValid(rawInputSymbol)

    while isSymbolValidBool == False:
        gameMessage("Must be X or O")
        #improvement, allow user to choose symbols
        rawInputSymbol = input().upper()
        isSymbolValidBool = isSymbolValid(rawInputSymbol)
    
    validInputSymbol = rawInputSymbol
    computerSymbol = VALID_SYMBOLS[VALID_SYMBOLS.index(validInputSymbol) - 1]
    symbolAssignmentHash = {HUMAN: validInputSymbol, COMPUTER: computerSymbol}

    gameMessage("You chose " + validInputSymbol + "!")
    gameMessage("Computer will play as " + computerSymbol + "!")

    pickFirstTurn(symbolAssignmentHash)

def pickFirstTurn(symbolAssignmentHash):
    firstTurnIndex = random.randint(0,1)
    firstTurn = VALID_PLAYERS[firstTurnIndex]

    if firstTurn == HUMAN:
        gameMessage("You will go first!")
    else:
        gameMessage(VALID_PLAYERS[firstTurnIndex].capitalize() + " will go first!")

    gamePlay(firstTurnIndex, symbolAssignmentHash)


def getHumanMove(activeGameBoard):
    isSpaceAvailableBool = False
    isInputValidBool = False
    moveConfirmed = False
    validInputMove = ""
    rawInputMove = ""

    # First input attempt
    rawInputMove = input().upper()
    
    # Is the input a valid move and is space available?
    # abstract this into a new function validateMove() with sanitizeInput and isSpaceTaken?
    while (moveConfirmed == False):
        isInputValidBool = isInputValidMove(rawInputMove)
        
        if isInputValidBool == True:
            validInputMove = rawInputMove
            isSpaceAvailableBool = isSpaceAvailable(validInputMove, activeGameBoard)

            if isSpaceAvailableBool == True:
                moveConfirmed = True
            
            else:
                gameMessage("That space is already taken.")
                rawInputMove = input().upper()
        else:
            gameMessage("Invalid move. Try A1, C3...")
            rawInputMove = input().upper()
    
    return validInputMove



def getComputerMove(activeGameBoard):
    print("Getting Computer Move")
    # select random space
    # isSpaceAvailable
    # while is Space Available == false
        # new random space
        # check if available
    
    #available space assigned
    # return available space





def gamePlay(firstTurnIndex, symbolAssignmentHash):
    activeGameBoard = GAME_BOARD.copy()
    currentTurnIndex = firstTurnIndex
    gameOver = False
    userMove = ""

    while gameOver == False:
                   
        if VALID_PLAYERS[currentTurnIndex] == HUMAN:
            gameMessage("Your move!")
            userMove = getHumanMove(activeGameBoard.copy())
            writeMoveToBoard( userMove, activeGameBoard, symbolAssignmentHash[HUMAN] )
           
            # if checkForWin(activeGameBoard)
                # You won! gameover=True
            # elsif checkForTie(activeGameBoard)
                # Game is a tie. gameOver=true
            # else
                # next turn
            currentTurnIndex = 0 if currentTurnIndex == 1 else 1
            printBoard(activeGameBoard)
            
        if VALID_PLAYERS[currentTurnIndex] == COMPUTER:
            gameMessage("Computer Move")
            # getComputerMove
             # writeMoveToBoard(getComputerMove(), activeGameBoard)
            # if checkForWin(activeGameBoard)
                # You won! gameover=True
            # elsif checkForTie(activeGameBoard)
                # Game is a tie. gameOver=true
            # else
                # next turn
            
            currentTurnIndex = 0 if currentTurnIndex == 1 else 1



startGame()
