import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
broken = list(map(int, input().split()))

# 현재 채널에서 + 혹은 -만 사용하여 이동하는 경우
min_count = abs(100 - n)

for nums in range(1000001):
    nums = str(nums)

    for j in range(len(nums)):
        # 각 숫자가 고장났는지 확인 후, 고장 났으면 break
        if int(nums[j]) in broken:
            break

        # 고장난 숫자 없이 마지막 자리까지 왔다면 min_count 비교 후 더 작은 값으로 업데이트
        elif j == len(nums) - 1:
            min_count = min(min_count, abs(int(nums) - n) + len(nums))

print(min_count)