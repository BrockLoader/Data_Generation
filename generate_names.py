def generate_names(val):

    import names

    val = int(val)

    name_list = list()

    loop_count = 0

    thousands = 1000

    while loop_count < val:
        full_name = names.get_first_name() + ' ' + names.get_last_name()
        if full_name in name_list:
            continue
        name_list.append(full_name)
        loop_count = loop_count + 1
        if loop_count == thousands:
            print(thousands, ' User Names Generated.')
            thousands = thousands + 1000
    
    return(name_list)


