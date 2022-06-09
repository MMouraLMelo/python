dias = int(input('Dias utilizados: '))
km = float(input('Quilômetros rodados: '))
custo = dias * 60 + km * 0.15
print(f'O total a pagar é R$ {custo} por {dias} dias e {km} Km rodados.')