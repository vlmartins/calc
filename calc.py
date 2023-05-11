def main():
    '''Método que inicia a calculadora, recebe os valores por input do usuário e retorna o resultado da operação matemática desejada.'''
    ligada = True
    valor = 0
    print('Bem vindo a calculadora')
    print('Digite um número ou operador matemático')
    while ligada:
        entrada = input()
        if entrada == 'sair':
            ligada = False
        elif entrada == '+':
            try:
                valor += int(input())
            except: 
                print('Err')
        elif entrada == '-':
            try:
                valor -= int(input())
            except:
                print('Err')
        elif entrada == '*':
            try:
                valor *= int(input())
            except:
                print('Err')
        elif entrada == '/':
            try:
                valor /= int(input())
            except:
                print('Err')
        elif entrada == 'c' or entrada == 'C':
            valor = 0
        else:
            try:
                valor = int(entrada)
            except: 
                print('Err')
        if ligada:
            print(f"Total {valor}")
        

if __name__ == '__main__':
    main()
