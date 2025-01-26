def mp(arr):
    profit=0
    for i in range(len(arr)):
        buy=arr[i]
        for j in range(i+1,len(arr)):
            sell=arr[j]
            d=sell-buy
            if d>profit:
                profit=d
    return profit

def main():
    n=int(input("Enter number of days"))
    print("Enter stock prices")
    stocks=[]
    for i in range(n):
        ele=int(input())
        stocks.append(ele)
    profit=mp(stocks)
    print(f'Maximum profit possible: {profit}')

main()
