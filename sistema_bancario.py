from typing import Final
import textwrap

def menu() -> str:
    menu: str = """
    ==========MENU==========
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [q]\tSair
=>"""
    return input(textwrap.dedent(menu))

def depositar(saldo: float, valor: float, extrato: list[str], /) -> tuple[float, list[str]]:
    if valor > 0:
        saldo += valor
        extrato.append(f'Depósito:\tR$ {valor:.2f}')
        print('Depósito realizado com sucesso!')
    else:
        print('O valor precisa ser positivo!')

    return saldo,extrato

def sacar(*,saldo: float, valor: float, extrato:list[str],limite:float,numero_saques:int,limite_saques:int) -> tuple[float,list[str],int]:
    if valor > saldo:
        print("saldo insuficiente!")

    elif valor > limite:
        print("limite diario excedido!")

    elif numero_saques >= limite_saques:
        print('Limite de saques diários excedido!')

    elif valor <=0:
        print("O valor precisa ser positivo!")

    else:
        saldo -= valor
        extrato.append(f'Saque:\t\tR$ {valor:.2f}')
        numero_saques += 1
        print("saque realizado com sucesso!")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo:float,/,*,extrato:list[str]) -> None:
    print('\n==========EXTRATO===========')
    print('\n'.join(extrato) if extrato else 'Nao foram realizadas movimentaçoes!')
    print(f'\nSaldo:\t\tR$ {saldo:.2f}')
    print('=======================')

def main() -> None:
    LIMITE_SAQUES: Final = 5
    saldo: float = 0
    limite: float = 500
    extrato: list[str] = []
    numero_saques:int = 0

    while True:
        opcao: str = menu()

        match opcao:
            case 'd':
                valor: float = float(input('Digite o valor a ser depositado: '))
                saldo, extrato = depositar(saldo, valor, extrato)

            case 's':
                valor: float = float(input('Digite um valor a ser sacado: '))

                saldo,extrato,numero_saques = sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES
                )

            case 'e':
                exibir_extrato(saldo, extrato=extrato)

            case 'q':
                print('Encerrando acesso...')
                break

            case default:
                print('opção invalida!')


main()