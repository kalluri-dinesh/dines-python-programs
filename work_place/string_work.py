# String: Strings are sequences of characters.
# 2. Python strings are "immutable" which means they cannot be changed after they are created.
# 3. To create a string, put the sequence of characters inside either single quotes, double
# quotes, or triple quotes and then assign it to a variable.
# access characters from String, use indexing or slicing
aa="KRISHNA reddy"
# print(type(aa))
# print(dir(aa))


#'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find',
# 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit',
# 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper',
# 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix',
# 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip',
# 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

cc=aa.capitalize()   #Converts the first character of a string into Upper case
print(cc)            #Krishna reddy from nellore
dd =aa.casefold()    #Returns casefolded string. Converts Uppercase to lowercase.
print(dd)            #krishna reddy from nellore
ff=aa.center(17)     #Returns a new copy of the string after centering it in a field of length width
print(ff)
