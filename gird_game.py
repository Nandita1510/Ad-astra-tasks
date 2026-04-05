def grid(b):
    size=len(b)
    for row in range(size):
        line=""
        for col in range(size):
            line+=f" {b[row][col]} " if b[row][col]!=0 else "   "
            if col<size-1:
                line+="|"
        print(line)
        if row<size-1:
            print("_" * (size * 4 - 1))

def check_win(b, s):
    for i in range(s):
        if sum(b[i])==15:
            return True
        if sum(b[j][i] for j in range(s))==15:
            return True
    if sum(b[i][i] for i in range(s))==15:
        return True
    if sum(b[i][s - i - 1] for i in range(s))==15:
        return True
    return False

def get_input(msg):
    while True:
        val=input(msg)
        if val.isdigit():
            return int(val)
        print("Please enter a valid number!")

def start():
    size=get_input("Enter grid size: ")

    while True:
        board=[[0]*size for _ in range(size)]
        turn=1

        while True:
            print(f"\nPlayer {turn}'s turn")
            grid(board)

            r=get_input("Enter row: ")
            c=get_input("Enter column: ")
            num=get_input("Enter a number (1-9): ")

            if r<0 or r>=size:
                print("Row out of range! Try again.")
                continue
            if c<0 or c>=size:
                print("Column out of range! Try again.")
                continue
            if num<1 or num>9:
                print("Number must be 1-9! Try again.")
                continue
            if board[r][c]!=0:
                print("Cell already filled! Try again.")
                continue
            board[r][c]=num
            if check_win(board, size):
                grid(board)
                print(f"\nPlayer {turn} wins!")
                break
            turn=2 if turn==1 else 1
        again=input("\nPlay again? (yes/no): ").strip().lower()
        if again!="yes":
            print("Thanks for playing")
            break
start()