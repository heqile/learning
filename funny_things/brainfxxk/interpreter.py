code_position = 0
data_index = 0
data =  256 * [0]
start_if_position = 0
skip = False


def move_left():
    global data_index, skip
    if skip: return
    data_index -= 1
    data_index %= 256

def move_right():
    global data_index, skip
    if skip: return
    data_index +=  1
    data_index %= 256

def decrease():
    global data_index, data, skip
    if skip: return
    data[data_index] -= 1
    data[data_index] %= 256
    
def increase():
    global data_index, data, skip
    if skip: return
    data[data_index] += 1
    data[data_index] %= 256

def start_if():
    global code_position, skip, start_if_position
    if data[data_index] == 0:
        skip = True
    else:
        start_if_position = code_position

def end_if():
    global code_position, skip, start_if_position
    if skip:
        skip = False
    else:
        code_position = start_if_position - 1

def print_char():
    global data_index, data, skip
    if skip: return
    print(chr(data[data_index]), end="")

def input_char():
    global data_index, data, skip
    if skip: return
    user_input = input("please input one character:")[0]
    data[data_index] = ord(user_input)

commands = {
    "<": move_left,
    ">": move_right,
    "-": decrease,
    "+": increase,
    "[": start_if,
    "]": end_if,
    ".": print_char,
    ",": input_char,
}

def interprete(code):
    global code_position, skip
    while(len(code) != code_position):
        command = code[code_position]
        code_position += 1
        commands[command]()
    print()


def main():
    #code = "++++++++[->++++++++<]>+."
    #code = ",."
    interprete(code)


if __name__ == "__main__":
    main()