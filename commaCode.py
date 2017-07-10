'''
a function that takes a list value as argument
returns a string with all items separated by comma and space
with an 'and' inserted before the last item
'''

def comma_code(a):
    for i in a[:-1]:
        print(i + ', ', end='')
    print('and ' + a[-1])

spam = ['apples', 'bananas', 'tofu', 'cats']
comma_code(spam)

