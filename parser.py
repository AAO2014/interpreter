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
        if i != len(text) - 2 and text[i] == '+' and text[i + 1].isdigit():
            i += 1
            continue
        elif i != len(text) - 2 and text[i] == '-' and text[i + 1].isdigit():
            negative_digit = True
        elif text[i] in '+-*/' and start_part:
            part = text[i]
            start_part = False
        elif text[i].isdigit():
            part += text[i]
            start_part = False
        elif text[i] == '(':
            left_index = i + 1
            right_index = left_index + find_right_bracket(text[left_index - 1:])
            part = text[left_index:right_index - 1]
            i = right_index
            start_part = False
        elif text[i] != ' ':
            part += text[i]
        else:
            start_part = False
        i += 1
        if not start_part and part:
            if part.isdigit():
                part = part if not negative_digit else f'-{part}'
                negative_digit = False
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
        elif not item.isdigit() or ' ' in item:
            item = parser(item)
        else:
            recurced_result = do_split(item)
            if recurced_result:
                result.extend(recurced_result)
            continue

        result.append(item)
    return result
