def valid_phone_number(phone_number):
    t_number = ''
    if len(phone_number) != 14:
        return False
    else:
        if phone_number[0] == '(' and phone_number[4] == ')':
            if phone_number[5] == ' ' and phone_number[9] == '-':
                for i in phone_number:
                    try: int(i)
                    except ValueError: pass
                    else: t_number += t_number.join(i)
                try: int(t_number)
                except ValueError: return False
                else: 
                    if len(str(t_number)) == 10 : return True
                    else: return False
            else: return False
        else: return False