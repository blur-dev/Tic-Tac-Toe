board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def displayBoard():
  bi = 0
  for i in range(3):
    print(board[bi] + " |" + board[bi+1] + " |" + board[bi+2])
    if i != 2:
      print("--+--+--\n")
    bi += 3 


def checkPositionRange(position):
  if position > 8 or position < 0:
    return False
  return True

def checkIfAlreadyPlaced(position):
  if board[position] == "X" or board[position] == "O":
    return False
  return True
  

#2c algorithm oval
def place(position, currentPlayer):
  #position is the index for the board array
  #board[poisition] is the specific element in the array

  #algorithm 1
  if checkPositionRange(position) == False:
    return "Out of Bounds"

  #algorithm 2
  if checkIfAlreadyPlaced(position) == False:
    return "Try Again!"

  #some more code
  if currentPlayer == 1:
    board[position] = "X"
  else:
    board[position] = "O"


  
#will return true if someone won  
#will return false if no one won 

def checkIfWon(position):
  if position == 0:
    if board[0] == board[1] and  board[1] == board[2]:
      return True 
    elif board[0] == board[4] and board[4] == board[8]:
      return True
    elif board[0] == board[3] and board[3] == board[6]:
      return True
  if position == 1:
    if board[1] == board[0] and board[0] == board[2]:
      return True
    elif board[1] == board[4] and board[4] == board[7]:
      return True
  if position == 2:
    if board[2] == board[5] and board[5] == board[8]:
      return True
    elif board[2] == board[1] and board[1] == board[0]:
      return True
    elif board[2]== board[4] and board[4] == board[6]:
      return True
  if position == 3:
    if board[3] == board[4] and board[4] == board[5]:
      return True
    elif board[3] == board[0] and board[0] == board[6]:
      return True
  if position == 4:
    if board[4] == board[0] and board[0] == board[8]:
      return True
    elif board[4] == board[2] and board[2] == board[6]:
      return True
    elif board[4] == board[1] and board[1] == board[7]:
      return True
    elif board [4] == board[3] and board[3] == board[5]:
      return True
  if position == 5:
    if board[5] == board[2] and board [2] == board[8]:
      return True
    elif board[5] == board[4] and board[4] == board[3]:
      return True
  if position == 6:
    if board[6] == board[3] and board[3] == board[0]:
      return True 
    elif board[6] == board[7] and board[7] == board[8]:
      return True
    elif board[6] == board[4] and board[4] == board[2]:
      return True
  if position == 7:
    if board[7] == board[6] and board[6] == board[8]:
      return True
    elif board[7] == board[1] and board[1] == board[4]:
      return True
  if position == 8:
    if board[8] == board[6] and board[6] == board[7]:
      return True
    elif board[8] == board[2] and board[2] == board[5]:
      return True
    elif board[8]== board[4] and board[4] == board[0]:
      return True

def startGame():
  currentPlayer = 1
  position = 1
  count = 1
  print("Welcome to Tic Tac Toe!")
  print("Instructions:  The Order being 0, 1, 2 from left to right all the way to 8")
  while 1:
    displayBoard()
    print("Go player " + str(currentPlayer))
    position = int(input("Where do you want to go? "))

    val = place(position, currentPlayer)
    if val == "Out of Bounds":
      print("Pick A Number 1-8, Try Again!")
      continue
    elif val == "Try Again":
      continue

    w = checkIfWon(position)
    if w == True:
      print("You won! Play Again!")
      displayBoard()
      break

    count+=1
    if count % 2 == 0:
      currentPlayer = 2
    else:
      currentPlayer = 1
  #end of the functin
      
startGame()