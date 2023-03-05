

def generate_bsb():

    import secrets as sc

    bsb = str(str(sc.SystemRandom().randint(1, 9)) + str(sc.SystemRandom().randint(1, 9)) + str(sc.SystemRandom().randint(1, 9)) + '-' + str(sc.SystemRandom().
    randint(1, 9)) + str(sc.SystemRandom().randint(1, 9)) + str(sc.SystemRandom().randint(1, 9)))
    
    return bsb