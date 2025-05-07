for _ in range(4):  # 총 4줄을 입력받음
    numbers = list(map(int, input().split()))  # 각 줄의 숫자 4개를 리스트로 변환
    print(sum(numbers))  # 합계 출력