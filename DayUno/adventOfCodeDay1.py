import sys

file_to_read = sys.argv[1]
prev = -1
ctr = 0
def partOne():
    with open(file_to_read, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if prev != -1:
                if prev < int(line):
                    ctr +=1
            prev = int(line)
        print(ctr)

def part2():
    prev_window = [-1, -1, -1]
    current_window = []
    ctr = 0
    with open(file_to_read, 'r') as f:
       lines = f.readlines()
       for line in range(len(lines)):
           for line2 in lines[line:]:
               if len(current_window) == 3:
                   print(current_window, prev_window)
                   if(sum(current_window) > sum(prev_window) and prev_window != [-1, -1, -1]):
                       ctr +=1

                   prev_window = current_window
                   current_window = []
                   break
               current_window.append(int(line2))
           
       print(ctr)

part2()