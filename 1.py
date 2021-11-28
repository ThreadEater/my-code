dayPerMonth = [0,31,59,90,120,151,181,212,243,273,304,334,365]
def main():
    year,month,day = map(int,input().split())
    if (month <= 2):
        print(dayPerMonth[month - 1] + day)
    elif (year % 4 == 0 and year % 400 != 0 and month > 2):
        print(dayPerMonth[month - 1] + day + 1)
    elif (year % 4 != 0 and month < 2 ):
        print(dayPerMonth[month - 1] + day)
    
if __name__=="__main__":
    main()