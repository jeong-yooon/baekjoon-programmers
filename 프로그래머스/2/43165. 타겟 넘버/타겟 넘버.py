# def solution(numbers, target):
#     answer = 0
#     leaves = [0]
#     for num in numbers:
#         tmp = []
#         for parent in leaves:
#             tmp.append(parent + num)
#             tmp.append(parent - num)
#         leaves = tmp
#     for leaf in leaves:
#         if leaf == target:
#             answer += 1
#     return answer








def solution(numbers, target):
    answer = 0
    leaves = [0]
    for i in numbers:
        tmp = []
        for j in leaves:
            tmp.append(j+i)
            tmp.append(j-i)
        leaves = tmp
    for k in leaves:
        if k == target:
            answer += 1
    
    return answer





