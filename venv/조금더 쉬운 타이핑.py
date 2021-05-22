"""이번에도 미쳤다...(지난번보단 나은데...)"""
# ㅋㅋㅋㅋ
empty_list = list()
print(len(empty_list))
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
animal_products = ['milk', 'meat', 'butter', 'yoghurt']
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB']
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']
print('과일:', fruits)
print('과일 갯수:', len(fruits))
print('야채:', vegetables)
print('야채 갯수:', len(vegetables))
print('동물 식품:', animal_products)
print('동물 식품 갯수:', len(animal_products))
print('인터넷 기술:', web_techs)
print('인터넷 기술 갯수:', len(web_techs))
print('국가:', countries)
print('국가 갯수:', len(countries))
fruits_fruit = fruits[0]
print(fruits_fruit)
fruits_fruit = fruits[1]
print(fruits_fruit)
fruits_fruit = fruits[3]
print(fruits_fruit)
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
last_fruit = fruits [-1]
second_fruit = fruits [-2]
print(last_fruit)
print(second_fruit)
all_furit = fruits[0:]
orange_and_mango = fruits[1:3]
orange_mango_lemon = fruits[1:]
all_furit = fruits[-4:]
orange_and_mango = fruits[-3:-1]
orange_mango_lemon = fruits[-3:]
fruits[0] = 'Avocado'
print(fruits)
fruits[1] = 'apple'
print(fruits)
last_index = len(fruits)-1
fruits[last_index] = 'lime'
does_exist = 'banana' in fruits
print(does_exist)
does_exist = 'lime' in fruits
print(does_exist)
fruits.append('apple')
print(fruits)
fruits.append('lime')
print(fruits)
fruits.insert(2, 'apple')
print(fruits)
fruits.insert(3, 'lime')
print(fruits)
print(fruits)
fruits.pop()
print(fruits)
fruits.pop()
print(fruits)
del fruits[0]
print(fruits)
del fruits[1]
print(fruits)
del fruits
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)
positive_numbers = [1, 2, 3,4,5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables )
num1 = [0, 1, 2, 3]
num2= [4, 5,6]
num1.extend(num2)
print('Numbers:', num1)
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]
negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits )
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits_copy.copy()
print(fruits_copy)
positive_numbers = [1, 2, 3,4,5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables )
num1 = [0, 1, 2, 3]
num2= [4, 5,6]
num1.extend(num2)
print('Numbers:', num1)
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]
num1 = [0, 1, 2, 3]
num2= [4, 5,6]
num1.extend(num2)
print('Numbers:', num1)
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]
negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits )
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits.reverse())
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages.reverse())
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
ages.sort(reverse=True)
print(ages)