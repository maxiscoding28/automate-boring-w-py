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
    [' 1 ', ' X ', ' - ', ' - '],
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

WIN_COMBINATIONS = [
    ["A1", "B1", "C1"],
    ["A2", "B2", "C2"],
    ["A3", "B3", "C3"],
    ["A1", "A2", "A3"],
    ["B1", "B2", "B3"],
    ["C1", "C2", "C3"],
    ["A1", "B2", "C3"],
    ["A3", "B2", "C1"],
]

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

def checkForWin(movesList):
    print(movesList, "checking for win")
   # A1 in potential wins in movesList
        # yes check next value
        # no next potential wins list

def checkForTie(activeGameBoard):
    print(activeGameBoard, "checking for tie")
    # are all spaces filled (assumes no winner has already returned false)
    # loop through values in GAMEBOARD index and check if cell is empty. If all false, return True for tie

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
    isSpaceAvailableBool = False
    randomIndex = 0
    randomMove = ""

    # select random space
    randomIndex = random.randint(0, 8)
    randomMove = VALID_MOVES[randomIndex]
    isSpaceAvailableBool = isSpaceAvailable(randomMove, activeGameBoard)

    while isSpaceAvailableBool == False:
        randomIndex = random.randint(0, 8)
        randomMove = VALID_MOVES[randomIndex]
        isSpaceAvailableBool = isSpaceAvailable(randomMove, activeGameBoard)
    
    return randomMove

def gamePlay(firstTurnIndex, symbolAssignmentHash):
    activeGameBoard = GAME_BOARD.copy()
    currentTurnIndex = firstTurnIndex
    userMovesList = []
    computerMovesList = []
    gameOver = False
    userMove = ""
    computerMove = ""

    while gameOver == False:
                   
        if VALID_PLAYERS[currentTurnIndex] == HUMAN:
            gameMessage("Your move!")
            userMove = getHumanMove(activeGameBoard.copy())
            userMovesList.append(userMove)

            if checkForWin(userMovesList) == True:
                gameMessage("You Won")
                gameOver == True
            elif checkForTie(activeGameBoard) == True:
                gameMessage("It's a tie!")
                gameOver == True
            else:
                currentTurnIndex = 0 if currentTurnIndex == 1 else 1
            
            writeMoveToBoard( userMove, activeGameBoard, symbolAssignmentHash[HUMAN] )
            printBoard(activeGameBoard)
            
        if VALID_PLAYERS[currentTurnIndex] == COMPUTER:
            gameMessage("Computer Move")
            computerMove = getComputerMove(activeGameBoard.copy())
            computerMovesList.append(computerMove)
            print(computerMove)
            
            if checkForWin(computerMovesList) == True:
                gameMessage("Computer Won")
                gameOver == True
            elif checkForTie(activeGameBoard) == True:
                gameMessage("It's a tie!")
                gameOver == True
            else:
                currentTurnIndex = 0 if currentTurnIndex == 1 else 1
                
            writeMoveToBoard(computerMove, activeGameBoard, symbolAssignmentHash[COMPUTER])
            printBoard(activeGameBoard)
            
            



startGame()
