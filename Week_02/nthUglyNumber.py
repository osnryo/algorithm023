# 347. 前 K 个高频元素

def heapSort(arr):
    def sift_down(arr, root, k):
        val = arr[root]
        while root<<1 < k:
            chlid = root << 1
            if chlid|1 < k and arr[chlid|1] > arr[chlid]:
                chlid |= 1
            if arr[chlid] > val:
                arr[root] = arr[chlid]
                root = chlid
            else:
                break
        arr[root] = val

    arr = [0] + arr
    k = len(arr)
    for i in range((k-1)>>1, 0, -1):
        sift_down(arr, i, k) 
    for i in range(k-1, 0, -1):
        arr[1], arr[i] = arr[i], arr[1]
        sift_down(arr, 1, i)
    return arr[1:]