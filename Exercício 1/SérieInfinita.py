import math

def analisa_infinidade():
    n = 2
    soma = 0
    
    while n < 999999:
        soma += (1/(n*(math.log(n, math.e)**2)))
        n += 1

    print('A soma é finita? Resposta:', math.isfinite(soma))
    print(f'Resultado do somatório de uma série de n = 2 até n = 999999 : {soma}')

if __name__ == '__main__':
    analisa_infinidade()