print('Enter TB or GB for the advertised unit:')

# weird anotation, in some cases is not necesary use a variable in the while, just cheking if a
#condition in the while its true or false is enought to satisfy a loop, where you want to make
#a person try again in the conditions
while True:
    unit = input('>').lower()
    if unit == 'tb':
        discrepancy = 1000000000000 / 1099511627776
        break
    elif unit == 'gb':
        discrepancy = 1000000000 / 1073741824
        break
    else :
        print('Invalid option')

print('Enter the advertised capacity: ')
advertised_capacity = float(input('>'))

real_capacity = str(round(advertised_capacity * discrepancy, 2))

print(f"the actual capacity is "+ real_capacity +" "+ unit)
