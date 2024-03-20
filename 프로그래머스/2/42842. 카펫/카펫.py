def solution(brown, yellow):
    answer = []
    width = 1
    height = 1
    #노란색 영역의 길이 경우의 수 전체 탐색
    yellow_width = []
    for i in range(yellow , 0, -1):
        if yellow % i == 0:
            if (yellow // i) in yellow_width:
                break
            yellow_width.append(i)
    
    while width <= brown:
        width += 1
        height = brown // 2 - width + 2
        # 세로의 길이가 클 때는 패스
        if height > width:
            continue
        # 정사각형일때 노란색 영역도 정사각형인지 확인
        elif height == width:
            if yellow ** (1/2) == int(yellow ** (1/2)):
                answer.append(width)
                answer.append(height)
                break
            else:
                continue
        else:
            print(yellow_width)
            for i in yellow_width:
                if i + 2 == width and (yellow // i) + 2 == height:
                    answer.append(width)
                    answer.append(height)
                    width = brown + 1
                    break
            
            
                    
        
    
    return answer