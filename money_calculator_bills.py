amount = int(input("Enter $: "))

bill_20 = amount // 20
bill_5 = (amount - bill_20 * 20) // 5
bill_1 = (amount - ((bill_20*20) + (bill_5*5))) // 1

print("For the amount of", amount,"you will need",bill_20,"bills of 20,",bill_5,"bills of 5,",bill_1,"bills of 1.")