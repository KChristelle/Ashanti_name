print('Hello we are about to find out what your Ashanti name is!!')
print('--------------------')
birthday = int(input('What is your birthday?'))
print('--------------------')
month = input('What is your birth month? (ex: January, April)')
print('--------------------')
year = int(input('What is the year were you born in? (Please, enter integers only)'))
print('--------------------')
gender = input('What is your gender?')


def get_last_digits(number, last_digit_count=2):
    return int(str(number)[-last_digit_count:])


def find_year_code():
    year_new = get_last_digits(year)
    year_code = int((year_new + (year_new / 4)) % 7)
    return year_code


def find_month_code(month_code):
    if month == 'January':
        month_code = 0
    elif month == 'February':
        month_code = 3
    elif month == 'March':
        month_code = 3
    elif month == 'April':
        month_code = 6
    elif month == 'May':
        month_code = 1
    elif month == 'June':
        month_code = 4
    elif month == 'July':
        month_code = 6
    elif month == 'August':
        month_code = 2
    elif month == 'September':
        month_code = 5
    elif month == 'October':
        month_code = 0
    elif month == 'November':
        month_code = 3
    elif month == 'December':
        month_code = 5
    else:
        print('The word you have entered is not a month.')
    return month_code


def leap_code(leap):
    if year / 4 == 0:
        leap = 1
    else:
        leap = 0
    return leap


def calculating_day(year_number, month_number, day_number, leap_number):
    day_of_birth = (year_number + month_number + day_number - leap_number) % 7
    return day_of_birth


# print(calculating_day(find_year_code(), find_month_code(month), birthday, leap_code(year)))


def ashanti_name():
    day_of_week = calculating_day(find_year_code(), find_month_code(month), birthday, leap_code(year))
    if day_of_week == 0 and gender == "Female":
        a_name = 'Akosa'
    elif day_of_week == 0 and gender == 'Male':
        a_name = 'Kwasi'
    elif day_of_week == 1 and gender == 'Female':
        a_name = 'Adwoa'
    elif day_of_week == 1 and gender == 'Male':
        a_name = 'Kadjo'
    elif day_of_week == 2 and gender == 'Female':
        a_name = 'Abeena'
    elif day_of_week == 2 and gender == 'Male':
        a_name = 'Kwabena'
    elif day_of_week == 3 and gender == 'Female':
        a_name = 'Akwa'
    elif day_of_week == 3 and gender == 'Male':
        a_name = 'Kwaku'
    elif day_of_week == 4 and gender == 'Female':
        a_name = 'Yaa'
    elif day_of_week == 4 and gender == 'Male':
        a_name = 'Yaw'
    elif day_of_week == 5 and gender == 'Female':
        a_name = 'Afia'
    elif day_of_week == 5 and gender == 'Male':
        a_name = 'Kofi'
    elif day_of_week == 6 and gender == 'Female':
        a_name = 'Amma'
    elif day_of_week == 6 and gender == 'Male':
        a_name = 'Kwame'
    else:
        print('Sorry I fed up')
    return print('Your name is:' + a_name)



