range = int(input("How many numbers you want to sum: "))
numList = []

i = 1
while (1 <= range):
    num = int(input(f"Enter number {i} value: "))
    numList.append(num)
    i+=1
    print(f"You entered these numbers {numList}")

sum = 0
for x in numList:
    sum = sum + x
    print(f"Boom Your sum is: {sum}") 

