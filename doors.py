door_num = list()

def doors(n):
    global door_num
    doors = [False] * n

    for x in range(n):
        for y in range(x, n, x+1):
            doors[y] = not doors[y]

    for z, door in enumerate(doors):
        if door == True:
            door_num.append(z+1)
doors(100)
print ("The following doors are open: ", door_num )  

            