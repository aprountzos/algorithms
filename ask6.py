def mergeSort(arr):

    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr)//2
    
    left = arr[:mid]
    right = arr[mid:]
    
    # αναρδρομικη κληση της μεθοδου για καθε μισο του array
    left, left_inv = mergeSort(left)
    right, right_inv = mergeSort(right)
    temp=[]

    i=j=0
    inversions = left_inv + right_inv

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1
            # len(left)-i = αριθμος στοιχειων που εχουν μεινει στο αριστερο μισο
            # αφου το στοιχειο που γινεται append στο temp απο το δεξι μισο
            # ειναι μικροτερο απο καθε στοιχειο που εχει μεινει στο αριστερο μισο
            inversions += len(left)-i

    #in case of any element left
    temp += left[i:]
    temp += right[j:]
    
    return temp, inversions



arr = [2,4,1,3,5] 
print(arr)
result, inversions = mergeSort(arr) 
print(result,"\nInversions: ",inversions) 