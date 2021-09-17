class NotNameError(Exception):
    def __init__(self, text):
        self.text = text

class NotEmailError(Exception):
    def __init__(self, point):
        self.point = point



registrations_good_log = []
registrations_bad_log = []

with open('G:\\Data sainse\\registrations_.txt', 'r', encoding='utf-8') as date:
    for line in date:
        line = line[:-1]
        try:
            name, mail, age = line.split(' ')
            if name.isalpha():
                pass
            else:
                raise NotNameError('the name field contains more than just letters:')
            if '@' in mail and '.' in mail:
                pass
            else:
                raise NotEmailError('the email field does NOT contain @ and .(point):')

            try:
                age = int(age)
                if 10 <= age <= 99:
                    pass
                else:
                    raise ValueError('the age field is NOT a number between 10 and 99')
            except ValueError as exc:
                registrations_bad_log.append(f'ошибка возраст не соответствует,{exc}, в строке {line}')

        except ValueError as exc:
            registrations_bad_log.append(f'ошибка ввода аргументов,{exc}, в строке {line}')
        except NotNameError as exc:
            registrations_bad_log.append(f'ошибка имени,{exc}, в строке {line}')
        except NotEmailError as exc:
            registrations_bad_log.append(f'ошибка эл.почты,{exc}, в строке {line}')

        else:
            registrations_good_log.append(line)



print(registrations_bad_log)
print(registrations_good_log)

with open('registrations_bad_log.log', 'w', encoding='utf8') as file_1:
    for listitem in registrations_bad_log:
        file_1.write('%s\n' % listitem)

with open('registrations_good_log.log', 'w', encoding='utf8') as file_2:
    for listitem in registrations_good_log:
        file_2.write('%s\n' % listitem)
