import sys

sys.stdin = open("_직사각형길이찾기.txt")

T = int(input())

for test_case in range(1, T + 1):
    sides = dict()
    rect = map(int, input().split())
    
    for side in rect :
        if side in sides:
            sides[side] += 1
        else:
            sides[side] = 1

    
    for k, v in sides.items():
        if v == 1:
            answer = k
            break
        else:
            answer = k

    print(f'#{test_case} {answer}')