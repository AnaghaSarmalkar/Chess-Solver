import re

occupied_loc = []           #A list which maintains all the pieces on the board
game = 0
piece_list = ['pawn', 'rook', 'queen', 'bishop', 'knight', 'king']

print("The chess board in the program is assumed to be named as follows:")
print("All the 8 rows are named using numbers [1-8]")
print("All the columns are named using alphabets [a-h]")
print("The positions of row 1 are 1a, 1b, 1c, 1d, 1e, 1f, 1g, 1h")
print("The positions of row 2 are 2a, 2b, 2c, 2d, 2e, 2f, 2g, 2h")
print("The positions of row 3 are 3a, 3b, 3c, 3d, 3e, 3f, 3g, 3h")
print("The positions of row 4 are 4a, 4b, 4c, 4d, 4e, 4f, 4g, 4h")
print("The positions of row 5 are 5a, 5b, 5c, 5d, 5e, 5f, 5g, 5h")
print("The positions of row 6 are 6a, 6b, 6c, 6d, 6e, 6f, 6g, 6h")
print("The positions of row 7 are 7a, 7b, 7c, 7d, 7e, 7f, 7g, 7h")
print("The positions of row 8 are 8a, 8b, 8c, 8d, 8e, 8f, 8g, 8h")
print("The available pieces are: ", piece_list, "\n")

