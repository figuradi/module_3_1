calls = 0


def count_calls():
    global calls
    calls = calls + 1


def string_info(string):
    global calls
    a = (len(string), string.upper(), string.lower())
    print(a)
    count_calls()


def is_contains(string, list_to_search):
    global calls
    lowercase_list = [x.lower() for x in list_to_search]
    string = string.lower()

    if string in lowercase_list:
        print(True)
    else:
        print(False)

    count_calls()


string_info('Anaconda')
string_info('Python')
string_info('Dmitry Igorevich')
is_contains('Python', ['Anaconda', 'Oleg', 'Dmitry'])
is_contains('dmitry', ['Contains', 'bAnaNas', 'DMitry'])
is_contains('TarAnTinO', ['Demon', 'AntOn', 'DMitry', 'ViaCHeslav', 'taRantINo'])

print(calls)