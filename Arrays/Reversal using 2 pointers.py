def reverse(arr):
    left,right=0,len(arr)-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr

array=list(map(int,input("Enter the array").split()))
print(reverse(array))
