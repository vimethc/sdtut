for number in range(3):
    print("--------------------------")
    print("Outer loop iteration" + str(number))

    #Inner loop
    for another_number in range(4):
        print("***********************")
        print("In inner loop iteration" + str(another_number))


for x in range(1,4):
    for y in range(1,4):
        print('*',end='')
    print()


for i in range(1,4):
    for j in range(1,i+1):
        print("*",end="")
    print()