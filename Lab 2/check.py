Even = False
l = [1, 2, 3, 4, 5, 6]
for i in l:
    if i % 2 == 0:
        Even = True
        break
if Even == True :
    print("Even Number Is Present")
else:
    print("Odd Number Is Present")