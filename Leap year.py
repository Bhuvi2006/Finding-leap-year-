#leap year

y=int(input("Enter the year: "))

leap=(y%4==0) and (y%100!=0) or (y%400==0)

print(leap)
    