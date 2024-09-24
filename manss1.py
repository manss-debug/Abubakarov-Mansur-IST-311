# 1 задание
a = int(input())
if a == 1:
    print("Январь")
elif a == 2:
    print("Февраль")
elif a == 3:
    print("Апрель")
elif a == 4:
    print("Март")
elif a == 5:
    print("Май")
elif a == 6:
    print("Июнь")
elif a == 7:
    print("Июль")
elif a == 8:
    print("Август")
elif a == 9:
    print("Сентябрь")
elif a == 10:
    print("Ноябрь")
elif a == 11:
    print("Октябрь")
elif a == 12:
    print("Декабрь")
elif a > 12 or a < 1:
    print("Нет такого месяца")

# 2 задание
a = int(input())
if a % 2 == 0:
    print("Четное")
else:
    print("Нечетное")

# 3 задание
N = int(input())
if N > 40:
    print("Stonks")
elif N == 40:
    print("Neznayu")
else:
    print("Not stonks")

# 4 задание
year = int(input())


def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


def is_year_leap(a):
    if a % 4 == 0:
        if a % 100:
            if a % 400:
                return True
            else:
                return False


year = int(input())
print(is_year_leap(year))


# 5 задание
def is_prime(n, i=2):
    if n == 1:
        return False
    if n == 2:
        return True
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return is_prime(n, i + 1)


num = int(input())
result = is_prime(num)

if result:
    print(f"Число {num} является простым")
else:
    print(f"Число {num} не является простым")

# 6 задание
a = 10
b = 3
c = [(-138 / 2) ** 1.3]
d = [abs((-69 / 28 ** 5.1) * 4)]
if a * 3.6 > b or (b in c and b in d):
    temp = a
    a = b
    b = temp

print("a =", a)
print("b =", b)

# 7 задание
d = []
d.append(int(input()))
d.append(int(input()))
d.append(int(input()))
d.append(int(input()))
d.append(int(input()))
if len(set(d) == len(d)):
    print("Все уникальные")
else:
    print("Повторяются")
kolotr = sum(num < 0 for num in d)
print("Кол-во отриц = ", kolotr)
kolchet = sum(nums % 2 == 0 for nums in d)
print("Кол-во четных", kolchet)
pr = sum(-256 <= nummm <= 1024 for nummm in d)
print("Кол-во чисел в промежутке = ", pr)

# 8 задание
a = int(input())
b = int(input())
c = int(input())
n = ((a ** 2 + b ** 3) // c + 3) // 4
print(n)
if n % 2 == 0:
    print('chet')
else:
    print('nechet')
