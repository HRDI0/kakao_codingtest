from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for k in course:                               #코스요리의 단품 주문 종류 ex) [2,3,4] -> AB... / ADF... / ABCD...
        candidates = []
        for menu_li in orders:
            for li in combinations(menu_li, k):   #iterable한 자료를 중복되지 않는 k 크기의 조합들로 만든다.(순열과는 다름.)
                res = ''.join(sorted(li))          #만들어진 k크기의 조합을 알파벳순으로 정렬해서 문자열로 만든다.
                candidates.append(res)              #만들어진 문자열은 코스요리 추가 후보로 리스트에 추가한다.
        sorted_candidates = Counter(candidates).most_common()
        #코스요리 추가 후보 리스트를 Counter객체로 만든후 가장 많이 주문된 순으로 나열한다. ex) (AB,4),(AF,3)....
        answer += [menu for menu, cnt in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]]
        #가장 많이 주문된 순으로 정렬된 코스요리 리스트중에서 가장 많이 주문된 메뉴를 answer 리스트에 추가한다.
        #if cnd > 1    ->    가장 많이 주문되었더라도 1번 주문은 제외
        # and cnt == sorted_candates[0][1]    ->    제일 많이 주문된 메뉴의 sorted_candates[0][1]은 주문횟수
    return sorted(answer)       #알파벳순으로 정렬하여 return

# n = list(input().split())
# m = list(map(int,input().split()))
# print(solution(n,m))

# ABCFG AC CDE ACDE BCFG ACDEH
# 2 3 4