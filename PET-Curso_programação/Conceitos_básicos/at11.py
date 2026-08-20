"""Crie um programa que receba uma temperatura em Celsius e,
 considerando as seguintes fórmulas K=C+273 e F=1,8C+32,
 exiba a temperatura lida usando as escalas Kelvin (K) e Fahrenheit (F)."""


temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))

kelvin = temperatura_celsius + 273
fah = 1.8*temperatura_celsius + 32

print(f"A temperatura {temperatura_celsius}°C em Kelvin e Fahrenheit é: {kelvin:.1f}K, {fah:.1f}°F")