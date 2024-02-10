# Pyramid Decoder Challenge
# mat 10feb24
import os

def print_banner(banner):
    print(f'{banner}')

def decode (message_file_name):
    message_file_path = os.path.join('assets', message_file_name)
    #print(f'message_file_path: {message_file_path}')

    # open & read the message file
    with open(message_file_path, 'r') as file:
        message = file.read()
    # message will be key, word pairs separated by new line chars
    #print(message)

    # create dictionary to store key, word pairs
    message_dict = {}
    # split by new line char \n
    message_list = message.split('\n')
    #print(message_list)
    for line in message_list:
        #print(line)
        if len(line) > 2:
            # split by space char into key, word pairs
            key, word = line.split(' ')
            #print(f'key: {key}, word: {word}')
            # add key, word to dictionary
            message_dict[key] = word
        #else:
            #print('empty line')

    #print(message_dict)

    # decode into clear message
    clear_message_decode = ""
    step = 1
    current_key = '1'
    while current_key in message_dict:
        #print(f'current_key: {current_key}')
        current_word = message_dict[current_key]
        #print(f'current_word: {current_word}')
        clear_message_decode += " " + current_word
        step += 1
        key_int = int(current_key)
        current_key = str(key_int + step)

    # return decoded message
    print(f'clear_message_decode: {clear_message_decode}')
    return clear_message_decode


if __name__ == '__main__':
    print_banner('Pyramid Decoder Challenge starts...')

    # set path to message_text file
    message_file_name = "coding_qual_input.txt"
    # decode message
    decode(message_file_name)

    print(f'Pyramid Decoder Challenge ends...')




