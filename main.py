print('шифр Цезаря;')
from Cesar import Cesar

permuter = Cesar('a', 'z', 1)

to_encode = "abcd"
print('start:', to_encode)
encoded = permuter.encode(to_encode)
print('encoded:', encoded)
decoded = permuter.decode(encoded)
print('decoded:', decoded)

print()
print('лозунговый шифр;')
from Slogan import Slogan

permuter = Slogan('a', 'z', 'hese')

to_encode = "abcd"
print('start:', to_encode)
encoded = permuter.encode(to_encode)
print('encoded:', encoded)
decoded = permuter.decode(encoded)
print('decoded:', decoded)


print()
print('полибианский квадрат;')
from Box import Box

permuter = Box('а', 'я', 6)

to_encode = "привет"
print('start:', to_encode)
encoded = permuter.encode(to_encode)
print('encoded:', encoded)
print('box:')
permuter.print()



print()
print('шифрующая система Трисемуса;')
from Tresem import Tresem

permuter = Tresem('а', 'я', 'зяяяб', 6)

to_encode = "привет"
print('start:', to_encode)
encoded = permuter.encode(to_encode)
print('encoded:', encoded)
print('box:')
permuter.print()


print()
print('Playfair')
from Playfair import Playfair

permuter = Playfair('а', 'я', 'зяяяб', 6, 'Я')

to_encode = "приветэю"
print('start:', to_encode)
encoded = permuter.encode(to_encode)
print('encoded:', encoded)
print('box:')
permuter.print()