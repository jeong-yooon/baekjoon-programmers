def solution(scores):
    answer = 0
    target_a, target_b = scores[0]
    target_score = target_a + target_b

    # 첫번째 점수에 대해서 내림차순,
    # 첫 번째 점수가 같으면 두 번째 점수에 대해서 오름차순으로 정렬
    scores.sort(key=lambda x: (-x[0], x[1]))
    maxb = 0
    
    # 각 사원에 대해 처리
    for a, b in scores:
        # 만약 어떤 사원이 다른 임의의 사원보다 두 점수가 모두 낮은 경우가 한 번이라도 있다면 인센티브를 받지 못함
        if target_a < a and target_b < b:
            return -1
        
        # 현재 동료 평가 점수가 이전에 확인한 최대 동료 평가 점수보다 크거나 같으면
        if b >= maxb:
            maxb = b
            # 두 점수의 합이 최고점(target_score) 이상이면 석차 증가
            if a + b > target_score:
                answer += 1
            
    return answer + 1
