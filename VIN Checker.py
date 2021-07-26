dict_base = {'A' : 1, 'a' : 1,
             'B' : 2, 'b' : 2,
             'C' : 3, 'c' : 3,
             'D' : 4, 'd' : 4,
             'E' : 5, 'e' : 5,
             'F' : 6, 'f' : 6,
             'G' : 7, 'g' : 7,
             'H' : 8, 'h' : 8,
             'I' : None, 'i' : None,
             'J' : 1, 'j' : 1,
             'K' : 2, 'k' : 2,
             'L' : 3, 'l' : 3,
             'M' : 4, 'm' : 4,
             'N' : 5, 'n' : 5,
             'O' : None, 'o' : None,
             'P' : 7, 'p' : 7,
             'Q' : None, 'q' : None,
             'R' : 9, 'r' : 9,
             'S' : 2, 's' : 2,
             'T' : 3, 't' : 3,
             'U' : 4, 'u' : 4,
             'V' : 5, 'v' : 5,
             'W' : 6, 'w' : 6,
             'X' : 7, 'x' : 7,
             'Y' : 8, 'y' : 8,
             'Z' : 9, 'z' : 9}

weight = [8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2]

def check_vin(number):
    if len(number) != 17:
        return False
    else:
        calc_list = []
        for i in number:
            try: int(i)
            except ValueError:
                if dict_base[i] == None: return False
                elif dict_base[i] != None: calc_list.append(int(dict_base[i]))
            else: calc_list.append(int(i))
        for i in range(0, len(weight)):
            calc_list[i] = calc_list[i] * weight[i]
        try: int(number[8])
        except ValueError:
            if sum(calc_list) % 11 == 10 and number[8] == ('X' or 'x'): return True
            elif str(sum(calc_list) % 11) == dict_base[number[8]]: return True
            else: return False
        else:
            if str(sum(calc_list) % 11) == number[8]: return True
            else: return False