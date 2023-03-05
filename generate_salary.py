
def generate_salary(min, max):
    import secrets as sc
    salary = sc.SystemRandom().randint(min, max)
    return salary