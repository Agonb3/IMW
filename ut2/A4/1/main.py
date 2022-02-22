dni = int(input('dni:'))
letter = 'TRWAGMYFPDXBNJZSQVHLCKE'
remain = dni % 23

print(f'{dni}{letter[remain]}')