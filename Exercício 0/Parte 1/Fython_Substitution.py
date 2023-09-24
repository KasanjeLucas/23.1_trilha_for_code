BASE_DIR = '.\Exercício 0\Parte 1\Texto.txt'

def main() -> None:
    def read_and_cut(file: str) -> list:
        with open(file, "r", encoding = 'UTF-8') as text:
            return (text.read()).split(' ')


    text = read_and_cut(BASE_DIR)

    for i in range(len(text)):
        if text[i] == 'Python':
            text[i] = 'Fython'

    text_together = " ".join(text)

    print (text_together)

if __name__ == '__main__':
    main()
