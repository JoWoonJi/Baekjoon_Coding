import sys

n = int(input())
lv_list = [int(sys.stdin.readline().strip()) for _ in range(n)]

def roundup(num):
    return int(num) + 1 if num - int(num) >= 0.5 else int(num)

def level(lv_list):
    lv_list.sort()
    total = len(lv_list)
    cut = roundup(total * 0.15) 
    cut_list = lv_list[cut:total-cut] # 리스트 슬라이싱. 인덱스라서 cut포함하지 않고 total-cut 포함하지 않는다(초과 미만 느낌?). 예로 cut이 2라면 0 1 2인덱스라서 3부터 시작하게됨.
    if cut_list:  
        return roundup(sum(cut_list) / len(cut_list))
    return 0  

print(level(lv_list))

#처음에 round사용했는데 틀려서 의아
#계속 파다가 알아보니 round함수는 .5가 되었을때 가장 가까운 짝수로 반올림한단다. 으잉??? 
#예를 들어 2.5를 반올림하면 2가되는 황당한...그래서 roundup이라는 새로운 반올림을 정의하는 함수를 만들어야한다.
# # 소수점 첫째 자리에서 반올림
# print(round(2.3))  # 결과: 2
# print(round(2.6))  # 결과: 3
# print(round(2.5))  # 결과: 2 (가장 가까운 짝수로 반올림)
# print(round(3.5))  # 결과: 4 (가장 가까운 짝수로 반올림)

# # 소수점 둘째 자리에서 반올림 (두 번째 인자로 자릿수 지정)
# print(round(2.34, 1))  # 결과: 2.3
# print(round(2.35, 1))  # 결과: 2.4
# print(round(2.36, 1))  # 결과: 2.4
# print(round(2.25, 1))  # 결과: 2.2 (가장 가까운 짝수로 반올림)
# print(round(2.75, 1))  # 결과: 2.8

# # 음수 반올림
# print(round(-2.5))  # 결과: -2 (가장 가까운 짝수로 반올림)
# print(round(-2.51)) # 결과: -3


#그러면 파이썬은 왜 이런 반올림을 사용하느냐?
# 파이썬에서 round 함수가 .5의 경우 가장 가까운 짝수로 반올림하는 이유는 "은행가 반올림" 규칙(banker's rounding)을 따르기 때문입니다. 이 규칙은 통계학과 재무학에서 널리 사용되며, 반올림 과정에서 발생할 수 있는 오류를 줄이기 위해 고안되었습니다.

# 은행가 반올림의 목적
# 은행가 반올림의 주된 목적은 반올림 과정에서 발생하는 오류를 최소화하는 것입니다. 숫자들을 반올림할 때 항상 상향 또는 하향으로 반올림하면, 반올림된 값들의 합은 원래 값들의 합과 상당한 차이가 날 수 있습니다. 이러한 오류를 줄이기 위해, .5의 경우 짝수 쪽으로 반올림하면 전체적으로 반올림에 의한 오류가 상쇄되고 평균적으로 더 정확한 결과를 얻을 수 있습니다.

# 예시
# 예를 들어, 2.5와 3.5를 반올림하는 경우를 생각해봅시다. 만약 항상 반올림할 때 상향으로 처리한다면, 2.5는 3으로, 3.5는 4로 반올림되어 두 숫자 모두 상향 반올림됩니다. 그러나 은행가 반올림 규칙을 사용하면, 2.5는 2로, 3.5는 4로 반올림되어 한 숫자는 내림, 다른 숫자는 올림되어 반올림에 의한 오류가 상쇄됩니다.

# 다른 프로그래밍 언어와의 비교
# 다른 프로그래밍 언어나 시스템에서는 .5의 경우 항상 올림을 하는 방식을 사용할 수도 있습니다. 이는 언어나 사용하는 라이브러리, 심지어는 프로그램의 설정에 따라 다를 수 있습니다. 따라서 파이썬의 round 함수가 다소 직관적이지 않게 느껴질 수 있으나, 이는 의도된 동작이며 특정한 목적을 가지고 설계된 것입니다.

# 만약 파이썬에서 항상 .5가 있는 경우 상향 반올림을 하고 싶다면, 다른 방법을 사용해야 합니다. 예를 들어, 소수점 아래 값을 검사하여 직접 반올림 로직을 구현하거나, decimal 모듈을 사용하여 반올림 방식을 명시적으로 지정할 수 있습니다.

#재무적으로는 이렇게 사용한다고 한다. 처음 안 사실.