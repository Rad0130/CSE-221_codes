file1=open('input3.txt','r')
file2=open('output3.txt','w')

n=int(file1.readline())
Times=[]

for _ in range(n):
    start, end=map(int,file1.readline().split())
    Times.append((start, end))

def maximum(Times):
    if not Times:
        return 0, []
    sorted_times=sorted(Times, key=lambda x: x[1])

    max_times=1
    selected_slots=[sorted_times[0]]
    prev_end=sorted_times[0][1]

    for i in sorted_times[1:]:
        start, end=i
        if start>=prev_end:
            max_times+=1
            selected_slots.append(i)
            prev_end=end

    return max_times,selected_slots

max_times,selected_slots=maximum(Times)

file2.write(f"{str(max_times)}\n")
for i in selected_slots:
    file2.write(f"{' '.join(map(str,i))}\n")


file1.close()
file2.close()