file1 = open('input1.txt', 'r')
file2 = open('output1.txt', 'w')

persons, edges = map(int, file1.readline().split())

parent = [i for i in range(persons + 1)]
rank = [0] * (persons + 1)
size = [1] * (persons + 1)

def find(A):
    if parent[A] != A:
        parent[A] = find(parent[A])
    return parent[A]

def friendship(A, B):
    root_A = find(A)
    root_B = find(B)

    if root_A != root_B:
        if rank[root_A] < rank[root_B]:
            parent[root_A] = root_B
            size[root_B] += size[root_A]
        elif rank[root_A] > rank[root_B]:
            parent[root_B] = root_A
            size[root_A] += size[root_B]
        else:
            parent[root_B] = root_A
            rank[root_A] += 1
            size[root_A] += size[root_B]

    return size[find(A)]

for _ in range(edges):
    A, B = map(int, file1.readline().split())
    friend_circle = friendship(A, B)
    file2.write(f"{friend_circle}\n")

file1.close()
file2.close()