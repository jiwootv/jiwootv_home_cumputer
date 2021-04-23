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