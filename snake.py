
import random
import sys
import time

class sl:
    def __init__(self,n):
        # NUMBER OF PLAYERS
        self.n = n
        # SNAKE AND LADDER BOARD
        self.board = [[0 for _ in range(10)] for _ in range(10)]
        # BASE OF THE LADDER
        self.board[0][1]=23
        self.board[0][5] = 45
        self.board[1][0] = 59
        self.board[5][8] = 72
        self.board[5][3] = 96
        self.board[7][9] = 92
        # MOUTH OF THE SNAKE
        self.board[4][2] = 17
        self.board[4][9] = 5
        self.board[5][4] = 8
        self.board[7][7] = 15
        self.board[8][3] = 63
        self.board[8][6] = 49
        self.board[9][2] = 40
        # POSITION OF THE PLAYERS
        self.status = [0 for _ in range(n)]
        # DICE
        self.dice = [1,2,3,4,5,6]

    def start(self):
        i=0
        while(i!=self.n):
            val=random.choice(self.dice)
            print("--> PLAYER {} CHANCE\nROLLING THE DICE..\n".format(i+1))
            time.sleep(2)
            print("THE DICE TURNS TO THE NUMBER {}\n".format(val))
            self.status[i]+=val
            self.win(i)
            time.sleep(2)
            print("THE PLAYER {} MOVES UP TO {} CELL\n".format(i+1,self.status[i]))
            x=self.status[i]//10
            y=self.status[i]%10
            if(y==0):
                x-=1
                y=10
            time.sleep(2)
            if(x%2==0):
                if(self.board[x][y-1]>0):
                    if(self.board[x][y-1]<self.status[i]):
                        print("OOPS!!\nPLAYER {} WAS ATTACKED BY A SNAKE.\nPLAYER {} MOVES DOWN TO {} CELL.\n".format(i+1,i+1,self.board[x][y-1]))
                    else:
                        print("LUCKY ROLL!!\nPLAYER {} FOUND A LADDER.\nPLAYER {} MOVES UP TO {} CELL.\n".format(i+1,i+1,self.board[x][y-1]))
                    self.status[i]=self.board[x][y-1]
                else:
                    print("PLAYER {} IS SAFE FROM THE SNAKES.\nPLAYER {} COULDN'T FIND ANY LADDERS TO CLIMB.\n".format(i+1,i+1))
            else:
                if (self.board[x][10-y]>0):
                    if (self.board[x][10-y] < self.status[i]):
                        print("OOPS!!\nPLAYER {} WAS ATTACKED BY A SNAKE.\nPLAYER {} MOVES DOWN TO {} CELL.\n".format(i+1,i+1,self.board[x][10-y]))
                    else:
                        print("LUCKY ROLL!!\nPLAYER {} FOUND A LADDER.\nPLAYER {} MOVES UP TO {} CELL.\n".format(i+1,i+1,self.board[x][10-y]))
                    self.status[i]=self.board[x][10-y]
                else:
                    print("PLAYER {} IS SAFE FROM THE SNAKES.\nPLAYER {} COULDN'T FIND ANY LADDERS TO CLIMB.\n".format(i+1,i+1))
            time.sleep(1)
            i+=1



    def win(self,ind):
        if(self.status[ind]>=100):
            print("VICTORY!! \n\nPLAYER {} HAS WON THE GAME.".format(ind+1))
            sys.exit()


def rules():
    print("1. Game can comprise of any number of players.")
    print("2. The player who reaches to \'100\' first wil win the game.")
    print("3. If the player happend to get caught in the snakes mouth, the player will move its tail.")
    print("4. If the player happend to reach the base of the ladder, the player will move to the top.\n")


def inp():
    print("\nLET'S PLAY SNAKE AND LADDER\n")
    rules()
    return int(input("ENTER THE NUMBER OF PLAYERS: "))


inst = sl(inp())
print("\nLET'S BEGIN\n")
while(1):
    inst.start()