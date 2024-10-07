file1=open('input3.txt','r')
file2=open('output3.txt','w')

N=int(file1.readline())
arr=list(map(int, file1.readline().split()))
l=0
r=N-1

def merge(arr, l, mid, r):
    combo_count=0
    left_temp=arr[l:mid+1]
    right_temp=arr[mid+1:r+1]

    i=j=0
    k=l

    while i<len(left_temp) and j<len(right_temp):
        if left_temp[i]<=right_temp[j]:
            arr[k]=left_temp[i]
            i+=1
        else:
            arr[k]=right_temp[j]
            j+=1
            combo_count+=(mid+1)-(l+i)
        k+=1

    while i<len(left_temp):
        arr[k]=left_temp[i]
        i+=1
        k+=1

    while j<len(right_temp):
        arr[k]=right_temp[j]
        j+=1
        k+=1

    return combo_count

def merge_sort(arr,l,r):
    combo_count=0

    if l<r:
        mid=(l+r)//2
        combo_count += merge_sort(arr, l, mid)
        combo_count += merge_sort(arr, mid + 1, r)
        combo_count += merge(arr, l, mid, r)

    return combo_count

file2.write(str(merge_sort(arr,l,r)))


file1.close()
file2.close()