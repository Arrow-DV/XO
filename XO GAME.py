# Import Needed Libary's
import os
# Variables First
counter,i,turn = 0,0,""
rows = [
    "-","-","-",
    "-","-","-",
    "-","-","-"
]
# Functions
def game_over():
    winning_conditions = [
        # Rows
        [rows[0], rows[1], rows[2]],
        [rows[3], rows[4], rows[5]],
        [rows[6], rows[7], rows[8]],
        # Columns
        [rows[0], rows[3], rows[6]],
        [rows[1], rows[4], rows[7]],
        [rows[2], rows[5], rows[8]],
        # Diagonals
        [rows[0], rows[4], rows[8]],
        [rows[2], rows[4], rows[6]]
    ]

    for condition in winning_conditions:
        if condition[0] != "-" and all(cell == condition[0] for cell in condition):
            return True  # Game is over, a player has won

    if "-" not in rows:
        return "draw"  # Game is over, it's a draw

    return False  # Game is not over yet
    
def flush(): # Flush Old Table
    os.system("cls")
def table(): # Display XO TABLE
    global rows ,counter
    for row in rows:
        print("\t" + row,end= " ")
        counter += 1
        if counter % 3 == 0 : print() ; counter = 0
def play():  # Choose Turn
    flush()
    table()
    global i,turn,rows
    if i == 0 :
        turn = "X"
        i += 1
    else :
        turn = "O"
        i -= 1
    print()
    try:
        move =  int(input(f"Play Row 0-9 Turn: {turn} : ")) # Play in The Table
    except:
        print("Wrong Input")
    if move != None:
        if "-" in rows[move] :
            try:
                rows[move] = turn
            except ValueError:
                print("WRONG CHOOSE!")
            except:
                print("Something Wen't Wrong")
# Start Game

while True:
    if game_over() == "draw":
        print("TIE")
        break
    elif game_over() == True:
        print(f"{turn} WON!")
        break
    else:
        play()