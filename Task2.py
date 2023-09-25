file = open("Illegal.txt", "w")


def checkreg(regplate):
    r1 = regplate[0:2]
    r2 = regplate[2:4]
    r3 = regplate[4:7]
    if r1.isalpha() and r2.isdigit() and r3.isalpha() and len(regplate) == 7:
        print("Registered")
    else:
        print("Unregistered")
        file.write(str(regplate)+"\n")


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
        file.write(str(reg) + " : " + str(speed) + "\n")
    checkreg(reg)
    loop = loop + 1
file.close()