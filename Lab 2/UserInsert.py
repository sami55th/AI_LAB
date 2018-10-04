l = [1,2,3,4,5,6,7,8,9]
cont = "yes"
while cont == "yes":
    i = int(input("Enter Value:"))
    j = int(input("Enter Position:"))
    l.insert(i,j)
    print (l)
    cont = input("Do You Want To Continue Press Yes:")

