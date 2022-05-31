import os


if __name__ == "__main__":
    while True:
        os.system('cls')
        print("Binary Converter by Steve D. J.\n")
        _from = input(">>>From (B: binary, D: decimal, H: hexadecimal): ")
        _to = input(">>>To (B: binary, D: decimal, H: hexadecimal): ")
        if _from == "B" and _to == "D":
            while True:
                number = input(">>>enter a binary value or 'RSM' to reselect mode: ")
                if number == "RSM":
                    break
                else:
                    not_bin_flag = 0
                    for word in number:
                        if word not in ['0', '1']:
                            not_bin_flag = 1
                            break
                    if not_bin_flag != 0:
                        print("Please input a binary value!")
                    else:
                        number = int(number)
                        decimal = 0
                        base = 1
                        temp = number
                        while temp:
                            last = temp % 10
                            temp = int(temp / 10)
                            decimal += last * base
                            base = base * 2
                        print("Decimal: ", decimal)
        elif _from == "B" and _to == "H":
            while True:
                number = input(">>>enter a binary value or 'RSM' to reselect mode: ")
                if number == "RSM":
                    break
                else:
                    not_bin_flag = 0
                    for word in number:
                        if word not in ['0', '1']:
                            not_bin_flag = 1
                            break
                    if not_bin_flag != 0:
                        print("Please input a binary value!")
                    else:
                        hexadecimal = ''
                        ct = 0
                        base = 1
                        temp = 0
                        hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
                        for i in range(len(number)-1, -1, -1):
                            if ct < 4:
                                temp += int(number[i]) * base
                                base *= 2
                                ct += 1
                            else:
                                hexadecimal = hex_list[temp] + hexadecimal
                                ct = 0
                                base = 1
                                temp = 0
                                temp += int(number[i]) * base
                                base *= 2
                                ct += 1
                        if temp != 0:
                            hexadecimal = hex_list[temp] + hexadecimal
                        print("Hexadecimal: ", hexadecimal)
        elif _from == "D" and _to == "B":
            while True:
                number = input(">>>enter a number or 'RSM' to reselect mode: ")
                if number == "RSM":
                    break
                else:
                    not_num_flag = 0
                    for word in number:
                        if word not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                            not_num_flag = 1
                            break
                    if not_num_flag != 0:
                        print("Please input a number!")
                    else:
                        number = int(number)
                        if number == 0:
                            print("Binary: ", 0)
                        else:
                            a = []
                            i = 0
                            while number > 0:
                                a.append(number % 2)
                                number = int(number / 2)
                                i += 1
                            b = i - 1
                            output = ''
                            while b >= 0:
                                output += str(a[b])
                                b -= 1
                            print("Binary: ", output)
        elif _from == "D" and _to == "H":
            while True:
                number = input(">>>enter a number or 'RSM' to reselect mode: ")
                if number == "RSM":
                    break
                else:
                    hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
                    not_num_flag = 0
                    for word in number:
                        if word not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                            not_num_flag = 1
                            break
                    if not_num_flag != 0:
                        print("Please input a number!")
                    else:
                        number = int(number)
                        if number == 0:
                            print("Hexadecimal: ", 0)
                        else:
                            a = []
                            i = 0
                            while number > 0:
                                a.append(number % 16)
                                number = int(number / 16)
                                i += 1
                            b = i - 1
                            output = ''
                            while b >= 0:
                                output += str(hex_list[a[b]])
                                b -= 1
                            print("Hexadecimal: ", output)
        elif _from == "H" and _to == "B":
            while True:
                number = input(">>>enter a hexadecimal or 'RSM' to reselect mode: ")
                if number == "RSM":
                    break
                else:
                    hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
                    not_hex_flag = 0
                    for word in number:
                        if word not in hex_list:
                            not_hex_flag = 1
                            break
                    if not_hex_flag != 0:
                        print("Please input a hexadecimal!")
                    else:
                        bin = ''
                        for word in number:
                            value = hex_list.index(word)
                            a = []
                            i = 0
                            while value > 0:
                                a.append(value % 2)
                                value = int(value / 2)
                                i += 1
                            b = i - 1
                            output = ''
                            while b >= 0:
                                output += str(a[b])
                                b -= 1
                            while len(output) < 4:
                                output = '0' + output
                            bin += output
                        print("Binary: ", bin)
        elif _from == "H" and _to == "D":
            while True:
                number = input(">>>enter a hexadecimal or 'RSM' to reselect mode: ")
                if number == "RSM":
                    break
                else:
                    hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
                    not_hex_flag = 0
                    for word in number:
                        if word not in hex_list:
                            not_hex_flag = 1
                            break
                    if not_hex_flag != 0:
                        print("Please input a hexadecimal!")
                    else:
                        base = 1
                        decimal = 0
                        for i in range(len(number)-1, -1, -1):
                            value = hex_list.index(number[i])
                            decimal += value * base
                            base *= 16
                        print("Decimal: ", decimal)
        else:
            pass
