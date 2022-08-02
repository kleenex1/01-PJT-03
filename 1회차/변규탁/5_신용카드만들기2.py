import sys

sys.stdin = open("_신용카드만들기2.txt")


T = int(input())

start = ["3", "4", "5", "6", "9"]

for test_case in range(1, T+1):
    card = input()
    count = 0
    
    if card[0] in start:
        for i in card:
            if i.isalnum():
                count += 1
        
    if count == 16:
        print(f'#{test_case} {1}')
    else:
        print(f'#{test_case} {0}')