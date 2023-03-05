

def generate_accountnumber(amt):

    import pandas as pd

    import secrets as sc

    val = int(amt)

    acc_nums = list()

    loop_count = 0

    thousands = 1000

    while loop_count < val:
        acc = str(str(sc.SystemRandom().randint(1, 9)) + str(sc.SystemRandom().randint(1, 9)) + str(sc.SystemRandom().randint(1, 9)) + str(sc.SystemRandom().randint(1, 9)) + str(sc.SystemRandom().randint(1, 9)) + str(sc.SystemRandom().randint(1, 9)) + str(sc.SystemRandom().randint(1, 9)) + str(sc.SystemRandom().randint(1, 9)) + str(sc.SystemRandom().randint(1, 9)))
        if acc in acc_nums:
            continue
        acc_nums.append(acc)
        loop_count = loop_count + 1
        if loop_count == thousands:
            print(thousands, ' Account Numbers Generated.')
            thousands = thousands + 1000
    
    acc_nums = pd.DataFrame(acc_nums)
    return(acc_nums)