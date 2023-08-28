def solution(number, k):
    answer = [] # Stack
    
    for num in number:
        if not answer: # 스택이 비어있는 경우
            answer.append(num)
            continue
        if k > 0:
            while answer[-1] < num: # 스택의 맨 끝수가 새로운 수보다 작으면
                answer.pop() # 제거
                k -= 1 # 횟수 차감
                if not answer or k <= 0: # 스택이 비어있거나 횟수가 모두 차감되면 종료
                    break
        answer.append(num) # 새로운 수 스택에 저장
    if k > 0:
        answer = answer[:-k]
    return ''.join(answer)