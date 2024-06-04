# 1부터 100까지 반복하는 반복문 구현
for num in range(1, 101):
    # 현재 숫자가 3의 배수인지 확인하는 조건문
    if num % 3 == 0:
        # 3의 배수일 경우 "Fizz" 출력
        print("Fizz")
    else:
        # 3의 배수가 아닐 경우 숫자 출력
        print(num)
