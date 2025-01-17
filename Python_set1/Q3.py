''' Write an output/error for the below program. '''

'''a. a = 10
b = 20
print(a and b)
print(a or b)'''

a = 10
b = 20
print(a and b) # output : 20 ''' variable b's value printing because of and operator '''
#print(a,b)
print(a or b) # output : 10 ''' variable a's value printing because of or operator '''

'''b. if False:
print("It is False")
else:
print("It is True")'''

if False:
    print("It is false.")
else:
    print("It is True.") # output : It is True.


''' c. if [ ]:
print("It is Blank")
else:
print("It is Something else") '''     

if []:
    print("It is blank.")
else:
    print("It is something else") # output : It is something else

''' d. if [ [ ] ]:
print("It is Blank")
else:
print("It is Something else")
 '''    
if [ [ ] ]:
    print("It is blank")
else:
    print("It is something else.") # output : It is blank

    
''' e. if [ False ]:
print("It is Blank")
else:
print("It is Something else")
'''

if [ False ]:
    print("It is blank")
else:
    print("It is something else.") # output : It is blank
    
''' f. type(range) '''
a = range(1,10)
print(type(a)) # output : <class 'range'>

