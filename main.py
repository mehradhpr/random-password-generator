import random

state = 'running'

while state == 'running':

    user_input = input('Enter "g" to generate a random password or "e" to quit: ')
    if user_input == 'e':
        break
    elif user_input == 'g':
        # 2 uppercase letters from A to Z,
        first_upper_letter = chr(random.randint(65, 91))
        second_upper_letter = chr(random.randint(65, 91))

        # 2 lowercase letters from a to z,
        first_lower_letter = chr(random.randint(97, 122))
        second_lower_letter = chr(random.randint(97, 122))

        # 2 digits from 0 to 9,
        first_digit = chr(random.randint(48, 57))
        second_digit = chr(random.randint(48, 57))

        # 2 punctuation signs such as !, ?, “, # etc.
        punctuation_list = list()

        for i in range(33, 48):
            punctuation_list.append(i)

        for i in range(58, 65):
            punctuation_list.append(i)

        for i in range(91, 97):
            punctuation_list.append(i)

        for i in range(123, 127):
            punctuation_list.append(i)

        first_p = chr(random.choice(punctuation_list))
        second_p = chr(random.choice(punctuation_list))

        password = list()

        password.extend([first_upper_letter, second_upper_letter, first_lower_letter, second_lower_letter,
                         first_digit, second_digit, first_p, second_p])

        random.shuffle(password)

        print(''.join(password))

    else:
        print('ERROR ---> Please Enter a valid character("e"/"g")\n')
