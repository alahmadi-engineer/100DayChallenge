#write program to take tips

print('Welcome to the tip calculator.')
Total = float(input('What was the total bill? '))
people = float(input('How Many people to split the bill? '))
percentage = float(input('what percentage tip would you like to give? 10, 12, or 15? '))
pay = (Total + ((Total)*(percentage/100)))/people
print('Each person should pay: {}'.format(pay))