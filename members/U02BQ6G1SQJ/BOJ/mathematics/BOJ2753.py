import sys;

# sys.stdin = open("input1.txt", 'r');    # 1
# sys.stdin = open("input2.txt", 'r');    # 0

year = int(sys.stdin.readline());
print(1 if ((year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0))) else 0);
