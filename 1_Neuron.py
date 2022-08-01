# from matplotlib import pyplot as plt

print("  I      Xt0     Xt1      Yp      Yt       e     DW0     W0      DW1      W1")
# Testing DATA
x0 = [t for t in range(0,51)]
x1 = [k for k in range(0,61)] 
y = []
xt0 = [0, 5, 10, 13, 16, 19, 22, 27, 30, 33, 38, 41, 46, 49, 52, 57, 60, 65, 68, 73, 78, 81, 86, 91, 94, 99, 104, 109, 114, 119, 122, 127, 130, 133, 136, 141, 144, 149, 152, 157, 162, 167, 172, 177, 182, 187, 192, 197, 200, 205] # < temp
xt1 = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245,] # < hum
yt =  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,] 
# learning rate
lr = 0.001 
epochs = 0
accuracy0 = [0 for a in range(len(xt0))]
accuracy1 = [0 for b in range(len(xt1))]
def safe_div(e):
    if e == 0:
        return 0
    return 1 / e
while epochs < 1:
    for i in range(len(xt0)): 
        for j in range(len(xt1)):
            Xt0 = xt0[i]

            Xt1 = xt1[j]

            Yt = yt[i] 
            
            B = 0 
            
            W0 = 0
            W1 = 0
            
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
print(f"{epochs:6} {dW0:12.4} {W0:6.4}")

print("Training DONE!")

accuracy_avg = (sum(accuracy0) + sum(accuracy1)) / (len(accuracy0) + len(accuracy1))

accuracy_avgg = accuracy_avg*100
print(f"ACCURACY: {accuracy_avgg:3.4}%")

for i in range(len(x0)):
    for j in range(len(x1)):
    
        Xt0 = x0[i]
        Xt1 = x1[j] 
        
        _Y = int(Xt0 * W0 + Xt1 * W1 + B) 
        
        Yp = 1 if _Y >= 1 else 0 
        
        y.append(Yp) 

print(f"{str(x0):3}:{str(Xt0):8}\n\n{str(x1):3}:{str(Xt1):8}")

print("Testing DONE!")

    # plt.plot(x,y) 
