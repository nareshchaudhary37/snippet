# coding=utf-8


class ChronologyNumber(object):
    MAX_LENGTH_NUMBER = 6
    ORD_VALUE = 64

    def __char_to_number(self, string_number):
        number = []
        for char in list(string_number):
            num = ord(char) - self.ORD_VALUE
            if num == 26:
                break
            number.append(num)
        return number

    def __number_to_char(self, number):
        string_number = ""
        for num in number:
            string_number += chr(num + self.ORD_VALUE)
        return string_number

    def get_next_number(self, current_string_number):
        new_num = self.__char_to_number(current_string_number)
        new_num[-1] += 1
        missing = self.MAX_LENGTH_NUMBER - len(new_num)
        return self.__number_to_char(new_num) + "A"*missing