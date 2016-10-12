#imports
import sys
import time

running = True

tr = ["7", "8", "9"]
mr = ["4", "5", "6"]         #board outfit with the "shortkeys"
br = ["1", "2", "3"]

def grid():
    print(str(tr) + "\n" + str(mr) + "\n" + str(br) )           #print outfit

def end_game(): #if somebody win
    choice = input("New Game? (y/n): ")
    if choice == "y":
        running()
        win()
    elif choice == "n":
        sys.exit()

def win():
    try:
        #player1
        #raws
        if tr[0] == "X" and tr[1] == "X" and tr[2] == "X":
            print("Playe_1 wins")
            sleep(5)
            end_game()
        if mr[0] == "X" and mr[1] == "X" and mr[2] == "X":
            print("Playe_1 wins")
            sleep(5)
            end_game()
        if br[0] == "X" and br[1] == "X" and br[2] == "X":
            print("Playe_1 wins")
            end_game()
        #corners
        if tr[0] == "X" and mr[1] == "X" and br[2] == "X":
            print("Playe_1 wins")
            end_game()
        if tr[2] == "X" and mr[1] == "X" and br[0] == "X":
            print("Playe_1 wins")
            end_game()
        #columns
        if tr[0] == "X" and mr[0] == "X" and br[0] == "X":
            print("Playe_1 wins")
            end_game()
        if tr[1] == "X" and mr[1] == "X" and br[1] == "X":
            print("Playe_1 wins")
            end_game()
        if tr[2] == "X" and mr[2] == "X" and br[2] == "X":
            print("Playe_1 wins")
            end_game()
        #player2
        #row
        if tr[0] == "O" and tr[1] == "O" and tr[2] == "O":
            print("Playe_2 wins")
            end_game()
        if mr[0]  == "O" and mr[1] == "O" and mr[2] == "O":
            print("Playe_2 wins")
            end_game()
        if br[0] == "O" and br[1] == "O" and br[2] == "O":
            print("Playe_2 wins")
            end_game()         
        #corners
        if tr[0] == "O" and mr[1] == "O" and br[2] == "O":
            print("Playe_2 wins")
            end_game()
        if tr[2] == "O" and mr[1] == "O" and br[0] == "O":
            print("Playe_2 wins")
            end_game()
        #columns
        if tr[0] == "O" and mr[0] == "O" and br[0] == "O":
            print("Playe_2 wins")
            end_game()
        if tr[1] == "O" and mr[1] == "O" and br[1] == "O":
            print("Playe_2 wins")   
            end_game()
        if tr[2] == "O" and mr[2] == "O" and br[2] == "O":
            print("Playe_2 wins")
            end_game()


    except:
        pass

#code
while running:
    grid() 
    win()

#palyer_1
    print(" ")
    player_1 = input("p1: ")
    print("")
    #top
    if player_1 == "7":
        tr[0] = "X"
    if player_1 == "8":
        tr[1] = "X"
    if player_1 == "9":
        tr[2] = "X"
    #middle
    if player_1 == "4":
        mr[0] = "X"
    if player_1 == "5":
        mr[1] = "X"
    if player_1 == "6":
        mr[2] = "X"
    #bottom 
    if player_1 == "1":
        br[0] = "X"
    if player_1 == "2":
        br[1] = "X"
    if player_1 == "3":
        br[2] = "X"

    grid() #grid_2
    win()

  #player_2
    print(" ")
    player_2 = input("p2: ")
    print(" ")
    #top
    if player_2 == "7":
        tr[0] = "O"
    if player_2 == "8":
        tr[1] = "O"
    if player_2 == "9":
        tr[2] = "O"
    #middle
    if player_2 == "4":
        mr[0] = "O"
    if player_2 == "5":
        mr[1] = "O"
    if player_2 == "6":
        mr[2] = "O"
    #bottom 
    if player_2 == "1":
        br[0] = "O"
    if player_2 == "2":
        br[1] = "O"
    if player_2 == "3":
        br[2] = "O"

