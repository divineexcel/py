# 

if __name__ == '__main__':
    n = int(input())
x = range(3)
# print(x)
for i in x:
    print(i)

if __name__ == '__main__':
    n = int(input())

x = range(n)
for i in x:
    print(i**2)


x = 5
123456789

def print_without_spaces(n):
    result = ""
    for i in range (1, n + 1):
        result += str(i)
        print(result)


if __name__ == '__main__':
    n = int(input("Enter the value of n: "))



# without_spaces(n) 


def without_spaces(n):
    numbers = [str(i) for i in range (1, n + 1)]
    result = ''.join(numbers)
    print(result)

if __name__ == '__main__':
    n = int(input())

without_spaces(n) 
q = str(n)
print (type (q))



 


x = int(input())
y = int(input())
z = int(input())
n = int(input())

coordinates = []

for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            if i + j + k != n:
                coordinates.append([i, j, k])
print("List of all possible coordinates where the sum of i+j+k is not equal to n:")
print(coordinates)

set_from_list = set([1, 2, 1, 4, 3])
for i in set_from_list:
    print(i, end="")