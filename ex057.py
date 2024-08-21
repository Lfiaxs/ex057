s = str(input('Informe seu sexo? [M/F] ')).strip().upper() [0]
while s not in 'MmFf':
    print('OPÇÃO INVÁLIDA!')
    s = str(input('Por favor, informe seu sexo. [M/F] ')).upper()
print('Sexo {} registrado com sucesso'.format(s))
print('FIM')

