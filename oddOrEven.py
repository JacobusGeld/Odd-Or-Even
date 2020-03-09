#Get user input
print('Enter a number and I will tell you if it is odd or even')
run = True
#Loop
while run:
    answer = input('Number: ')
    try:
        if int(answer)%2 == 0: 
            print(answer, 'is an even number')
        else: 
            print(answer, 'is an odd number')
    except ValueError:
        if answer=='quit':
            print('Thanks for playing!')
            run = False
            break
        else:
            print('Please only use whole numbers or type "quit" to quit')
