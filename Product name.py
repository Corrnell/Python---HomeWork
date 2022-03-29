productName = "\"Pizza\""
productPrice = 10.00
deliveryCost = 25.00

print(productName,":",productPrice,"lei")

answer = input("Do you wanna buy? ")

if answer.lower() == "yes" or answer.lower() == "y":
    orderQuantity = int(input("How many: "))
    orderCost = orderQuantity * productPrice

    print("------------------")
    print("ORDER INFO")
    print(productName, "x",orderQuantity, "=", orderCost)

    answer2 = input("Do you want any delivery: ")


    if answer2.lower() == "yes" or answer2.lower() == "y":
        orderCost += deliveryCost
        print("Order cost including delivery will be", orderCost)
    elif answer2.lower() != "yes" or answer2.lower() != "y":
        print("Too bad :(")
        print("Order cost without including delivery will be", orderCost)
elif answer.lower() != "yes" or answer.lower() != "y":
    print("Too bad :(")
    quit()
