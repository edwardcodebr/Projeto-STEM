import numpy as np
import math
import matplotlib.pyplot as plt
import sys
import pyttsx3
import time


def tela_carregamento(segundos):
    for i in range(segundos * 10, 0, -1):
        sys.stdout.write("\rCarregando... [{}] {}s".format("." * (i % 4), i/10))
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\rCarregado!        \n")

# Defina o tempo de carregamento em segundos
tempo_carregamento = 3

engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Define a velocidade da voz

def falar(texto, voz='brazil'):
    voices = engine.getProperty('voices')
    for v in voices:
        if 'brazil' in v.id and 'female' in v.id:
            voz = v.id
            break
    engine.setProperty('voice', voz)
    engine.say(texto)
    engine.runAndWait()
    
def menu():
    texto = '''
    bem vindo ao aplicativo de fisica, por favor, entre um valor
    '''
    falar(texto)

def velocidade_carro(distancia, tempo):
    velocidade = distancia / tempo
    print(f"A velocidade do carro é de {velocidade:.2f} km/h.")
    velocidadefalar = f'a velocidade do carro é de {velocidade} quilometros por hora'
    falar(velocidadefalar)

def calcular_trajetoria(v0, theta, gravidade):
    distancia = (v0 ** 2 * np.sin(2 * np.radians(theta))) / gravidade
    altura_maxima = (v0 ** 2 * (np.sin(np.radians(theta))) ** 2) / (2 * gravidade)
    return distancia, altura_maxima

def lei_ohl(volt, amperes):
    resistencia = volt / amperes
    print(f"A resistência é de {resistencia:.2f} Ohms.")
    texto =f'A resistência é de {resistencia:.2f} Ohms'
    falar(texto)

def conversao_f(celsius1):
    fahrenheit = (celsius1 * 9/5) + 32
    print(f"A temperatura em Fahrenheit é de {fahrenheit:.2f} °F.")
    texto = f'f"A temperatura em Fahrenheit é de {fahrenheit:.2f}'
    falar(texto)
    
def conversao_k(celsius2):
    kelvin = celsius2 + 273.15
    print(f"A temperatura em Kelvin é de {kelvin:.2f} K.")
    texto = f"A temperatura em Kelvin é de {kelvin:.2f}"

def conversao_celsius_fahrenheit(fh):
    celsius = (fh - 32) * 5/9
    print(f"A temperatura em Celsius é de {celsius:.2f} °C.")
    texto = f"A temperatura em Celsius é de {celsius:.2f}"
def conversao_celsius_kelvin(klv):
    celsius = klv - 273.15
    print(f"A temperatura em Celsius é de {celsius:.2f} °C.")
    texto = f"A temperatura em Celsius é de {celsius:.2f}"
    falar(texto)

def calcular_energia_cinetica(massa, velocidade):
    energia = 0.5 * massa * velocidade ** 2
    return energia

def calcular_forca_atrito(coeficiente_atrito, forca_normal):
    forca_atrito = coeficiente_atrito * forca_normal
    return forca_atrito

def calc_forc(massa, aceleracao):
    forca = massa * aceleracao
    return forca

def calcular_velocidade_onda(frequencia, comprimento_onda):
    velocidade_onda = frequencia * comprimento_onda
    return velocidade_onda

def onda_senoidal(x_grid, t_grid, ao, ko, omegao, phio):
    senoidal_wave = ao * np.sin(ko * x_grid - omegao * t_grid + phio)
    return senoidal_wave

def onda_eletromagnetica_1d(x_grid, t_grid, A, lambda_, omega, phi):
    Ex = A * np.cos(omega * t_grid - (2 * np.pi / lambda_) * x_grid + phi)
    By = A * np.cos(omega * t_grid - (2 * np.pi / lambda_) * x_grid + phi)
    return Ex, By

def forca(massa, aceleracao):
    forca = massa * aceleracao
    return forca

def calcular_gravidade(m1, m2, distancia):
    gravidade = 6.674 * (10 ** -11) * ((m1 * m2) / distancia ** 2)
    return gravidade

def equacao_bernoulli(P, rho, v, h, g=9.81):
    """
    Calcula a constante da equação de Bernoulli.

    Args:
    P (float): Pressão do fluido em pascals (Pa).
    rho (float): Densidade do fluido em quilogramas por metro cúbico (kg/m³).
    v (float): Velocidade do fluido em metros por segundo (m/s).
    h (float): Altura em metros em relação a uma referência escolhida.
    g (float, optional): Aceleração devido à gravidade em metros por segundo ao quadrado (m/s²). Default é 9.81.

    Returns:
    float: Constante da equação de Bernoulli.
    """
    return P + 0.5 * rho * v**2 + rho * g * h

def dilatlinear(compriin, material, tempod):
    compri = compriin*material*(tempod)
    return compri

def dilatvol(volin, material1, tempod1):
    dilvol = volin * material1 * tempod1
    return dilvol

def explicar_gravidade():
    print("Aqui você encontrará uma explicação sobre a gravidade da Terra.")

def explicar_pi():
    print("Aqui você encontrará uma explicação sobre o valor de PI na física.")

def forca_gravitacional(m1, m2, r, G=6.67430e-11):
    """
    Calcula a força gravitacional entre dois corpos.

    Args:
    m1 (float): Massa do primeiro corpo em kg.
    m2 (float): Massa do segundo corpo em kg.
    r (float): Distância entre os centros dos corpos em metros.
    G (float, optional): Constante gravitacional universal em N*m²/kg². Default é 6.67430e-11.

    Returns:
    float: Força gravitacional entre os corpos em Newtons.
    """
    return G * abs(m1 * m2) / r**2
def eletricidade(r, i):
    "u flaot, em volts, resistenc float ohml, corrente em amprere float"
    u = r*i
    return u
def capacitor(cargae, difpot):
    "dada uma carga eletrica em float divido pela diferença potencial em float é dada a capacitância"
    capacitancia = cargae*difpot
    return capacitancia
def gravidade(g, m, r):
    gravity = g*m/r**2
    return gravity