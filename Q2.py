day = int(input("Enter day: "))
month = int(input("Enter month(integer):"))
year = int(input("Enter year:"))
if month>= 1 and month<=12 and day>=1 and day<=31 and year>= 1800 and year<=2025:
    print()    
else:
    print("Wrong input... not supported")
    exit()
###if the date is not the end of a month(i.e btw 1 and 27)
if day<=27:
    day = day+1
    print("Next date is ",day,"/",month,"/",year)
### if the date is 28 of Feb
elif day == 28 and month == 2:
    ###And year is a leap year
    if year%4==0:
        print("Next date is 29/02/",year)
    else:
        print("Next date is 01/03/",year)
elif day == 30:
    ###For months having 30 days
    if month in [4,6,9,11]:
        print("Next date is 01/",month+1,"/",year)
    else:
        print("Next date is 31/",month,"/",year)
elif day == 31:
    ###if 31st of december
    if month == 12:
        print("Next date is 01/01/",year+1)
    else:
        print("Next date is 01/",month+1,"/",year)
        
        
