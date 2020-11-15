

def max_profit(arr,start, stop):
    n = stop - start

    if n <= 1:
        return 0, start, stop
    else:    
        mid =(start + stop)//2
    
        leftbest, buyleft, sellleft  = max_profit(arr,start,mid-1)
        rightbest, buyright, sellright = max_profit(arr,mid,stop)
        buy=arr[start]
        buy_index=start
        sell=arr[mid]
        sell_index=mid
        for i in range(start,mid):
            if arr[i] < buy:
                    buy = arr[i]
                    buy_index = i
        
        for i in range(mid+1,stop):
            if arr[i] > sell:
                    sell = arr[i]
                    sell_index = i 
                    
        crossBest = sell-buy
    
        if rightbest > leftbest:
                if crossBest > rightbest:
                    return crossBest, buy_index, sell_index
                else:
                    return rightbest, buyright, sellright
        else:
                if crossBest > leftbest:
                    return crossBest, buy_index, sell_index
                else:
                    return leftbest, buyleft, sellleft
                    
                
                
                
arr=[]
sell,i,j=max_profit(arr,0,len(arr)-1)
print(sell,i,j)