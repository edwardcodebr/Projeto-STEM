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
# Exemplo de uso:
tela_carregamento(tempo_carregamento)
while True:
    print('''
    Bem-vindo ao aplicativo de física
    Criadores: C. Eduardo Correa Queiroz (Programador), Carlos Eduardo de Deus e Joaquim Diogenes.
    Versão: 0.7.24
    Escolha sua opção:
    1 - Medir velocidade em KM.
    2 - Medir distância de um lançamento oblíquo em m.
    3 - Medir resistência.
    4 - Transformar celsius para Fahrenheit.
    5 - Transformar celsius para Kelvin.
    6 - Transformar Fahrenheit para celsius.
    7 - Transformar Kelvin para celsius.
    8 - Calcular energia cinética.
    9 - Calcular força de atrito.
    10 - Calcular força.
    11 - Calcular velocidade da onda.
    12 - Calcular onda senoidal.
    13 - Calcular onda eletromagnética.
    14 - Mostrar força gravitacional.
    15 - Equação de Bernoulli.
    16 - Medir eletricidade.
    17 - Medir capacitor.
    18 - Ver explicação do cálculo da gravidade da Terra.
    19 - Ver explicação do valor de PI na física.
    20 - Medir dilatação linear.
    21 - Medir dilatação volumétrica.
    22 - Lista de materiais para dilatação em notação científica.
    23 - Materiais para engenharia (densidade, módulo, resistência e coeficiente).
    24 - informações do sistema.
    25 - Sair.
    ''')
    menu()
    escolha = int(input("Escolha uma opção: "))
    match escolha:
        case 1:
            def distanciafalar():
                texto = 'bote o valor da distancia'
                falar(texto)
            distanciafalar()
            distancia = float(input("Corrida do carro em quilometros(0.00KM):"))
            def tempofalar():
                texto = 'bote o valor do tempo'
                falar(texto)
            tempofalar()
            tempo = float(input("Tempo percorrido em horas(acrescente o minutos em 0.00):"))
            velocidade_carro(distancia, tempo)
            
        case 2:
            texto = 'Digite o lançamento em graus'
            falar(texto)
            theta = float(input("Digite o ângulo de lançamento em graus (em float: 0.00):"))
            texto = 'digite a velociade inicial'
            falar(texto)
            v0 = float(input("Digite a velocidade inicial em m/s (metros por segundo: 0.00):"))
            
            gravidade = 9.81
            distancia, altura_maxima = calcular_trajetoria(v0, theta, gravidade)
            print(f"Distância total: {distancia:.2f} metros") 
            print(f"Altura máxima: {altura_maxima:.2f} Metros")
            texto = f'Distância total: {distancia:.2f} metros'
            texto1 = f"Altura máxima: {altura_maxima:.2f} Metros"
            falar(texto)
            falar(texto1)
    
        case 3:
            texto = 'digite a voltagem'
            falar(texto)
            volt = float(input("Voltagem:"))
            texto = 'digite a corrente'
            falar(texto)
            amperes = float(input("Corrente em amperes:"))
            lei_ohl(volt, amperes)
        case 4:
            celsius1 = float(input("temperatura(em celsius):"))
            conversao_f(celsius1)
        case 5:
            celsius2 = float(input("temperatura(em celsius):"))
            conversao_k(celsius2)
        case 6:
            fh = float(input("temperatura (em fahrenheit):"))
            conversao_celsius_fahrenheit(fh)
        case 7:
            klv = float(input("temperatura (em kelvin):"))
            conversao_celsius_kelvin(klv)
        case 8:
            texto = "Digite a massa do objeto"
            falar(texto)
            massa = float(input("Digite a massa do objeto em kg (em float: 0.00): "))
            texto = "digite a velocidade do objeto"
            falar(texto)
            velocidade = float(input("Digite a velocidade do objeto em m/s (em float: 0.00): "))

            # Calcula a energia cinética
            energia = calcular_energia_cinetica(massa, velocidade)

           # Exibe o resultado
            print(f"A energia cinética do objeto é: {energia:.2f} joules")
            texto = f"A energia cinética do objeto é: {energia:.2f} joules"
            falar(texto)
        case 9:
            texto = "digite o coeficiente de atrito"
            falar(texto)
            coeficiente_atrito = float(input("digite o coeficiente de atrito (em float: 0.00):"))
            texto = "digite a força normal em newtons"
            falar(texto)
            forca_normal = float(input("Digite a força normal em Newtons(em float: 0.00):"))
            
            forca_atrito = calcular_forca_atrito(coeficiente_atrito, forca_normal)
            
            print(f"A força de atrito é: {forca_atrito:.2f} Newtons.") 
            texto = f"A força de atrito é: {forca_atrito:.2f} Newtons."
            falar(texto)
        case 10:
            texto = "digite a massa do objeto em quilogramas"
            falar(texto)
            massa = float(input("Digite a massa do objeto em quilogramas(em float: 0.00):"))
            texto = "digite a aceleração em metro quadrado"
            falar(texto)
            aceleracao = float(input("digite a aceleração em metros por segundo ao quadrado(em float: 0.00)"))
            
            forca = calc_forc(massa, aceleracao)
            print(f"A força resultante é: {forca:.2f} Newtons")
            texto = f"A força resultante é: {forca:.2f} Newtons"
            falar(texto)
        case 11:
            texto = "digite a frequencia"
            falar(texto)
            frequencia = float(input("digite a frquencia em heartz (Hz):"))
            texto = "digite o comprimento de onda"
            falar(texto)
            comprimento_onda = float(input("Digite o comprimento de onda em metros(em float: 0.00):"))
            
            velocidade_onda = calcular_velocidade_onda(frequencia, comprimento_onda)
            print(f"A velocidade da onda é: {velocidade_onda:.2f} metros por segundo.")
            texto = f"A velocidade da onda é: {velocidade_onda:.2f} metros por segundo"
            falar(texto)
        case 12:
            texto = "digite a posição X"
            x = float(input("Digite a posição (x): "))
            texto = "digite o tempo"
            t = float(input("Digite o tempo (t): "))
            texto = "digite a amplitude"
            ao = float(input("Digite a amplitude máxima (ao) [default 1]: ") or 1)
            texto = "digite a onda"
            ko = float(input("Digite o número de onda (ko) [default 2]: ") or 2)
            texto = "digite a frequencia angular"
            omegao = float(input("Digite a frequência angular (omegao) [default 3]: ") or 3)
            texto = "e por ultimo, digite a fase inicial"
            phio = float(input("Digite a fase inicial (phio) [default 0]: ") or 0)
            texto = "veja o resultado"
            falar(texto)
            # Criando uma malha de x e t
            x_vals = np.linspace(0, 10, 100)  # Define os valores de x para a malha
            t_vals = np.linspace(0, 10, 100)  # Define os valores de t para a malha
            x_grid, t_grid = np.meshgrid(x_vals, t_vals)

            # Calculando a onda senoidal em função de x e t
            senoidal_wave = onda_senoidal(x_grid, t_grid, ao, ko, omegao, phio)

            # Plotando a onda senoidal
            plt.figure(figsize=(10, 6))
            plt.imshow(senoidal_wave, cmap='viridis', extent=[0, 10, 0, 10], aspect='auto', origin='lower')
            plt.colorbar(label='Amplitude da Onda')
            plt.title('Simulação de Onda Senoidal')
            plt.xlabel('Espaço')
            plt.ylabel('Tempo')
            plt.show()
        case 13:
            texto = "digite a posição X"
            falar(texto)
            x = float(input("Digite a posição (x): "))
            texto = "digite o tempo"
            falar(texto)
            t = float(input("Digite o tempo (t): "))
            texto = "digite a amplitude"
            falar(texto)
            A = float(input("Digite a amplitude máxima (A) [default 1]: ") or 1)
            texto = "digite o comprimento de onda"
            falar(texto)
            lambda_ = float(input("Digite o comprimento de onda (lambda) [default 1]: ") or 1)
            texto = "digite a frequência"
            falar(texto)
            omega = float(input("Digite a frequência angular (omega) [default 2*pi]: ") or 2 * np.pi)
            texto = "digite a fase inicial"
            falar(texto)
            phi = float(input("Digite a fase inicial (phi) [default 0]: ") or 0)

            texto = "veja seu resultado de ondas eletromagnetica"
            falar(texto)
            
            # Criando uma malha de x e t
            x_vals = np.linspace(0, 10, 100)  # Define os valores de x para a malha
            t_vals = np.linspace(0, 10, 100)  # Define os valores de t para a malha
            x_grid, t_grid = np.meshgrid(x_vals, t_vals)

            # Calculando o campo elétrico e magnético em função de x e t
            Ex, By = onda_eletromagnetica_1d(x_grid, t_grid, A, lambda_, omega, phi)

            # Plotando o campo elétrico
            plt.figure(figsize=(12, 6))

            plt.subplot(2, 1, 1)
            plt.imshow(Ex, cmap='viridis', extent=[0, 10, 0, 10], aspect='auto', origin='lower')
            plt.colorbar(label='Campo Elétrico (Ex)')
            plt.title('Simulação de Onda Eletromagnética - Campo Elétrico')
            plt.xlabel('Espaço')
            plt.ylabel('Tempo')

            # Plotando o campo magnético
            plt.subplot(2, 1, 2)
            plt.imshow(By, cmap='viridis', extent=[0, 10, 0, 10], aspect='auto', origin='lower')
            plt.colorbar(label='Campo Magnético (By)')
            plt.title('Simulação de Onda Eletromagnética - Campo Magnético')
            plt.xlabel('Espaço')
            plt.ylabel('Tempo')

            plt.tight_layout()
            plt.show()
        case 14:
            m1 = 5.972e24  # Massa da Terra em kg
            m2 = 7.348e22  # Massa da Lua em kg
            r = 3.844e8  # Distância média entre a Terra e a Lua em metros

            forca = forca_gravitacional(m1, m2, r)
            print(f"A força gravitacional entre a Terra e a Lua é {forca} Newtons.")
            texto = f"A força gravitacional entre a Terra e a Lua é {forca} Newtons"
            falar(texto)
        case 15:
            texto = "digite a pressão do fluido em pascal"
            falar(texto)
            P = float(input("Digite a pressão do fluido em pascals (Pa): "))
            texto = "digite a densidade"
            falar(texto)
            rho = float(input("Digite a densidade do fluido em quilogramas por metro cúbico (kg/m³): "))
            texto = "digite a velocidade do fluido"
            falar(texto)
            v = float(input("Digite a velocidade do fluido em metros por segundo (m/s): "))
            texto = "digite a altura de referência"
            falar(texto)
            h = float(input("Digite a altura em metros em relação a uma referência escolhida: "))
            texto = "digite a aceleração"
            falar(texto)
            g = float(input("Digite a aceleração devido à gravidade em metros por segundo ao quadrado (m/s²): "))

