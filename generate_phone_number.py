
def phone_number():

    import secrets as sc

    return str('07 3' + str(sc.SystemRandom().randint(5, 7)) + str(sc.SystemRandom().randint(5, 7)) + str(sc.SystemRandom().randint(5, 7)) + ' ' + str(sc.SystemRandom().randint(1, 9)) + str(sc.SystemRandom().randint(1, 9)) + str(sc.SystemRandom().randint(1, 9)) + str(sc.SystemRandom().randint(1, 9)) )