def max_profit(arr,start, stop):
    n = stop - start

    if n <= 1:
        return 0, start, stop
    else:   
        # '//' για να παρω το floor της διαιρεσης
        # αλλιως mid=len(arr)//2  
        mid =(start + stop)//2

        # αναρδρομικη κληση της μεθοδου για καθε μισο του array
        leftbest, buyleft, sellleft  = max_profit(arr,start,mid-1)
        rightbest, buyright, sellright = max_profit(arr,mid,stop)

        # αρχικοποιηση τιμης αγορας/πωλησης και των αντιστοιχων index
        buy=arr[start]
        buy_index=start
        sell=arr[mid]
        sell_index=mid

        #δε χρησιμοποιησα min,max της python για να δειξω πως προκυπτει το Θ(n)
        #αναζητηση min στο αριστερο μισο
        for i in range(start,mid):
            if arr[i] < buy:
                    buy = arr[i]
                    buy_index = i

        #αναζητηση max στο δεξι μισο
        for i in range(mid + 1 ,stop + 1 ):
            if arr[i] > sell:
                    sell = arr[i]
                    sell_index = i 
                    
        crossBest = sell-buy
        
        #μπορουσε να χρησιμοποιηθει η max της python στο return
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
                    
                
                
                
arr=[13,4,6,1,2,2,7,44,2,100]
sell,i,j=max_profit(arr,0,len(arr)-1)
print(sell,i,j)