#The Chess game loop
while game ==0 :
    inputstatus = 0
    game = 0
    selection = []
    possible_loc = []
    ans = 0
    choice = 0
    status = 0
    piece = ''
    loc = ''

    #Loop for getting input from user
    while inputstatus == 0:
        format_loc = 0
        piece = str(input("Enter the piece name:\n"))
        piece = piece.lower()
        while format_loc == 0:
            #Input location being taken as string
            loc=str(input("Enter the current location of the piece (eg. 1a, 2b, 2c, etc):\n"))
            loc=loc.lower()
            if len(loc) > 2 or len(loc) < 2:
                print("Incorrect location format of piece. Please enter location in correct format like 1a, 2a, 3a")
                format_loc = 0
            else:
                try:
                    loc = re.findall(r"[^\W\d_]|\d", loc)
                    loc = [int(loc[0]), ord(loc[1])]
                    format_loc = 1
                except ValueError:
                    print("Incorrect location format of piece. Please enter location in correct format like 1a, 2a, 3a")

        #Checking if correct input of row 1 to 8 and column a to h and piece name is being received.
        if 0 < loc[0] < 9 and 96 < loc[1] < 105 and piece in piece_list:

            #Checking if the input location is already occupied by some other piece
            if [loc[0], chr(loc[1])] not in occupied_loc:
                inputstatus = 1

            else:
                print("This location already contains a piece.")
                inputstatus = 0

        else:
            print("Either piece name or its current location is incorrect. Please enter again.")
            inputstatus = 0

    if piece == "pawn":

        if loc[0] == 1:
            print("Pawn cannot be in the first row.")

        elif loc[0] == 2:

            for i in range(1, 3):
                if loc[0] + i < 5:  # vertical down movement 1 and 2 places for 2nd row
                    a = loc[0] + i
                    if [a, chr(loc[1])] not in occupied_loc:
                        possible_loc.append([a, chr(loc[1])])
                    else:
                        break

        elif loc[0] > 2:
            if loc[0] + 1 < 9:      # vertical down movement 1 place for rows after 2
                a = loc[0] + 1
                if [a, chr(loc[1])] not in occupied_loc:
                    possible_loc.append([a, chr(loc[1])])

        if loc[0] != 1:
            if loc[0] + 1 < 9 and loc[1] + 1 < 105:                     # right diagonal down movement
                if [loc[0] + 1, chr(loc[1] + 1)] not in occupied_loc:
                    possible_loc.append([loc[0] + 1, chr(loc[1] + 1)])

            if loc[0] + 1 < 9 and loc[1] - 1 > 96:                      # left diagonal down movement
                if [loc[0] + 1, chr(loc[1] - 1)] not in occupied_loc:
                    possible_loc.append([loc[0] + 1, chr(loc[1] - 1)])

    elif piece == "rook":

        for i in range(1, 8):           # vertical down movement
            a = loc[0] + i
            if a < 9:
                if [a, chr(loc[1])] in occupied_loc:
                    break
                else:
                    possible_loc.append([a, chr(loc[1])])

        for i in range(1, 8):           # vertical up movement
            a = loc[0] - i
            if a > 0:
                if [a, chr(loc[1])] in occupied_loc:
                    break
                else:
                    possible_loc.append([a, chr(loc[1])])

        for i in range(1, 8):           # right movement
            b = loc[1] + i
            if b < 105:
                if [loc[0], chr(b)] in occupied_loc:
                    break
                else:
                    possible_loc.append([loc[0], chr(b)])

        for i in range(1, 8):           # left movement
            b = loc[1] - i
            if b > 96:
                if [loc[0], chr(b)] in occupied_loc:
                    break
                else:
                    possible_loc.append([loc[0], chr(b)])

    elif piece == "bishop":

        for i in range(1, 8):
            a = loc[0] + i
            b = loc[1] + i
            if a < 9 and b < 105:  # forward diagonal down movement
                if [a, chr(b)] in occupied_loc:
                    break
                else:
                    possible_loc.append([a, chr(b)])

        for i in range(1, 8):
            a = loc[0] + i
            b = loc[1] - i
            if a < 9 and b > 96:  # reverse diagonal down movement
                if [a, chr(b)] in occupied_loc:
                    break
                else:
                    possible_loc.append([a, chr(b)])

        for i in range(1, 8):
            a = loc[0] - i
            b = loc[1] - i
            if a > 0 and b > 96:  # reverse diagonal up movement
                if [a, chr(b)] in occupied_loc:
                    break
                else:
                    possible_loc.append([a, chr(b)])

        for i in range(1, 8):
            a = loc[0] - i
            b = loc[1] + i
            if a > 0 and b < 105:  # fwd diagonal up movement
                if [a, chr(b)] in occupied_loc:
                    break
                else:
                    possible_loc.append([a, chr(b)])

    elif piece == "knight":

        if loc[1] + 2 < 105:
            if loc[0] - 1 > 0:          #2 Right 1 Up
                if [loc[0] - 1, chr(loc[1] + 2)] not in occupied_loc:
                    possible_loc.append([loc[0] - 1, chr(loc[1] + 2)])
            if loc[0] + 1 < 9:          #2 Right 1 Down
                if [loc[0] + 1, chr(loc[1] + 2)] not in occupied_loc:
                    possible_loc.append([loc[0] + 1, chr(loc[1] + 2)])

        if loc[1] - 2 > 96:
            if loc[0] - 1 > 0:          #2 Left 1 Up
                if [loc[0] - 1, chr(loc[1] - 2)] not in occupied_loc:
                    possible_loc.append([loc[0] - 1, chr(loc[1] - 2)])
            if loc[0] + 1 < 9:          #2 Left 1 Down
                if [loc[0] + 1, chr(loc[1] - 2)] not in occupied_loc:
                    possible_loc.append([loc[0] + 1, chr(loc[1] - 2)])

        if loc[0] - 2 > 0:
            if loc[1] - 1 > 96:         #2 Up 1 Left
                if [loc[0] - 2, chr(loc[1] - 1)] not in occupied_loc:
                    possible_loc.append([loc[0] - 2, chr(loc[1] - 1)])
            if loc[1] + 1 < 105:        #2 Up 1 Right
                if [loc[0] - 2, chr(loc[1] + 1)] not in occupied_loc:
                    possible_loc.append([loc[0] - 2, chr(loc[1] + 1)])

        if loc[0] + 2 < 9:
            if loc[1] - 1 > 96:         #2 Down 1 Left
                if [loc[0] + 2, chr(loc[1] - 1)] not in occupied_loc:
                    possible_loc.append([loc[0] + 2, chr(loc[1] - 1)])
            if loc[1] + 1 < 105:        #2 Down 1 Right
                if [loc[0] + 2, chr(loc[1] + 1)] not in occupied_loc:
                    possible_loc.append([loc[0] + 2, chr(loc[1] + 1)])

    elif piece == "king":           #Movements for king. One in up, down, left, right and all diagonals

        if loc[0] - 1 > 0:
            if [loc[0] - 1, chr(loc[1])] not in occupied_loc:
                possible_loc.append([loc[0] - 1, chr(loc[1])])

        if loc[0] + 1 < 9:
            if [loc[0] + 1, chr(loc[1])] not in occupied_loc:
                possible_loc.append([loc[0] + 1, chr(loc[1])])

        if loc[1] + 1 < 105:
            if [loc[0], chr(loc[1] + 1)] not in occupied_loc:
                possible_loc.append([loc[0], chr(loc[1] + 1)])
            if loc[0] - 1 > 0:
                if [loc[0] - 1, chr(loc[1] + 1)] not in occupied_loc:
                    possible_loc.append([loc[0] - 1, chr(loc[1] + 1)])
            if loc[0] + 1 < 9:
                if [loc[0] + 1, chr(loc[1] + 1)] not in occupied_loc:
                    possible_loc.append([loc[0] + 1, chr(loc[1] + 1)])

        if loc[1] - 1 > 96:
            if [loc[0], chr(loc[1] - 1)] not in occupied_loc:
                possible_loc.append([loc[0], chr(loc[1] - 1)])
            if loc[0] - 1 > 0:
                if [loc[0] - 1, chr(loc[1] - 1)] not in occupied_loc:
                    possible_loc.append([loc[0] - 1, chr(loc[1] - 1)])
            if loc[0] + 1 < 9:
                if [loc[0] + 1, chr(loc[1] - 1)] not in occupied_loc:
                    possible_loc.append([loc[0] + 1, chr(loc[1] - 1)])

    elif piece == "queen":      #Any number of moves in any direction.
        for i in range(1, 8):
            a = loc[0] + i
            b = loc[1] + i
            if a < 9 and b < 105:  # forward diag down movement
                if [a, chr(b)] in occupied_loc:
                    break
                else:
                    possible_loc.append([a, chr(b)])

        for i in range(1, 8):
            a = loc[0] + i
            b = loc[1] - i
            if a < 9 and b > 96:  # reverse diag down movement
                if [a, chr(b)] in occupied_loc:
                    break
                else:
                    possible_loc.append([a, chr(b)])

        for i in range(1, 8):
            a = loc[0] - i
            b = loc[1] - i
            if a > 0 and b > 96:  # reverse diag up movement
                if [a, chr(b)] in occupied_loc:
                    break
                else:
                    possible_loc.append([a, chr(b)])

        for i in range(1, 8):
            a = loc[0] - i
            b = loc[1] + i
            if a > 0 and b < 105:  # fwd diag up movement
                if [a, chr(b)] in occupied_loc:
                    break
                else:
                    possible_loc.append([a, chr(b)])

        for i in range(1, 8):
            a = loc[0] + i
            if a < 9:  # vertical down movement
                if [a, chr(loc[1])] in occupied_loc:
                    break
                else:
                    possible_loc.append([a, chr(loc[1])])

        for i in range(1, 8):
            a = loc[0] - i
            if a > 0:  # vertical up movement
                if [a, chr(loc[1])] in occupied_loc:
                    break
                else:
                    possible_loc.append([a, chr(loc[1])])

        for i in range(1, 8):
            b = loc[1] + i
            if b < 105:  # right movement
                if [loc[0], chr(b)] in occupied_loc:
                    break
                else:
                    possible_loc.append([loc[0], chr(b)])

        for i in range(1, 8):
            b = loc[1] - i
            if b > 96:  # left movement
                if [loc[0], chr(b)] in occupied_loc:
                    break
                else:
                    possible_loc.append([loc[0], chr(b)])

    while status == 0:

        if not possible_loc:

            print("No possible moves.")
            if piece == "pawn" and loc[0] == 1:
                break
            else:
                occupied_loc.append([loc[0], chr(loc[1])])
                break

        print("The possible moves for ", piece, " are", possible_loc)
        selection = str(input("Select the new location of the piece from the given possible locations\n"))
        selection = selection.lower()
        try:
            selection = re.findall(r"[^\W\d_]|\d", selection)
            selection = [int(selection[0]), selection[1]]
        except ValueError:
            print("Make Proper Selection")
            continue
        if selection in possible_loc:
            print("The new selected location is ", selection)
            status = 1
        else:
            print("This is not a possible move. Select only from the list of possible moves.")
            print("\n")
            status = 0

    piece = ''
    occupied_loc.append(selection)
    occupied_loc = [x for x in occupied_loc if x != []]

    while ans == 0:
        if len(occupied_loc) == 64:
            print("The board is completely filled.")
            ans = 1
            game = 1

        else:
            choice = str(input("Do you want to continue? Yes or No \n"))
            choice = choice.lower()
            if choice == "yes":
                game = 0
                ans = 1
            elif choice == "no":
                game = 1
                ans = 1
            else:
                print("Incorrect selection")
                ans = 0

print("Thank you for playing.")


