#간결하게
import sys
input=sys.stdin.readline
n=int(input())
m=int(input())
a=input()
ans=0;cnt=0;i=0
while i<m:
  if a[i:i+3]=='IOI':
    i+=2
    cnt+=1
    if cnt==n:
      ans+=1
      cnt-=1
  else:
    cnt=0
    i+=1
print(ans)
# #복습
# #100
# import sys

# N = int(sys.stdin.readline().strip())
# M = int(sys.stdin.readline().strip())
# S = sys.stdin.readline().strip()

# P = 'IOI'

# cnt = i = answer = 0

# # 입력받은 S의 길이만큼 반복
# while i < (M - 1):
#   # 현재 반복되는 문자열이 'IOI'냐 ?
#   if S[i : i+3] == P:
#     # 그렇다면 다음에도 반복하는지 확인하기 위해 i+2
#     i += 2
#     # 'IOI' 반복 수 저장
#     cnt += 1
#     # 반복 수 cnt가 우리가 원하는 N과 동일하냐 ?
#     if cnt == N:
#       # 그렇다면 Pn을 찾은 것이므로 answer + 1
#       answer += 1
#       # 지금 Pn의 일부를 포함해서 또다른 Pn이 나올 수 있으므로 
#       # cnt를 초기화하지 않고 -1만 함
#       cnt -= 1

#   # 현재 반복되는 문자열이 'IOI'가 아니냐 ?
#   else:
#     # 그럼 다음 인덱스로 이동
#     i += 1
#     # cnt 초기화
#     cnt = 0

# print(answer)

#50
# N = int(input())
# M = int(input())
# S = input()

# def count_pn(N, S):
#     target = 'I' + 'OI' * N 
#     count = 0
#     for i in range(len(S) - len(target) + 1):
#         if S[i:i+len(target)] == target:
#             count += 1
#     return count

# count = count_pn(N, S)
# print(count)
