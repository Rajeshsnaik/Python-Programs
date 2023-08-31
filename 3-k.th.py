def find( k, arr, l ):
    arr.sort(reverse=True)
    #sort the array in descending order
    print("kth max element is ",arr[k-1])

    # since indexing
    print("kth smallest element is ",arr[l-k])

array = [20, 34, 65, 78, 1, 2, 3, -1]
k = 3
# call function
find(k, array, len(array))