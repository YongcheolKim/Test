"""간단한 파이썬 코드 예시"""


def greet(name):
    """이름을 받아 인사말을 반환합니다."""
    return f"안녕하세요, {name}님!"


def add(a, b):
    """두 수를 더합니다."""
    return a + b


def main():
    print(greet("세계"))
    print(f"3 + 5 = {add(3, 5)}")

    # 리스트와 반복문 예시
    numbers = [1, 2, 3, 4, 5]
    total = sum(numbers)
    print(f"{numbers}의 합계: {total}")

    # 짝수만 골라내기
    evens = [n for n in numbers if n % 2 == 0]
    print(f"짝수: {evens}")


if __name__ == "__main__":
    main()
