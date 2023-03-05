def generate_names():

    import names

    val = input('How many names do you want to generate?: ')

    val = int(val)

    name_list = list()

    loop_count = 0

    while loop_count < val:
        full_name = names.get_first_name() + ' ' + names.get_last_name()
        if full_name in name_list:
            break
        name_list.append(full_name)
        loop_count = loop_count + 1
    
    return(name_list)


