def solution(numbers):
    answer = []

    for number in numbers:
        bin_number = list('0' + bin(number)[2:]) # 이진수로 변경 후 앞 '0b' 슬라이싱 하여 저장
        idx = ''.join(bin_number).rfind('0') # 리스트에서 가장 오른쪽에 있는 0의 인덱스를 탐색
        bin_number[idx] = '1' # idx에 해당하는 위치의 0을 1로 변경
        
        if number % 2 == 1: # 홀수일 때
            bin_number[idx+1] = '0' # 가장 오른쪽의 1을 0으로 변경
        
        answer.append(int(''.join(bin_number), 2)) # 이진수를 다시 10진수로 바꿔 저장

    return answer