saal = int(input("Kripya saal enter karen: "))

if (saal % 4 == 0 and saal % 100 != 0) or (saal % 400 == 0):
    print(saal % 4 == 0)
    print(saal % 100 != 0)
    print("leap year")
else:
    print(saal % 4 == 0)
    print(saal % 100 != 0)
    print("not leap year")
