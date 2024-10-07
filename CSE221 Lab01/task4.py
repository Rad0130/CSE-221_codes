file1=open("input4.txt",'r')
file2=open("output4.txt","w")

from datetime import datetime

n = int(file1.readline())
train_data = []
for _ in range(n):
            train_info = file1.readline().strip().split(" will departure for ")
            train_name = train_info[0]
            departure_time = train_info[1].split(" at ")[1]
            destination = train_info[1].split(" at ")[0]
            train_data.append((train_name, departure_time, destination))

def sort_trains(n, train_data):
    train_data.sort(key=lambda x: (x[0], -datetime.strptime(x[1], "%H:%M"), train_data.index(x)))

    with open("output4.txt", "w") as output_file:
        for train in train_data:
            file2.write(f"{train[0]} will departure for {train[2]} at {train[1]}\n")

if __name__ == "__main__":
    sort_trains(n, train_data)

file1.close()
file2.close()