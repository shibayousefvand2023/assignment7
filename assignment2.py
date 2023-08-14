name = ('Wellcome to my word count program')
print(name)
def word_cont(str):
    word_cont = len(str.split())
    print('number words:', word_cont)

print('sentence do you like:')
str=input()
word_cont(str)