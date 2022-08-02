import sys

sys.stdin = open("_최빈수구하기.txt")


T = int(input())


for test_case in range(1, T + 1):
    N = int(input())
    score_list = dict()
    scores = map(int, input().split())
    
    for score in scores:
        if score in score_list:
            score_list[score] += 1
        else:
            score_list[score] = 1

    rank_1 = max(score_list.values())
    list_ = []
    
    for k, v in score_list.items():
        if v == rank_1:
            list_.append(k)
            
    list_.sort(reverse= True)
    print(f'#{test_case} {list_[0]}')

