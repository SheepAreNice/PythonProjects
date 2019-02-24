#! python3

print('Enter a time in seconds and the calculator will tell you that time broken into days, hours, minutes, and seconds.')

timeInput = int(input('> '))

seconds = str(int(((timeInput % 86400) % 3600) % 60))
minutes = str(int(((timeInput % 86400) % 3600) / 60))
hours = str(int((timeInput % 86400) / 3600))
days = str(int(timeInput / 86400))

print(days + ' day(s), ' + hours + ' hour(s), ' + minutes + ' minute(s), ' + seconds + ' second(s).')
 # Testing GitHub edit
