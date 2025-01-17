# Write output for the below statements, if you find any error please write the error.
# -> [] * 3
# -> ('a', 'b', 'c') * 2
# Q1. -> (2) ** 2
#     -> [{}] * 2
#     -> {3:1} * 2
#     -> ‘123’ + 2
#     -> ['a', 'b', 'c'] + ‘rf’
#     -> (2, 4) ** 2
#     -> Assume Z = ['P', 'L', ']' ] and then Z += 'SE'. What will be the output of print(Z)?


print([] * 3) # output : [] ''' list can not be multiply '''

print(('a', 'b', 'c') * 2) # output : ('a', 'b', 'c', 'a', 'b', 'c') ''' All the string in tuple is multiply by 2 times '''

print((2) ** 2) # output : 4 ''' number is square up '''

print([{}] * 2) # output : [{}, {}] ''' There is dictionary in the list so dictionary is multiply by 2 '''

# print({3:1} * 2) # output : TypeError: unsupported operand type(s) for *: 'dict' and 'int'

# print('123' + 2) # output : TypeError: can only concatenate str (not "int") to str ''' It means we can concatenate string to string ('123' + '4') , not string to int '''

# print(['a', 'b', 'c'] + 'rf') # output : TypeError: can only concatenate list (not "str") to list ''' It means we can concatenate list to list ['a', 'b', 'c'] + ['rf'] , not list to str.

# print((2, 4) ** 2) # output : TypeError: unsupported operand type(s) for ** or pow(): 'tuple' and 'int'

Z = ['P', 'L', ']' ]
Z += 'SE'
print(Z) # ['P', 'L', ']', 'S', 'E'] ''' It appends single-single element to the existing list using Addition assignment operator '''

    


