#Criar uma calculadora que números ou operadores matemáticos e realize a operação matemática desejada, com a possibilidade de ver resultado no final.

def main():
    '''Calculadora que realiza operações matemáticas'''
    ligada = True
    valor = 0
    print('Bem vindo a calculadora')
    print('Digite um número ou operador matemático')
    while ligada:
        entrada = input()
        if entrada == 'sair':
            ligada = False
        elif entrada == '+':
            valor += int(input())
        elif entrada == '-':
            valor -= int(input())
        elif entrada == '*':
            valor *= int(input())
        elif entrada == '/':
            valor /= int(input())
        elif entrada == 'c' or entrada == 'C':
            valor = 0
        else:
            try:
                valor = int(entrada)
            except: 
                print('Err')
        print(f"Total {valor}")
        

if __name__ == '__main__':
    main()