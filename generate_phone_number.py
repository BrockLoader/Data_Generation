def generate_phone_number(amt):

    import pandas as pd

    import secrets as sc

    val = int(amt)

    ph_nums = list()

    loop_count = 0

    thousands = 1000

    while loop_count < val:
        phone = str('07 ' + str(sc.SystemRandom().randint(3, 7)) + str(sc.SystemRandom().randint(3, 7)) + str(sc.SystemRandom().randint(3, 7)) + str(sc.SystemRandom().randint(3, 7)) + ' ' + str(sc.SystemRandom().randint(1, 9)) + str(sc.SystemRandom().randint(1, 9)) + str(sc.SystemRandom().randint(1, 9)) + str(sc.SystemRandom().randint(1, 9)) )
        if phone in ph_nums:
            continue
        ph_nums.append(phone)
        loop_count = loop_count + 1
        if loop_count == thousands:
            print(thousands, ' Numbers Generated.')
            thousands = thousands + 1000
    
    ph_nums = pd.DataFrame(ph_nums)
    return(ph_nums)