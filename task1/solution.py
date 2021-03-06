SIGNS = [(119, 'Козирог'), (218, 'Водолей'), (320, 'Риби'), (420, 'Овен'),
         (520, 'Телец'), (620, 'Близнаци'), (721, 'Рак'), (822, 'Лъв'),
         (922, 'Дева'), (1022, 'Везни'), (1121, 'Скорпион'),
         (1221, 'Стрелец'), (1231, 'Козирог')]


def what_is_my_sign(day, month):
    """ Return the horoscope sign according to the day and month. """
    date = month*100 + day
    for sign_end_date, sign in SIGNS:
        if date <= sign_end_date:
            return sign
