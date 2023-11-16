import random




class Player:
    def __init__(self,player_name,index):
        self.player_name = player_name
        self.index = index
        self.isActive = False


class Grid:
    def __init__(self, grid_size):
        self.Grid = self.initialize_grid_index(grid_size) # [[0] * grid_size] * grid_size
        self.Ladders = []
        self.snakes = []

    def insert_snake(self,snakes):
        for i in snakes:
            if i[0]>i[1]:
                self.snakes.append(i)

    def insert_ladder(self,ladders):
        for i in ladders:
            if i[0]<i[1]:
                self.Ladders.append(i)

    def initialize_grid_index(self,grid_size):
        Grid = [[0 for i in range(grid_size)] for j in range(grid_size)]

        init = grid_size*grid_size
        for i in range(grid_size):
            for j in range(grid_size):
                Grid[i][j] = init
                init = init - 1

        for row in range(grid_size-1,-1,-2):
            Grid[row].reverse()

        # for i in Grid:
        #     print(i,end="\n")

        return Grid

size = 10
grid = Grid(size)

grid.insert_snake([[98, 10], [50, 5], [25, 15], [75, 30], [80, 70]])
grid.insert_ladder([[20, 60], [71, 97], [35, 78]])


player1 = Player("player1",1)
player2 = Player("player2",1)
player3 = Player("player3",1)

players = []

players.append(player1)
players.append(player2)
players.append(player3)

gamestart = True

while gamestart:
    for player in players:
        choice = random.randint(1,6)
        if choice == 1 and player.isActive == False:
            player.isActive = True
            player.index += 1
            continue

        if player.isActive:
            if (player.index + choice) > size*size:
                continue
            else:
                player.index += choice

            if player.index == size*size:
                print(f'{player.player_name} won the game !!!')
                gamestart = False
                break

            # check for snake
            for i in grid.snakes:
                if player.index == i[0]:
                    player.index = i[1]
                    print(f'{player.player_name} fell down from snake to position {player.index}')

            # check for ladder
            for i in grid.Ladders:
                if player.index == i[0]:
                    player.index = i[1]
                    print(f'{player.player_name} climbed the ladder to position {player.index}')

            print(f'{player.player_name} at position {player.index}')




