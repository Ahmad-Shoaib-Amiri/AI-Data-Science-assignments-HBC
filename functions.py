'''Function'''
def repeatation(repeat, letter):
    count = 0
    for i in range(len(repeat)):
        if repeat[i] == letter:
            count += 1
    print(count)
sentence = input('Enter a sentence: ')
letter = input('Enter the letter you want to see the repeatation:')
repeatation(sentence, letter)
