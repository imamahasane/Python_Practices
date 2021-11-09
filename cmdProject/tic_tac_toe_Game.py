
bdList = ["-", "-", "-",
           "-", "-", "-",
           "-", "-", "-",]

def show_box():
    print(bdList[0] +" | "+ bdList[1] +" | "+ bdList[2])
    print(bdList[3] +" | "+ bdList[4] +" | "+ bdList[5])
    print(bdList[6] +" | "+ bdList[7] +" | "+ bdList[8])
       
      
def position(player):
    userInput = input("Choose a position (1 to 9): ")
    
    if userInput not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        userInput = input("Wrong Input Please Try Agin (1 to 9): ")
    
    userInput = int(userInput) - 1
    
    bdList[userInput] = player
    show_box()
    

def over_the_game():
    win_the_game()
    tie_the_game()

winner = None    

def win_the_game():
    global winner
    
    winTheRow = row()
    winTheColumns = columns()
    winTheDiagonal = diagonal()
    
    if winTheRow:
        winner = winTheRow
        
    elif winTheColumns:
        winner = winTheColumns
       
    elif winTheDiagonal:
        winner = winTheDiagonal
           
    else:
        winner = None
        
    return 

continueTheGame = True

def row():
    global continueTheGame
    
    r1 = bdList[0] == bdList[1] == bdList[2] != "-"
    r2 = bdList[3] == bdList[4] == bdList[5] != "-"
    r3 = bdList[6] == bdList[7] == bdList[8] != "-"
    
    if r1 or r2 or r3:
        continueTheGame = False
        
    if r1:
        return bdList[0]
    
    if r2:
        return bdList[3]
    
    if r3:
        return bdList[6]
    
    return

def columns():
    global continueTheGame
    
    c1 = bdList[0] == bdList[3] == bdList[6] != "-"
    c2 = bdList[1] == bdList[4] == bdList[7] != "-"
    c3 = bdList[2] == bdList[5] == bdList[8] != "-"
    
    if c1 or c2 or c3:
        continueTheGame = False
        
    if c1:
        return bdList[0]
    
    if c2:
        return bdList[1]
    
    if c3:
        return bdList[2]
    
    return

def diagonal():
    global continueTheGame
    
    d1 = bdList[0] == bdList[4] == bdList[8] != "-"
    d2 = bdList[6] == bdList[4] == bdList[2] != "-"
    
    if d1 or d2:
        continueTheGame = False
        
    if d1:
        return bdList[0]
    
    if d2:
        return bdList[6]

    return


def tie_the_game():
    global continueTheGame
    
    if "-" not in bdList:
        continueTheGame = False
    
    return

currentPlayer = "X"

def lap_player():
    global currentPlayer
    
    if currentPlayer == "X":
        currentPlayer = "O"
    elif currentPlayer == "O":
        currentPlayer = "X"
    
    return
  

def main():
    show_box()
    
    while continueTheGame:    
        position(currentPlayer)
        
        over_the_game()
                
        lap_player()
        
    if winner == "X" or winner == "O":
        print(winner, "win the game.")
        
    elif winner == None:
        print("Tie the game.")
    
main()
    