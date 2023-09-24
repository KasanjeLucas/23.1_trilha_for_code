BASE_DIR = '.\Exercício 0\Parte 2\Figurinhas.txt'

def main() -> None:
    def read_and_cut(file: str) -> list:
        with open(file, "r", encoding = 'UTF-8') as text:
            return (text.read()).split(', ')
        
    figures = read_and_cut(BASE_DIR)

    figures.sort(key=ascii)

    print(*figures) # Coloquei o texto meio direto mesmo, para não complicar demais o código
    print('\n')

main()