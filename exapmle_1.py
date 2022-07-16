# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.

# def serchNumber (a, b):
#     my_list = [1]
#     i = 1
#     while len(my_list) < a:
#         my_list.append(my_list[-1]*b)
#     print(my_list)

# serchNumber(5, -3)

def print_numbers(x=[]):
    x.append(5)
    print(x)

a = []
print_numbers(x=a)
print_numbers(x=a)
print_numbers(x=a)
print_numbers(x=a)
print(f'---> {a}')