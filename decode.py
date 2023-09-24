print('\n\n\n\n\n\n\n\n\n\n\n\n')
print('\033[91m⢸⣿⠛⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠉⠉⠛⢿⣿\n⠄⡇⢰⣿⣇⡀⠄⠄⣝⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⡄⠄⠈⠄⣷⢠⡆\n⢹⣿⣼⣿⣯⢁⣤⣄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⣴⠶⣲⣵⠟⠸\n⠄⢿⣿⣿⣿⣷⣮⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣾⣟⣡⡴⠄\033[0m')
print('\n\n')
print('\033[96mДекодер поддерживает только английские буквы!\033[0m\n\n1 - Декодер строчки в бинарный код\n2 - Декодер бинарного кода в строчку\nbreak - Завершить работу декодера')
while True:
    type = input('\n\nТип декодера: ')
    if type == '1':
        while True:
            string = input('\n\n         Введите строчку > ')
            if string == 'break':
                break
            try:
                print('         \033[92m[DECODE]\033[0m ', end='')
                print(''.join(format(ord(char), '08b') for char in string))
                break
            except:
                print('\033[91mПроизошла ошибка!\033[0m\n\n')
    elif type == '2':
        while True:
            binary_string = str(input('\n\n         Введите бинарный код > '))
            if binary_string == 'break':
                break
            try:
                print('         \033[92m[DECODE]\033[0m ', end='')
                print("".join([chr(int(byte, 2)) for byte in [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]]))
                break
            except:
                print('\033[91mПроизошла ошибка!\033[0m\n\n')
    elif type == 'break':
        quit()
    else:
        print('\033[91m[DECODE] Ошибка! Используйте 1 или 2\033[0m\n\n')
