answer = input('전화번호를 입력하세요. (아무거나) 숫자만 입력해 주세요. 길이는 꼭 11자리여야 합니다.')
answer2 = (answer[0:3]+'-'+answer[3:7]+'-'+answer[7:11])
print(f'당신이 입력한 전화번호는 {answer2}입니다.')
