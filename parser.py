from const import HASH_MAP


class Symbol:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def __str__(self):
        return self.name


class Cons(list):
    pass


def find_right_bracket(text):
    left_bracket_counter = 0
    rigth_bracket_counter = 0
    for index, char in enumerate(text):
        if char == '(':
            left_bracket_counter += 1
        elif char == ')':
            rigth_bracket_counter += 1
            if left_bracket_counter == rigth_bracket_counter:
                return index
    return -1


def do_split(text):
    text = text.replace('\n', '')
    result = []
    part = ''
    i = 0
    start_part = True
    negative_digit = False
    while i < len(text):
        if text[i:].lower().startswith('cons'):
            result.append('cons')
            i += 4
            continue
        elif text[i] == '+' and text[i + 1].isdigit():
            start_part = True
            i += 1
            continue
        elif text[i] == '-' and text[i + 1].isdigit():
            start_part = True
            negative_digit = True
        elif text[i] in '+-*/' and start_part:
            part = text[i]
            start_part = False
        elif text[i].isdigit():
            start_part = True
            part += text[i]
        elif text[i] == '(':
            left_index = i + 1
            right_index = left_index + find_right_bracket(text[left_index - 1:])
            part = text[left_index:right_index - 1]
            i = right_index
            start_part = False
        elif text[i].isalpha():
            part += text[i]
        elif text[i] != ' ':
            part += text[i]
        elif text[i] == ' ':
            start_part = False
        i += 1
        if not start_part and part or i == len(text):
            if part.isdigit():
                part = f'-{part}' if negative_digit else part
                negative_digit = False
            start_part = True
            result.append(part)
            part = ''
    return result


def parser(script: str) -> list:
    result = []
    for item in do_split(script.strip()):
        item = item.strip()
        if item in HASH_MAP:
            item = HASH_MAP[item]
        elif item.isdigit() or len(item) > 1 and item[0] == '-' and item[1:].isdigit():
            item = int(item)
        elif item.isalpha():
            item = Symbol(item)
        elif not item.isdigit() or ' ' in item:
            item = parser(item)
        else:
            sub_result = do_split(item)
            if sub_result:
                result.extend(sub_result)
            continue

        result.append(item)
    return result
