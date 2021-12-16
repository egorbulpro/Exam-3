def card_number():
    crd_nmbr = input('Введите пожалуйста номер Вашей карты: ')
    if len(crd_nmbr) < 16 or len(crd_nmbr) > 16:
        print('Вы ввели не верный номер')
    else:
        print(f'**** **** **** {crd_nmbr[-4:]}')

card_number()