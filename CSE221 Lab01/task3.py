file1=open("input3.txt",'r')
file2=open("output3.txt","w")

n = int(file1.readline().strip())
student_ids = list(map(int, file1.readline().split()))
marks = list(map(int, file1.readline().split()))

def rank_students(n, student_ids, marks):
    student_data = list(zip(student_ids, marks))
    student_data.sort(key=lambda x: (-x[1], x[0]))

    for student_id, mark in student_data:
        file2.write(f"Id:{student_id} Mark:{mark}\n")


if __name__ == "__main__":
    rank_students(n, student_ids, marks)

file1.close()
file2.close()