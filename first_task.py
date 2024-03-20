import string
import datetime


def cipher():
    cipher = []
    n = int(input())

    for i in range(n):
        sum_day = 0
        sum_month = 0
        member_data = input().split(',')
        member = {
            "surname": member_data[0],
            "name": member_data[1],
            "patronymic": member_data[2],
            "birth_day": member_data[3],
            "birth_month": member_data[4],
            "birth_year": member_data[5]
            }
        input_date = member['birth_year'], member['birth_month'], member['birth_day']
        is_valid_date(input_date)
        fio = member["surname"] + member["name"] + member["patronymic"]
        unique_letters_count = len(set(fio))

        for j in range(len(member["birth_day"])):
            sum_day += int(member["birth_day"][j])

        for j in range(len(member["birth_month"])):
            sum_month += int(member["birth_month"][j])

        sum_day_month = sum_day + sum_month
        letter_pozition = string.ascii_lowercase.index(f'{member["surname"][0]}'.lower()) + 1
        cipher_i = hex(unique_letters_count + 64 * sum_day_month + 256 * letter_pozition).upper()

        if len(cipher_i) < 3:
            cipher_i = cipher_i.string.ljust(3, '0')

        cipher.append(cipher_i[-3:])

    return ' '.join(cipher)


def is_valid_date(input_date):
    year, month, day = input_date
    try:
        datetime.datetime.strptime(f'{year}-{month}-{day}', '%Y-%m-%d')
        date_1 = datetime.date(day=1, month=1, year=1950)
        date_2 = datetime.date(day=31, month=12, year=2021)
        date = datetime.date(day=int(day), month=int(month), year=int(year))
        date_1 < date < date_2
        return True
    except ValueError:
        return 'Uncorrect date'
    
print(cipher())