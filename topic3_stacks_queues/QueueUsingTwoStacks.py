import sys

my_queue = []
def enqueue(x):
    my_queue.append(x)

def dequeue():
    return my_queue.pop(0)

for i in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().strip().split()
    if command[0] == '1':
        enqueue(int(command[1]))
    elif command[0] == '2':
        dequeue()
    elif command[0] == '3':
        print(my_queue[0])
