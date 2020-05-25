# is_Hot=True
# is_cold=False
# if is_Hot:
#     print("It's a hot day")
#     print('Drinh a plety water')
# elif is_cold:
#     print('Its a cold day')
#     print('Wear the warm cloths')
# else:
#     print('Enjoy your day')
# is_good=False
# is_Bad=True
# price=1000000
# if is_good:
#     print(price-price*0.1)
# elif is_Bad:
#     print(price-price*0.2)

'''And OR operator'''
# is_HighIncome=True
# is_goodIncome=False
# has_CrimminalRecord=False
# if is_HighIncome and not has_CrimminalRecord:
#     print(f'Eligible for Loan')
'''Comparision Operator'''
# temp=30
# if temp>30:
#     print('It is not a hot day')
# else:
#     print('Its not hot Day cool')
# name='Surya'
# if len(name)<3:
#     print('Name must be atleast 3 character')
# elif len(name)>50:
#     print('Name can be maximum of 50 character')
# else:
#     print('GOod Name')
weight=int(input('Weight: '))
unit=input('(L)bs or (K)g: ')
if unit.upper()=='L':
    print(weight*0.45)
elif unit.upper()=='K':
    print(weight/0.45)
