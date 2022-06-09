from math import sin, cos, tan, radians
ang = float(input('Digite um ângulo: '))
s = sin(radians(ang))
c = cos(radians(ang))
t = tan(radians(ang))
print(f'O ângulo de {ang}° tem o SENO de: {s}°')
print(f'O ângulo de {ang}° tem o COSSENO de: {c}°')
print(f'A ângulo de {ang}° tem a TANGENTE de: {t}°')
