# Question 1
# n = int(input())
# x = n % 10
# n = n//10
# while n > 0:
#     if n % 10 > x:
#         x = n % 10
#     n = n//10
# print(x)

# Question 2
# import random
# number = random.randint(0, 100)
# while True:
#     answer = input('Guess the number: ')
#     if answer == "" or answer == "exit":
#         print("Exit the program")
#         break
#     if not answer.isdigit():
#         print("Print the right number")
#         continue
#     answer = int(answer)
#     if answer == number:
#         print('True!')
#         break
#     elif answer > number:
#         print('It is more than guessed number')
#     else:
#         print('It is less than guessed number')




# Question 3
# n = int(input())
# factorial = 1
# for x in range(1, n+1):
#     factorial *= x
# print(factorial)

# Question 4
# for x in range(1,10):
#     for n in range(1,10):
#         print("%4d" % (x*n), end='')
#     print()