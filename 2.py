def main():
    profit = int(input())
    if (profit <= 10):
        print(0.1*profit)
    elif (10 < profit <= 20):
        print(1 + (profit - 10) * 0.075)
    elif (20 < profit <= 40):
        print(1.75 + (profit - 20) * 0.05)
    elif (40 < profit <= 60):
        print(2.75 + (profit - 40) * 0.03)
    elif (60 < profit <= 100):
        print(3.35 + (profit - 60) * 0.015)
    elif (profit > 100):
        print(3.95 + (profit - 100) * 0.01)
if (__name__=="__main__"):
    main()