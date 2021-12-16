def word_palindrom():
    wrd_pldr = input('Введите проверяемое слово: ')
    if wrd_pldr == wrd_pldr[::-1]:
        print("Введеное слово является палиндромом")
    else:
        print('Веденное слово не является палиндромом')

word_palindrom()