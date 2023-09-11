from collections import deque

def solution(s):
    rotate = len(s) # 문자열 총 길이
    queue = deque(s) # 큐 선언
    answer = 0
    
    for i in range(rotate): # 문자열 탐색
        if i != 0: 
            sym = queue.popleft() # 맨 앞 문자열
            queue.append(sym) # 맨 뒤로 이동
            
        stack = []
        for q in queue:
            if stack: # 괄호의 짝이 맞으면 스택에서 해당 괄호를 제거하고
                if stack[-1] == '[' and q == ']': 
                    stack.pop()
                elif stack[-1] == '{' and q == '}':
                    stack.pop()
                elif stack[-1] == '(' and q == ')':
                    stack.pop()
                else:
                    stack.append(q)
            else: # 짝이 맞지 않으면 스택에 추가한다.
                stack.append(q)

        if len(stack) == 0: # 스택이 다 비워지면 x 카운팅
            answer += 1
            
    return answer