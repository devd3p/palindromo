def palindromo(palavra):
    '''Palíndromos'''
    palavra = input('Digite uma palavra: ')
    if palavra.lower == palavra[-1::-1]:
        return f'{palavra} é um palíndromo.'
    else:
        return f'{palavra} não é um palíndromo.'