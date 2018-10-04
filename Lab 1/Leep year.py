year = int(input("Enter The Year You Want To Check: "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("{0} Is a Leep Year,it has 366 days".format(year))
        else:
            print("{0} Is Not A Leep Year,it has 365 Days".format(year))
    else:
        print("{0} Is  A Leep Year,it has 366 Days".format(year))
else:
    print("{0} Is Not A Leep Year,it has 365 Days".format(year))
