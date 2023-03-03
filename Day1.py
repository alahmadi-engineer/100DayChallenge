#write program to take input and mix them together

print('Welcome to the Band Name Generator.')
city = input('what is the name of the city you grew up in? \n')
pet = input('what is your pet name? \n')
BandName = city.title() + ' ' + pet.title()
print('Your band name could be {}'.format(BandName))