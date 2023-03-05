

def generate_acc():

    import secrets as sc

    acc = str(str(sc.SystemRandom().randint(1, 9)) + str(sc.SystemRandom().randint(1, 9)) + str(sc.SystemRandom().randint(1, 9)) + str(sc.SystemRandom().randint(1, 9)) + str(sc.SystemRandom().randint(1, 9)) + str(sc.SystemRandom().randint(1, 9)) + str(sc.SystemRandom().randint(1, 9)) + str(sc.SystemRandom().randint(1, 9)))
    
    return acc