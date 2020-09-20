from random import randint
from time import sleep

winners_list = []
row_list = []
num = 0
num1 = 0
count = 0
prize_money = 0

budget = int(input("please enter you budget each round cost 3 nis: "))
while budget < 3:
    budget = int(input("not enough budget you need 3 nis or more to play: "))

print("\nrolling the winner's numbers...\n-----------------------------")
sleep(3)

while num < 6:
    winners_numbers = randint(1, 37)
    if winners_numbers not in winners_list:
        winners_list.append(winners_numbers)
        num += 1
print("the winner's number are: " + str(winners_list))

while budget > 2:
    budget -= 3
    print("\nrolling your numbers...\n-----------------------------")
    sleep(3)

    while num1 < 6:
        row_numbers = randint(1, 37)
        if row_numbers not in row_list:
            row_list.append(row_numbers)
            num1 += 1
    print("your numbers are: " + str(row_list))

    for i in row_list:
        if i in winners_list:
            count +=1
    if count == 6:
        prize_money += 1000000
        print("you won the big prize of 1000000 nis\n-----------------------------")

    elif count == 5:
        prize_money += 5000
        print("you won the prize of 5000 nis\n-----------------------------")

    elif count == 4:
        prize_money += 100
        print("you won the prize of 100 nis\n-----------------------------")

    elif count == 3:
        print("you won the prize of 10 nis\n-----------------------------")
        prize_money += 10

    num1 = 0
    row_list = []
    count = 0

print("\nCalculate the total amount of money you have won")
sleep(3)

print("You won a total of " + str(prize_money))


