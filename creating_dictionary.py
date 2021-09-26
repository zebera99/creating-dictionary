with open('data/vocabulary.txt', 'w') as f:     #creating a dictionary file called vocabulary.txt in data folder
    while True:
        eng_voca = input('영어 단어를 입력하세요: ')
        if eng_voca == 'q':
            break

        kor_voca = input('한국어 뜻을 입력하세요: ')
        if kor_voca == 'q':
            break

        f.write(f'{eng_voca}: {kor_voca}\n')
