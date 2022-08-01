# from matplotlib import pyplot as plt

print("  I      Xt0     Xt1      Yp      Yt       e     DW0     W0      DW1      W1")
# Testing DATA
x0 = [t for t in range(0,51)]
x1 = [k for k in range(0,61)] 
y = []
xt0 = [0,   5, 10, 15, 20, 25, 27, 30, 35, 40] # < temp
xt1 = [10, 20, 30, 35, 40, 45, 50, 50, 65, 70] # < hum
yt =  [0,   0,  0,  0,  0,  1,  1,  1,  1,  1] 
W0 = 0
W1 = 0
# learning rate
lr = 0.001 
epochs = 0
accuracy0 = [0 for a in range(len(xt0))]
accuracy1 = [0 for b in range(len(xt1))]
def safe_div(x):
    if x == 0:
        return 0
    else:
        return 1 /x

while epochs < 1:

    for i in range(len(xt0)): 
        for j in range(len(xt1)):
            Xt0 = xt0[i]

            Xt1 = xt1[j]

            Yt = yt[i] 

            B = 0 



            _Y = int(Xt0 * W0 + Xt1 * W1 + B)

            Yp = 1 if _Y >= 1 else 0 

            e = Yt - Yp 

            dW0 = lr * e * Xt0
            dW1 = lr * e * Xt1

            W0 += dW0
            W1 += dW1
            print(f"{i:3}:{Xt0:8}{Xt1:8}{Yp:8}{Yt:8}{e:8}{dW0:8.3}{W0:8.3}{dW1:8.3}{W1:8.3}")

            accuracy0[i] = safe_div(e)
            accuracy1[i] = safe_div(e)
    epochs += 1
print("Epochs  Delta Weight  Weight")
print(f"{epochs:6} {dW0:12.4}   {W0:6.4}")

print("Training DONE!")

accuracy_avg = (sum(accuracy0) + sum(accuracy1)) / (len(accuracy0)+ len(accuracy1))
print(accuracy0)
print(accuracy1)

print(f"ACCURACY: {accuracy_avg*100}%")

# for j in range(len(x1)):
#     for i in range(len(x0)):
#         Xt0 = x0[i]
#         Xt1 = x1[j]
#         _Y = int(Xt0 * W0 + Xt1 * W1 + B)
#         Yp = 1 if _Y >= 1 else 0 
#         print(f"{j:3}:{Xt0:8}{Xt1:8}{Yp:8}{Yt:8}") 
print("Testing DONE!")
