
import time

initial_time = time.time()

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]



def print_board(b):
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print("------------------------")
        for j in range(len(b[0])):
            if j % 3 == 0 and j!=0:
                print(" | ", end="")
            if j == 8:
                print(b[i][j])
            else:
                print(str(b[i][j]) +" " ,end="")


# print(print_board(board))

def valid_box(b,num,pos):
    #checking row of the grid
    for i in range(len(b[0])):
        if b[pos[0]][i] == num and pos[1] != i:
            return False

    #checking column of the grid
    for j in range(len(b)):
        if b[j][pos[1]] == num and pos[0] != j:
            return False

    box_x = pos[1]//3
    box_y = pos[0]//3

    #checking box 
    for i in range(box_y*3,box_y * 3 + 3):
        for j in range(box_x*3, box_x * 3 + 3):
            if b[i][j] == num and (i,j) != pos:
                return False

    return True

def find_empty(board):
    for i,row in enumerate(board):
        for j,value in enumerate(row):
            if value == 0:
                return (i,j)
    return None


def solve_sudoko(b):
    find = find_empty(b)

    if not find:
        return True
    else:
        row,col = find
    
    for i in range(1,10):
        if valid_box(b,i,(row,col)):
            b[row][col] = i

            if solve_sudoko(b):
                return True

            b[row][col] = 0

    return False
    

print_board(board)
print("*************************")
if(solve_sudoko(board)):
    print("Sudoko solved successfully")
    print("*************************")
    print_board(board)
else:
    print("Soduoko cannot be solved")

finished_time = time.time()

print("\nTime taken to solve : ",(finished_time-initial_time))
print("")