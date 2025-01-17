EurRon = 4.97
UsdRon = 4.87
HufRon = 0.012
PlnRon = 1.16

# Cur = input("Insert curency to convert:")
Cur = None
Er = 1

while Cur != "Euro" and Cur != "Usd" and Cur != "Usd":
    Cur = input("Insert curency to convert:")

x = input("How much in ")
x=int(x)

if Cur == "Euro":
    print("Result: ", EurRon*x)
elif Cur == "Usd":
    print("Result: ", UsdRon*x)
elif Cur == "Huf":
    print("Result: ", HufRon*x)
elif Cur == "Pln":
    print("Result: ", PlnRon*x)
else:
    Er == 0 