# Cálculo da constante de Bernoulli 
            constante_bernoulli = equacao_bernoulli(P, rho, v, h, g)
# Output
            print(f"A constante de Bernoulli é: {constante_bernoulli} Pa")
            texto = f"sua constante é de {constante_bernoulli}"
            falar(texto)
        case 16:
            texto = 'insira a resisência'
            falar(texto)
            print("Insira a resistência(em float):")
            r = float(input())
            texto = 'insira a corrente em amperes'
            falar(texto)
            print("insira a corrente em amperes")
            i = float(input())
            u = eletricidade(r, i)
            print(f"{u} Volts")
            texto = f"seu resultado deu {u} Volts"
            falar(texto)
        case 17:
            texto = 'insira a carga elétrica'
            falar(texto)
            print("Insira a carga elétrica(em float):")
            cargae = float(input())
            texto = "insira a diferença potêncial"
            texto(falar)
            print("insira a diferença potêncial(em float)")
            difpot = float(input())
            capacitancia = capacitor(cargae, difpot)
            print(f"{capacitancia:.2f} Jaules")
            texto = f"seu resultado deu {capacitancia:.2f} Jaules"
            falar(texto)
        case 18:
            print('''A gravidade da terra, denotada por "g" na física,
            é a aceleração que um objeto experimenta devido a atração gravitacional da terra.
            O valor padrão da gravidade ao nível do mar é aproximadamente 9,81 m/s**2.
            Este valor pode ser calculado utilizando a fórmula da lei da Gravitação universal de Newton.
            
            g = GM/R**2
            Onde:
            G = é a constante gravitacional(6,674x10**-11)
            M = é a massa da terra(5,972x10**24)
            R = É o raio da terra(6,371x10**6)''')
            g = 6.674*10**-11
            m = 5.972*10**24
            r = 6.371*10**6
            gravity = gravidade(g, m, r)
            print(f"Gravidade da terra igual {gravity:.3}")
            texto = f"A gravidade da terra, denotada por g na física, é a aceleração que um objeto experimenta devido a atração gravitacional da terra. O valor padrão da gravidade ao nível do mar é aproximadamente 9,81 m/s**2. Este valor pode ser calculado utilizando a fórmula da lei da Gravitação universal de Newton. g igual a GM/R ao quadrado Onde: G é a constante gravitacional(6,674x10**-11) M é a massa da terra(5,972x10**24)R é o raio da terra(6,371x10**6) Gravidade da terra igual {gravity:.3}"
            falar(texto)
            print("-- Bônus --")
            print('''A gravidade igual a 10 m/s**2, é usado na engenharia em seus cálculos no ensino por:
            Simplicidade nos cálculos, aproximação suficiente precisa, facilitação no ensino e margem de segurança.
            Portanto, o uso de 10m/s**2 é uma prática comum devido à conveniência e à pequena margem de erro introduzida pela aproximação.''')
            
            texto = f'bônus A gravidade igual a 10 m/s**2, é usado na engenharia em seus cálculos no ensino por: Simplicidade nos cálculos, aproximação suficiente precisa, facilitação no ensino e margem de segurança. Portanto, o uso de 10 metros ao quadrado é uma prática comum devido à conveniência e à pequena margem de erro introduzida pela aproximação.'
            falar(texto)
        case 19:
            print("A constante matemática (pi):")
            print('''Tem relação com uma circuferência de um circulo e seu diâmetro,
            desempenha um papel fundamental em muitos campos da física. Sua história na física está ligada com o desenvolvimento
            da mátematica e da ciência em geral.
            Hoje, PI é fundamental em muitos campos da física, incluindo mecânica, termodinâmica, eletricidade e magnetismo.
            É amplamente utilizado em cálculos e formulações teóricas.''')
            print("-- Bônus --")
            print('Refêrencia na biblia:')
            print('''Em 1 Reis 7:23, onde é descrita a construção de um "mar de fundição"
            um grande recipiente circular no templo de Salomão. O versículo afirma que o diâmetro do mar era de 10 côvados e com perímetro de 30 côvados,
            o que implicaria um valor de PI igual a 3. Essa simplificação pode ter sido feita por conveniência prática ou por razões simbólicas,
            e não reflete a precisão matemática atual de PI.''')
            
            texto = f'A constante matemática (pi) Tem relação com uma circuferência de um circulo e seu diâmetro, desempenha um papel fundamental em muitos campos da física. Sua história na física está ligada com o desenvolvimento da mátematica e da ciência em geral. Hoje, PI é fundamental em muitos campos da física, incluindo mecânica, termodinâmica, eletitrismo e magnetismo. É amplamente utilizado em cálculos e formulações teóricas. Bônus Refêrencia na biblia. Em 1 Reis 7:23, onde é descrita a construção de um mar de fundição, um grande recipiente circular no templo de Salomão. O versículo afirma que o diâmetro do mar era de 10 côvados e com perímetro de 30 côvados, o que implicaria um valor de PI igual a 3. Essa simplificação pode ter sido feita por conveniência prática ou por razões simbólicas, e não reflete a precisão matemática atual de PI.'
            falar(texto)
        case 20:
            texto = 'digite o comprimento inicial'
            falar(texto)
            print("digite o comprimento inicial(em float 0.00).")
            compriin = float(input())
            texto = 'digite o material'
            falar(texto)
            print("digite o material para dilatar (em inteiro 0)")
            print('''1 - aluminio
2 - cobre
3 - vidro
4 - aço
5 - cimento''')
            materilist = int(input())
            match materilist:
                case 1:
                    aluminio = 2.4*pow(10,-5)
                    material = aluminio
                case 2:
                    cobre = 1.7*pow(10,-5)
                    material = cobre
                case 3:
                    vidro = 0.5*pow(10,-5)
                    material = vidro
                case 4:
                    aco = 1.2*pow(10,-5)
                    material = aco
                case 5:
                    cimento = 0.7*pow(10,-6)
                    material = cimento
            texto = 'digite a temperatura final'
            falar(texto)
            print("digite o temperatura final(em float 0.00):")
            tempf = float(input())
            texto = 'digite a temperatura inicial'
            falar(texto)
            print("digite o temperatura inicial(em float 0.00):")
            tempin = float(input())
            tempod = tempf - tempin
            compri = dilatlinear(compriin, material, tempod)
            print(f"{compri} Metros")
            texto = f"{compri} Metros"
            falar(texto)
        case 21:
            texto = 'digite o volume cubico inicial'
            falar(texto)
            print("Digite o volume cubico inicial (em float 0.00)")
            volin = float(input())
            texto = 'digite o material'
            falar(texto)
            print("digite o material para dilatar (em inteiro 0)")
            print('''1 - agua
2 - gelo
3 - cobre
4 - aco
5 - vidro
6 - concreto
7 - vidro prex''')
            materilist1 = int(input())
            match materilist1:
                case 1:
                    agua = 3.3*pow(10,-4)
                    material1 = agua
            
                case 2:
                    gelo = 1.53*pow(10,-4)
                    material1 = gelo
                   
                case 3:
                    cobre = 5.1*pow(10,-5)
                    material1 = cobre
                   
                case 4:
                    aco = 3.3*pow(10,-5)
                    material1 = aco
                  
                case 5:
                    vidro = 2.7*pow(10,-5)
                    material1 = cimento
                  
                case 6:
                    concreto = 3.6* pow(10,-5)
                    material1 = concreto
                  
                case 7:
                    vidroprex = 9.6*pow(10,-6)
                    material1 = vidroprex
            
            texto = 'digite a temperatura final'
            falar(texto)
            print("digite o temperatura final(em float 0.00):")
            tempf1 = float(input())
            texto = 'digite a temperatura inicial'
            falar(texto)
            print("digite o temperatura inicial(em float 0.00):")
            tempin1 = float(input())
            tempod1 = tempf1 - tempin1
            dilvol = dilatvol(volin, material1, tempod1)
            print(f"{dilvol} Metros cubicos.")
            texto = f"{dilvol} Metros cubicos."
            falar(texto)
        case 22:
            print('''A dilatação térmica é um fenômeno físico que descreve a variação das dimensões de um corpo devido à variação de temperatura. Os principais materiais que apresentam dilatação térmica são os sólidos, líquidos e gases. Aqui estão alguns exemplos de materiais e seus coeficientes de dilatação linear em notação científica:

    Alumínio: 2.3×10−5 K−12.3×10−5K−1
    Ferro: 1.2×10−5 K−11.2×10−5K−1
    Cobre: 1.7×10−5 K−11.7×10−5K−1
    Chumbo: 2.9×10−5 K−12.9×10−5K−1
    Aço: 1.1×10−5 K−11.1×10−5K−1
    Vidro: 0.9×10−5 K−10.9×10−5K−1
    Água: 0.21×10−3 K−10.21×10−3K−1
    Mercúrio: 0.18×10−3 K−10.18×10−3K−1
    Ar (ideal): 3.4×10−3 K−13.4×10−3K−1
    Zinco: 3.0×10−5 K−13.0×10−5K−1
    Latão: 1.9×10−5 K−11.9×10−5K−1
    Níquel: 1.3×10−5 K−11.3×10−5K−1
    Prata: 1.9×10−5 K−11.9×10−5K−1
    Ouro: 1.4×10−5 K−11.4×10−5K−1
    Platina: 8.8×10−6 K−18.8×10−6K−1
    Tungstênio: 4.5×10−6 K−14.5×10−6K−1
    Quartzo: 0.55×10−6 K−10.55×10−6K−1
    Gelo: 5.0×10−5 K−15.0×10−5K−1
    Borracha: 2.0×10−4 K−12.0×10−4K−1
    Madeira (média): 5.0×10−6 K−15.0×10−6K−1
    Tijolo: 5.0×10−6 K−15.0×10−6K−1
    Cimento: 5.0×10−6 K−15.0×10−6K−1
    Poliéster: 6.0×10−5 K−16.0×10−5K−1
    Poliestireno: 8.5×10−5 K−18.5×10−5K−1
    Polietileno: 1.1×10−4 K−11.1×10−4K−1
    Acrílico: 7.5×10−5 K−17.5×10−5K−1
    Cristal: 0.55×10−6 K−10.55×10−6K−1
    Concreto: 1.2×10−5 K−11.2×10−5K−1
    Granito: 3.0×10−6 K−13.0×10−6K−1
    Mármore: 5.0×10−6 K−15.0×10−6K−1
    PVC: 5.5×10−5 K−15.5×10−5K−1
    Vidro borossilicato: 3.3×10−6 K−13.3×10−6K−1
    Ferro fundido: 1.0×10−5 K−11.0×10−5K−1
    Aço inoxidável: 1.6×10−5 K−11.6×10−5K−1
    Alumina: 8.0×10−6 K−18.0×10−6K−1
    Carbono (grafite): 8.0×10−6 K−18.0×10−6K−1
    Silício: 2.6×10−6 K−12.6×10−6K−1
    Silício (cristalino): 2.6×10−6 K−12.6×10−6K−1
    Quartzo (fused): 0.55×10−6 K−10.55×10−6K−1
    Teflon: 1.1×10−4 K−11.1×10−4K−1
    Vidro de borosilicato: 3.3×10−6 K−13.3×10−6K−1
    Nitinol: 1.1×10−5 K−11.1×10−5K−1
    Niobato de lítio: 10.0×10−6 K−110.0×10−6K−1
    Zircônia: 10.0×10−6 K−110.0×10−6K−1
    Ametista: 5.0×10−6 K−15.0×10−6K−1
    Safira: 5.0×10−6 K−15.0×10−6K−1
    Rubidium: 8.6×10−6 K−18.6×10−6K−1
    Argônio: 5.3×10−5 K−15.3×10−5K−1
    Enxofre: 2.0×10−5 K−12.0×10−5K−1
    Ferro (gama): 4.6×10−5 K−14.6×10−5K−1
    
Esses valores representam a variação percentual de comprimento por grau Celsius de temperatura.''')
        case 23:
            print('''Materiais para engenharia são importantes na fisica, pois sua densidade, resistencia, cedencia, modulo e coefinciente correspondem com a fisica:
Aço Carbono:

    Densidade: ~7850 kg/m³
    Resistência: ~250-500 MPa
    Módulo de Elasticidade: ~200 GPa
    Coeficiente de Expansão Térmica: ~12 x 10^-6 /°C

Alumínio:

    Densidade: ~2700 kg/m³
    Resistência: ~300 MPa
    Módulo de Elasticidade: ~70 GPa
    Coeficiente de Expansão Térmica: ~23.1 x 10^-6 /°C

Cobre:

    Densidade: ~8900 kg/m³
    Resistência: ~220 MPa
    Módulo de Elasticidade: ~110 GPa
    Coeficiente de Expansão Térmica: ~16.5 x 10^-6 /°C

Titânio:

    Densidade: ~4500 kg/m³
    Resistência: ~1000 MPa
    Módulo de Elasticidade: ~110 GPa
    Coeficiente de Expansão Térmica: ~8.6 x 10^-6 /°C

Aço Inoxidável:

    Densidade: ~7900 kg/m³
    Resistência: ~500-1000 MPa
    Módulo de Elasticidade: ~200 GPa
    Coeficiente de Expansão Térmica: ~10-17 x 10^-6 /°C

Polietileno de Alta Densidade (HDPE):

    Densidade: ~950 kg/m³
    Resistência: ~20-30 MPa
    Módulo de Elasticidade: ~0.8-1.0 GPa
    Coeficiente de Expansão Térmica: ~100-200 x 10^-6 /°C

Ferro Fundido:

    Densidade: ~6800-7800 kg/m³
    Resistência: ~100-700 MPa
    Módulo de Elasticidade: ~100-170 GPa
    Coeficiente de Expansão Térmica: ~10-14 x 10^-6 /°C

Alumina (Cerâmica):

    Densidade: ~3900 kg/m³
    Resistência: ~200-400 MPa
    Módulo de Elasticidade: ~300-400 GPa
    Coeficiente de Expansão Térmica: ~8 x 10^-6 /°C

Concreto:

    Densidade: ~2400 kg/m³
    Resistência: ~20-40 MPa
    Módulo de Elasticidade: ~15-30 GPa
    Coeficiente de Expansão Térmica: ~10-15 x 10^-6 /°C

Madeira (Pinus):

    Densidade: ~500 kg/m³
    Resistência: ~40-80 MPa
    Módulo de Elasticidade: ~5-10 GPa
    Coeficiente de Expansão Térmica: ~5-8 x 10^-6 /°C

Polímeros Reforçados com Fibra de Carbono:

    Densidade: ~1500-2000 kg/m³
    Resistência: ~1000-4000 MPa
    Módulo de Elasticidade: ~150-300 GPa
    Coeficiente de Expansão Térmica: ~0,1-3 x 10^-6 /°C

Vidro:

    Densidade: ~2500 kg/m³
    Resistência: ~20-120 MPa
    Módulo de Elasticidade: ~50-90 GPa
    Coeficiente de Expansão Térmica: ~8-10 x 10^-6 /°C

Cimento Portland:

    Densidade: ~3100 kg/m³
    Resistência: ~10-80 MPa
    Módulo de Elasticidade: ~10-40 GPa
    Coeficiente de Expansão Térmica: ~8-13 x 10^-6 /°C

Tungstênio:

    Densidade: ~19300 kg/m³
    Resistência: ~550-1000 MPa
    Módulo de Elasticidade: ~400-550 GPa
    Coeficiente de Expansão Térmica: ~4.5 x 10^-6 /°C

Zinco:

    Densidade: ~7100 kg/m³
    Resistência: ~100-300 MPa
    Módulo de Elasticidade: ~80-110 GPa
    Coeficiente de Expansão Térmica: ~30-35 x 10^-6 /°C

Nylon:

    Densidade: ~1100 kg/m³
    Resistência: ~40-80 MPa
    Módulo de Elasticidade: ~2-4 GPa
    Coeficiente de Expansão Térmica: ~70-170 x 10^-6 /°C

PVC (Policloreto de Vinila):

    Densidade: ~1400 kg/m³
    Resistência: ~50-80 MPa
    Módulo de Elasticidade: ~2.5-4 GPa
    Coeficiente de Expansão Térmica: ~50-80 x 10^-6 /°C

Latão:

    Densidade: ~8500 kg/m³
    Resistência: ~100-550 MPa
    Módulo de Elasticidade: ~90-130 GPa
    Coeficiente de Expansão Térmica: ~18-20 x 10^-6 /°C

Ferro:

    Densidade: ~7850 kg/m³
    Resistência: ~200-400 MPa
    Módulo de Elasticidade: ~190-210 GPa
    Coeficiente de Expansão Térmica: ~11-13 x 10^-6 /°C

Bronze:

    Densidade: ~8300 kg/m³''')

        case 24:
            print("Calcfisic IA, versão 0.8")
            print("programado por Carlos Eduardo Corrêa Queiroz e auxiliado por Eduardo de Deus e Joaquim Diógenes e supervisionado pelo orientador Edvam Nunes")
            print('um projeto de pesquisa e desenvolvimento da "science tecnology engineering mathematic" da Samsung Amazonas da Universidade do Estado do Amazonas.')
            texto = "Calcfisic IA, versão 0.8, programado por Carlos Eduardo Corrêa Queiroz e auxiliado por Eduardo de Deus e Joaquim Diógenes e supervisionado pelo orientador Edvam Nunes, um projeto de pesquisa e desenvolvimento da science tecnology engineering mathematic da Samsung Amazonas da Universidade do Estado do Amazonas."
            falar(texto)
        case 25:
            texto = 'desligando o sistema, obrigado por usar e volte sempre'
            falar(texto)
            print("DESLIGANDO")
            sys.exit()
