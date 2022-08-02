import sys

sys.stdin = open("_신용카드만들기1.txt")

T = int(input())

for test_case in range(1, T + 1):
    card = list(map(int, input().split()))

    fifteen = 0
    for i in range(1, len(card) + 1) :
        if i % 2 == 0:
            fifteen += card[i-1]
        else:
            fifteen += card[i-1]*2

    if fifteen % 10 == 0 :
        answer = 0
    else:
        answer = 10 - (fifteen % 10) 
    
    print(f'#{test_case} {answer}')