budget = int(input("please enter your marketing budget in ILS: "))
print("\nFacebook campaign cost 100$ per day \nInstagram campaign cost 50$ per day.\n")

facebook = int(input("How long do you wants the Facebook campaign will run: "))*100
instagram = int(input("How long do you wants the Instagram campaign will run: "))*50

sum = ((facebook + instagram) * 3.4) * 1.17
print("\nyour marketing campaigns including tax cost you " + str("%.2f" % (sum)))

if budget < sum:
    print("\nyou need to add: " + str("%.2f" % (sum - budget)))
else:
    print("\nyour campaing run successfully")




