def displayPathtoPrincess(n,grid):
#print all the moves here
    bot = []
    princess = []
    for row in grid:    
        for items in row:
            if items == "m":
                bot.append(grid.index(row))
                bot.append(row.index(items))
                
            if items == "p":
                princess.append(grid.index(row))
                princess.append(row.index(items))
 

        
        
    path = [bot[0]-princess[0], bot[1]-princess[1]]


    if path[0] > 0:
        for i in range(abs(path[0])):
            print ("UP")
    if path[0] < 0:
        for i in range(abs(path[0])):
            print ("DOWN")

    if path[1] > 0:
        for i in range(abs(path[1])):
            print ("LEFT")

    if path[1] < 0:
        for i in range(abs(path[1])):
            print ("RIGHT")


m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
