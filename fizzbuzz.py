# 1부터 100까지 반복하는 반복문 구현
for num in range(1, 101):
    # 현재 숫자가 3과 5의 공배수인지 확인하여 공배수인 경우 "FizzBuzz" 출력
    if num % 15 == 0:
        print("FizzBuzz")
    else:
        print(num)