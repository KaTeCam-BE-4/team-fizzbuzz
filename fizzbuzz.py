# 1부터 100까지 반복하는 반복문 구현
for num in range(1, 101):
    # 현재 숫자가 3의 배수인지 확인하는 조건문
    if num % 3 == 0:
        # 3의 배수일 경우 "Fizz" 출력
        print("Fizz")
    # 현재 숫자가 5의 배수인지 확인하는 조건문
    elif num %5 ==0:
        # 5의 배수일 경우 "Buzz"출력
        print("Buzz")

    else:
        # 위의 조건을 만족시키지 못할경우 숫자 출력
        print(num)

