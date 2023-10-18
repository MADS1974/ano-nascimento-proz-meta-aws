import datetime

def obter_ano_valido():
    while True:
        try:
            ano = int(input("Digite o ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano <= 2021:
                return ano
            else:
                print("Ano fora do intervalo válido.")
        except ValueError:
            print("Ano inválido. Por favor, insira um número válido.")

def calcular_idade(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade

nome = input("Digite seu nome completo: ")
ano_nascimento = obter_ano_valido()
idade = calcular_idade(ano_nascimento)

print(f"Nome: {nome}")
print(f"Idade em 2022: {idade} anos")
