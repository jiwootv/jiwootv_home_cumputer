"저기 229줄을 어떻게 쓰나요? ㄷㄷ (근데 썼네)"


# 한줄
letter = 'p'
print(letter) # p
print(len(letter)) # 1
greeting = "hello! world!" # hello! world
print(greeting)
print(len(greeting))
sentence = """"i hope you are enjoying 30 days df python challenge


"""
print(sentence)

# 여러줄 작성
multiline_string = '''I am a teacher and anjoy teaching.
 I didn 't find anything as rewding as empowerring people.
 Tgay is why I cteated 30 days python.
 
 
 '''
print(multiline_string)

# 여러줄 또다른 방법
multiline_string = """I am a teacher and anjoy teaching.
 I didn 't find anything as rewding as empowerring people.
 Tgay is why I cteated 30 days python.
 
 
 """
print(multiline_string)

# 스트링 다루기
frist_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = frist_name + space +last_name
print(full_name) # Asabeneh Yetayeh

# 스트링의 길이 확인

print(len(frist_name)) # 8
print(len(last_name))  # 7
print(len(frist_name) > len(last_name)) # True
print(len(full_name)) # 15

# 인덱스로 스트링 다루기

language = 'Python'
first_letter = language[0]
# 여기서부터는 주석 없음 (# 없음 (# 없음(# 없음(# 없음(# 없음(# 없음(# 없음)))))))
print(first_letter)
second_letter = language[1]
print(second_letter)
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)

language = 'python'
last_letter = language[-1]
print(last_letter)
second_last = language[-2]
print(second_last)

language = 'python'
frist_three = language [0:3]
last_three = language [3:6]
print(last_three)

last_three = language[-3:]
print(last_three)
last_three = language[3:]
print(last_three)

language = 'python'
pto = language [0:6:2]
print(pto)

print('I hope every one enjoying the python challenge. \nDo you?')
print('Days \ttopics \tExercisse')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a back slash simbol(\\)')
print('In every programming language iy syarts with \"Hello, World!\"')


challenge = 'thirty days of python'
print(challenge.capitalize())

challenge = 'thirty days of python'
print(challenge.count('y'))
print(challenge.count('y', 7, 14))
print(challenge.count('th'))

challenge = 'thirty days of python'
print(challenge.endswith('on'))
print(challenge.endswith('tion'))

challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())
print(challenge.expandtabs(10))

challenge = 'thirty days of python'
print(challenge.find('y'))
print(challenge.find('th'))

frist_name = 'Asabeneh'
last_name = 'Yetayeh'
job = 'teacher'
coutry = 'Finland'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(frist_name, last_name, job, coutry)
print(sentence)

radius = 10
pi = 3.14
area = pi
result = 'The area of circle with {} is {}'.format(str(radius), str(area))
print(result)

challenge = 'ThirtyDaysPython'
print(challenge.isalnum())
print('\t')

challenge = '30DaysPython'
print(challenge.isalnum())
print('\t')

challenge = 'thirty days of python'
print(challenge.isalnum())
print('\t')

challenge = 'thirty days of python 2019'
print(challenge.isalnum())
print('\t')

challenge = 'thirty days of python'
print(challenge.isalpha())
print('\t')

num = '123'
print(num.isalpha())
print('\t')


challenge = 'Thirty'
print(challenge.isdigit())
print('\t')

challenge = '30'
print(challenge.isdigit())
print('\t')

num = '10'
print(num.isdecimal())
num = '10.5'
print('\t')

print(num.isdecimal())
print('\t')


challenge = '30DaysOfPython'
print(challenge.isidentifier())
print('\t')

challenge = 'thirty_days_of_python'
print(challenge.isidentifier())

print('\t')
print('\t')
print('\t')

challenge = 'thirty days of python'
print(challenge.islower())
print('\t')
challenge = 'Thirty days of python'
print(challenge.islower())
print('\t')


challenge = 'thirty days of python'
print(challenge.isupper())
print('\t')
challenge = 'THIRTY DAYS DF PYTHON'
print(challenge.isupper())
print('\t')

num = '10'
print(num.isnumeric())
print('\t')
print('ten'.isnumeric())
print('\t')
print('\t')
print('\t')

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '#, '.join(web_tech)
print(result)
print('\t')

challenge = 'thirty days of python'
print(challenge.strip())

challenge = 'thirty days of python'
print(challenge.replace('python', 'coding'))

challenge = 'thirty days of python'
print(challenge.split())

challenge = 'thirty days of python'
print(challenge.title())

challenge = 'Thirty Days Of Python'
print(challenge.swapcase())

challenge = 'thirty days of python'
print(challenge.startswith('thirty'))
challenge = '30 days of python'
print(challenge.startswith('thirty'))
# 이건 너무한거 아닙니까!!!!!!!
#선생님 이건 너무하셨네요...
#(근데 이걸 한 내가 더 신기하겠지?)
# [저도 그래요〕
#(쓸떼없이 안 맞는 과로([〕))
#(진짜 이런걸 할수 있구나... 나같은 놈이... 엌 힘들었어)+