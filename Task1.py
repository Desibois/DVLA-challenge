limit = int(input("Number of cars: ")) + 1
loop = 1
distance = 1000
speedlimit = 30
list1 = {}
while loop != limit:
    reg = input("Car " + str(loop) + " Reg plate: ")
    time1 = float(input("Time entered: "))
    time2 = float(input("Time exited: "))
    speed = (time2 - time1)/distance
    if speed < speedlimit:
        pass
    elif speed > speedlimit:
        list1.update({reg: speed})
    loop = loop + 1

for i, j in list1.items():
    print(i, ' : ', j)




