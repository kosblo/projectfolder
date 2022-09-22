""""def whatisyourname():
    print(f'my name is korede.')
whatisyourname()"""
"""'def whatisyourname(name):
    print(f'my name is {name}.')
whatisyourname('dayo')
whatisyourname('ade')
whatisyourname('david')"""

calon=True
while calon:
    firstnum=int(input("enter a number"))
    option=input('choose an option(+,-,/,*)!')
    secondnum=int(input('enter a number'))
   

def calculator(a,b,c):
    if  b =='+':
        result= int(a)+int(c)
    elif b =='-':
        result=int(a)-int(c)
    elif b =='/':
        result =int(a)/int(c)
    else:
        result=int(a)*int(c)
        print(result)
    calculator(firstnum,option,secondnum)
    

