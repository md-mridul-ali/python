year=int(input("Enter any valid year:"))
if(year % 4 == 0 and year % 100 != 0):
    print(f"{year} is leap year.")
elif(year % 100 == 0 and year % 400 == 0):
    print(f"{year} is leap year.")
else:
    print(f"{year} not leap year.")