want_finish = 'y'

while want_finish=="y":
    amount = input("Enter amount: ")
    amount = int(amount)
    tens = amount//10
    amount = amount % 10

    print ("Tens: ", tens)
    print ("Tens rest: ", amount)

    fives = amount//5
    amount = amount % 5

    print ("Fifes: ", fives)
    print ("Fifes rest: ", amount)

    twos = amount//2
    amount = amount % 2

    print ("Two\'s: ", twos)
    print ("Two\'s rest: ", amount)

    print ("One\'s: ", amount)
    
    want_finish = input("Do you want to finish? (y/n): ")



