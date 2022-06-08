dis = float(input('Digite uma distância em metros: '))
km = dis / 1000
hm = dis / 100
dam = dis / 10
dm = dis *10
cm = dis * 100
mm = dis * 1000
print(f'{dis} metros corresponde a {km} quilômetros.')
print(f'{dis} metros corresponde a {hm} hectômetros.')
print(f'{dis} metros corresponde a {dam} decâmetros')
print(f'{dis} metros corresponde a {dm} decímetros.')
print(f'{dis} metros corresponde a {cm} centímetrs.')
print(f'{dis} metros corresponde a {mm} milímetros.')