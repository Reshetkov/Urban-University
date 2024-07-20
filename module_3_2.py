def send_email(message, recipient, sender = 'university.help@gmail.com'):
    if '@' not in recipient or '@' not in sender:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    elif recipient[-4:] != '.com' and recipient[-4:] != '.net' and recipient[-3:] != '.ru':
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    elif sender[-4:] != '.com' and sender[-4:] != '.net' and sender[-3:] != '.ru':
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    elif sender == recipient:
        print(message)
    elif sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса',sender, 'на адрес',recipient)
    elif sender != 'university.help@gmail.com':
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса',sender, 'на адрес',recipient)

recipient_address = input('Введите адрес получателя: ')
answer = input('По умолчанию адрес отправителя это university.help@gmail.com. Хотите изменить адрес отправителя? Да/Нет: ' ).lower()
if answer == 'нет':
    send_email('Нельзя отправить письмо самому себе!', recipient_address)
else:
    sender_address = input('Введите адрес отправителя: ')
    send_email('Нельзя отправить письмо самому себе!', recipient = recipient_address, sender = sender_address)