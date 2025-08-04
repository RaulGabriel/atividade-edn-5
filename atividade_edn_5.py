# =================================
# ATIVIDADE PRÁTICA 05 - EDN
# =================================
import datetime

def calcular_gorjeta():
    """
    1 - Cria uma função que calcule a gorjeta a ser deixada em um restaurante.
    """
    print("\n=== 1 - Calculadora de Gorjeta ===")
    try:
        valor_conta = float(input("Digite o valor total da conta: R$ "))
        porcentagem = float(input("Digite a porcentagem da gorjeta (ex: 15 para 15%): "))
        valor_gorjeta = (valor_conta * porcentagem) / 100
        print(f"O valor da gorjeta é: R$ {valor_gorjeta:.2f}")

    except ValueError:
        print("Erro: Por favor, digite valores numéricos válidos.")

def verificar_palindromo():
    """
    2- Cria uma função que verifique se uma palavra ou frase é um palíndromo.
    """
    print("\n=== 2 - Verificador de Palíndromo ===")
    frase = input("Digite uma palavra ou frase para verificar: ")
    frase_limpa = frase.lower().replace(' ', '')
    frase_invertida = frase_limpa[::-1]

    if frase_limpa == frase_invertida:
        print("Resultado: Sim")
    else:
        print("Resultado: Não")

def calcular_preco_final():
    """
    3 - Cria um programa que serve para calcular o preço final de um produto.
    """
    print("\n=== 3 - Calculadora de Preço Final com Desconto ===")
    try:
        preco_original = float(input("Digite o preço original do produto: R$ "))
        desconto_percentual = float(input("Digite o percentual de desconto (ex: 20 para 20%): "))
        valor_desconto = (preco_original * desconto_percentual) / 100
        preco_final = preco_original - valor_desconto
        print(f"O preço final com desconto é: R$ {preco_final:.2f}")

    except ValueError:
        print("Erro: Por favor, digite valores numéricos válidos.")

def calcular_dias_de_vida():
    """
    4 - Cria um programa que calcule a quantos dias um indivíduo está vivo.
    """
    print("\n=== 4 - Calculadora de Dias de Vida ===")
    try:
        data_nasc_str = input("Digite sua data de nascimento no formato DD/MM/AAAA: ")
        data_nascimento = datetime.datetime.strptime(data_nasc_str, "%d/%m/%Y").date()
        hoje = datetime.date.today()
        diferenca = hoje - data_nascimento
        print(f"Você está vivo há {diferenca.days} dias.")

    except ValueError:
        print("Erro: Formato de data inválido. Use DD/MM/AAAA e uma data válida.")


def menu_principal_05():
    while True:
        print("\n" + "="*45)
        print("Atividade Prática 05 - EDN")
        print("\n" + "-"*26)
        print("Opções:")
        print("1 - Calculadora de Gorjeta")
        print("2 - Verificador de Palíndromo")
        print("3 - Calculadora de Preço Final com Desconto")
        print("4 - Calculadora de Dias de Vida")
        print("5 - Sair")
        print("="*45)

        try:
            opcao = int(input("Escolha uma opção (1-5): "))

            if opcao == 1:
                calcular_gorjeta()
            elif opcao == 2:
                verificar_palindromo()
            elif opcao == 3:
                calcular_preco_final()
            elif opcao == 4:
                calcular_dias_de_vida()
            elif opcao == 5:
                print("Encerrando o programa.")
                break
            else:
                print("Opção inválida!")
        except ValueError:
            print("Digite uma opção numérica válida.")


if __name__ == "__main__":
    menu_principal_05()