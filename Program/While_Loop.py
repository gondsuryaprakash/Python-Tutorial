# i=1
# while i<=5:
#     print('*'* i)
#     i+=1
# print('Done')
'''Guesing Game'''
# secretNumber=9
# i=0
# gl=3
# while i<gl:
#     guess=int(input('Guess: '))
#     i+=1
#     if guess==secretNumber:
#         print('Nice Played')
#         break
#     else:
#         print('Try once more!')
# else:
#     print('Sorry you failed')
'''Commond'''
commond=''
is_Started=False
is_Stopped=False
while True:
    commond=input('> ')
    if commond.lower()=='start':
        if is_Started:
            print('Car is already started')
        else:
            is_Started=True
            print('Ready to go')


    elif commond.lower()=='stop':
        if is_Stopped:
            print('Car is already stopped')
        else:
            is_Stopped=True
            is_Started=False
            print('Car stopped')

    elif commond.lower()=='help':
        print('''
        start-to start the car
        stop-to stop the car 
        quit-to quit
        ''')
    elif commond.lower()=='quit':
        break
    else:
        print("Sorry we don't understand")






