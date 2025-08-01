def generate_numbers_1(max_number: int):
    print("called generate_numbers_1 function")
    numbers = []
    for i in range(1, max_number+1):
        numbers.append(i)
    return numbers

#Generator 객체를 만드는 함수 - yiled를 사용
def generate_numbers_2(max_number: int):
    print("called generate_numbers_2 function")
    for i in range(1, max_number+1):
        yield i



numbers_1 = generate_numbers_1(10)
numbers_2 = generate_numbers_2(10)
print(numbers_1)
print(numbers_2)

#(i**2 for i in numbers)
# def make_numbers():
#     for i in [1,2,3,4,5]:
#         yield i

# gen2 = make_numbers()
