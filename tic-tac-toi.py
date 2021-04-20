string = "         "
def PRINT(string):
    print("---------")
    print("|", string[0], end = " ")
    print(string[1], end = " ")
    print(string[2], end = " |\n")
    print("|", string[3], end = " ")
    print(string[4], end = " ")
    print(string[5], end = " |\n")
    print("|", string[6], end = " ")
    print(string[7], end = " ")
    print(string[8], end = " |\n")
    print("---------")

PRINT(string)

a = 0
cordinates = [[string[0], string[1], string[2]],
              [string[3], string[4], string[5]],
              [string[6], string[7], string[8]]]

def impossible(check_str):  # function to check impossible condition

    x_str = check_str.count("X")  #x in string
    o_str = check_str.count("O")  #o in string

    if x_str - o_str <= -2 or x_str - o_str >= 2 or check_O(check_str) == check_X(check_str) == True:
        return 1
    return 0

def check_X(check_str):  #function to check X wins
    if check_str[0:3] == ['X', 'X', 'X'] or check_str[3:6] == ['X', 'X', 'X'] or check_str[6:9] == ['X', 'X', 'X'] or check_str[::4] == ['X', 'X', 'X'] or check_str[2:7:2] == ['X', 'X', 'X'] or check_str[:7:3] == ['X', 'X', 'X'] or check_str[1:8:3] == ['X', 'X', 'X'] or check_str[2::3] == ['X', 'X', 'X'] :
        return 1
    return 0

def check_O(check_str):  # function to check O wins
    if check_str[0:3] == ['O', 'O', 'O'] or check_str[3:6] == ['O', 'O', 'O'] or check_str[6:9] == ['O', 'O', 'O'] or check_str[::4] == ['O', 'O', 'O'] or check_str[2:7:2] == ['O', 'O', 'O'] or check_str[:7:3] == ['O', 'O', 'O'] or check_str[1:8:3] == ['O', 'O', 'O'] or check_str[2::3] == ['O', 'O', 'O']:
        return 1
    return 0

def check_not_finished(check_str):  #function to check Game finished or not or even draw
    l = [True for x in check_str if x == " "]
    if any(l) == False and check_O(check_str) == False and check_X(check_str) == False:
        return 1

chance = 0
a = 0

while a != 1:
    cord = input("Enter Cordinates: ").split()
    try:
        cord = [ int(_) for _ in cord]
    except ValueError:
        print("You should enter numbers!")
    i , j = cord
    if type(i) == int and type(j) == int:
        if i <= 3 and j <= 3 and i > 0 and j > 0:
            if cordinates[i-1][j-1] == "_" or cordinates[i-1][j-1] ==" " :

                if chance % 2 == 0:
                    cordinates[i-1][j-1] = "X"
                else:
                    cordinates[i-1][j-1] = "O"

                new_string = []
                for i in cordinates:
                    for _ in i :
                        new_string.append(_)
                PRINT(new_string)

                if impossible(new_string):
                    print("Impossible")
                    a = 1
                elif check_X(new_string):
                    print("X wins")
                    a = 1
                elif check_O(new_string):
                    print("O wins")
                    a = 1
                elif check_not_finished(new_string):
                    print("Draw")
                    a = 1

                chance += 1

            else:
                print("This cell is occupied! Choose another one!")
        else:
            print("Coordinates should be from 1 to 3!")
