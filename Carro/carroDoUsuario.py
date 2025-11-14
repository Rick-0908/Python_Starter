import random
import Car
import Velocidade

make = input("Digite a marca do carro: ")
model = input("Digite o modelo do carro: ")
year = int(input("Digite o ano do carro: "))
color = input("Digite a cor do seu carro: ")

print(
    f"A marca do seu carro é: {make}, o modelo dele é: {model},o ano dele é: {year}, e a cor dele é: {color}")

guardar_carroUsuario = Car.Carro(make, model, year, color)

variacao_condicaoCarro = random.choice([True, False])

if variacao_condicaoCarro:
    guardar_carroUsuario.drive()
else:
    guardar_carroUsuario.stop()


print("Agora vamos verificar sua velocidade")

velocidade = int(input("Digite sua velocidade atual: "))
combustivel = int(input("Digite seu combustivel: "))

guardar_estatisticas = Velocidade.Estatisticas(velocidade, combustivel)


if guardar_estatisticas.verificacaoVelocidade() and guardar_estatisticas.verificacaoCombustivel():
    guardar_estatisticas.verificacaoVelocidade()
    guardar_estatisticas.verificacaoCombustivel()
    estatisticas = True
else:
    print("Erro")


