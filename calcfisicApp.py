import tkinter as tk
from tkinter import messagebox
import pyttsx3
import numpy as np
import matplotlib.pyplot as plt
import math

# Inicializa o pyttsx3
engine = pyttsx3.init()

def falar(texto, voz='brazil'):
    voices = engine.getProperty('voices')
    for v in voices:
        if 'brazil' in v.id and 'female' in v.id:
            voz = v.id
            break
    engine.setProperty('voice', voz)
    engine.say(texto)
    engine.runAndWait()

def velocidade_carro():
    try:
        distancia = float(entry_distancia.get())
        tempo = float(entry_tempo.get())
        velocidade = distancia / tempo
        resultado = f"A velocidade do carro é de {velocidade:.2f} quilometros por hora."
        label_resultado.config(text=resultado)
        falar(resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos.")

def calcular_trajetoria():
    try:
        v0 = float(entry_v0.get())
        theta = float(entry_theta.get())
        gravidade = float(entry_gravidade.get())
        distancia, altura_maxima = (v0 ** 2 * np.sin(2 * np.radians(theta))) / gravidade, (v0 ** 2 * (np.sin(np.radians(theta))) ** 2) / (2 * gravidade)
        resultado = f"Distância: {distancia:.2f} metros, Altura Máxima: {altura_maxima:.2f} metros"
        label_resultado.config(text=resultado)
        falar(resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos.")

def lei_ohm():
    try:
        volt = float(entry_volt.get())
        amperes = float(entry_amperes.get())
        resistencia = volt / amperes
        resultado = f"A resistência é de {resistencia:.2f} Ohms."
        label_resultado.config(text=resultado)
        falar(resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos.")
def conversao_f(celsius1):
    try:
        celsius1 = float(celsius1)
        fahrenheit = (celsius1 * 9/5) + 32
        resultado = f"A temperatura em Fahrenheit é de {fahrenheit:.2f} °F."
        messagebox.showinfo("Resultado", resultado)
        falar(resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico válido.")

def conversao_k(celsius2):
    try:
        celsius2 = float(celsius2)
        kelvin = celsius2 + 273.15
        resultado = f"A temperatura em Kelvin é de {kelvin:.2f} K."
        messagebox.showinfo("Resultado", resultado)
        falar(resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico válido.")

def conversao_celsius_fahrenheit(fh):
    try:
        fh = float(fh)
        celsius = (fh - 32) * 5/9
        resultado = f"A temperatura em Celsius é de {celsius:.2f} °C."
        messagebox.showinfo("Resultado", resultado)
        falar(resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico válido.")

def conversao_celsius_kelvin(klv):
    try:
        klv = float(klv)
        celsius = klv - 273.15
        resultado = f"A temperatura em Celsius é de {celsius:.2f} °C."
        messagebox.showinfo("Resultado", resultado)
        falar(resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico válido.")
def calcular_energia_cinetica(massa, velocidade):
    try:
        massa = float(massa)
        velocidade = float(velocidade)
        energia = 0.5 * massa * velocidade ** 2
        resultado = f"A energia cinética é de {energia:.2f} Jaules."
        messagebox.showinfo("Resultado", resultado)
        falar(resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

def calcular_forca_atrito(coeficiente_atrito, forca_normal):
    try:
        forca_atrito = coeficiente_atrito * forca_normal
        label_resultado.config(text=f"Força de Atrito: {forca_atrito} N")
        texto = f"Força de Atrito: {forca_atrito} N"
        falar(texto)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")
    

def calcular_forca(massa, aceleracao):
    try:
        forca = massa * aceleracao
        label_resultado.config(text=f"Força: {forca} N")
        texto = f"Força: {forca} Newtons"
        falar(texto)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")
    
def calcular_velocidade_onda(comprimento_onda, frequencia):
    try:
        velocidade_onda = comprimento_onda * frequencia
        label_resultado.config(text=f"Velocidade da Onda: {velocidade_onda} m/s")
        texto = f"Velocidade da Onda: {velocidade_onda} metros por segundo"
        falar(texto)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")
    

def calcular_onda_senoidal(amplitude, frequencia, fase):
    try:
        resultado = f"A função da onda senoidal é: y = {amplitude}*sin({frequencia}*x + {fase})"
        label_resultado.config(text=resultado)
        texto = f"A função da onda senoidal é: y = {amplitude}*sin({frequencia}*x + {fase})"
        falar(texto)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

def calcular_bernoulli(pressao1, densidade_fluido, altura1, velocidade1, pressao2, altura2, velocidade2):
    g = 9.81  # Aceleração da gravidade em m/s²
    termo1 = pressao1 + 0.5 * densidade_fluido * velocidade1**2 + densidade_fluido * g * altura1
    termo2 = pressao2 + 0.5 * densidade_fluido * velocidade2**2 + densidade_fluido * g * altura2
    if termo1 == termo2:
        label_resultado.config(text="A equação de Bernoulli é válida.")
    else:
        label_resultado.config(text="A equação de Bernoulli não é válida.")

def calcular_dilatacao_linear(comprimento_inicial, coeficiente_dilatacao, variacao_temperatura):
    delta_L = comprimento_inicial * coeficiente_dilatacao * variacao_temperatura
    label_resultado.config(text=f"Variação no Comprimento: {delta_L} m")

def calcular_dilatacao_volumetrica(volume_inicial, coeficiente_dilatacao_volumetrica, variacao_temperatura_volumetrica):
    delta_V = volume_inicial * coeficiente_dilatacao_volumetrica * variacao_temperatura_volumetrica
    label_resultado.config(text=f"Variação no Volume: {delta_V} m³")


# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora Física")

# Força
frame_forca = tk.Frame(root)
frame_forca.pack(pady=10)
tk.Label(frame_forca, text="Massa (kg):").grid(row=0, column=0)
entry_massa_forca = tk.Entry(frame_forca)
entry_massa_forca.grid(row=0, column=1)
tk.Label(frame_forca, text="Aceleração (m/s²):").grid(row=1, column=0)
entry_aceleracao = tk.Entry(frame_forca)
entry_aceleracao.grid(row=1, column=1)
btn_calcular_forca = tk.Button(frame_forca, text="Calcular Força", command=lambda: calcular_forca(float(entry_massa_forca.get()), float(entry_aceleracao.get())))
btn_calcular_forca.grid(row=2, columnspan=2, pady=5)

# Energia Cinética
frame_energia_cinetica = tk.Frame(root)
frame_energia_cinetica.pack(pady=10)
tk.Label(frame_energia_cinetica, text="Massa (kg):").grid(row=0, column=0)
entry_massa = tk.Entry(frame_energia_cinetica)
entry_massa.grid(row=0, column=1)
tk.Label(frame_energia_cinetica, text="Velocidade (m/s):").grid(row=1, column=0)
entry_velocidade = tk.Entry(frame_energia_cinetica)
entry_velocidade.grid(row=1, column=1)
btn_calcular_energia = tk.Button(frame_energia_cinetica, text="Calcular Energia Cinética", command=lambda: calcular_energia_cinetica(entry_massa.get(), entry_velocidade.get()))
btn_calcular_energia.grid(row=2, columnspan=2, pady=5)

# Força de Atrito
frame_atrito = tk.Frame(root)
frame_atrito.pack(pady=10)
tk.Label(frame_atrito, text="Coeficiente de Atrito:").grid(row=0, column=0)
entry_coeficiente_atrito = tk.Entry(frame_atrito)
entry_coeficiente_atrito.grid(row=0, column=1)
tk.Label(frame_atrito, text="Força Normal:").grid(row=1, column=0)
entry_forca_normal = tk.Entry(frame_atrito)
entry_forca_normal.grid(row=1, column=1)
btn_calcular_atrito = tk.Button(frame_atrito, text="Calcular Força de Atrito", command=lambda: calcular_forca_atrito(float(entry_coeficiente_atrito.get()), float(entry_forca_normal.get())))
btn_calcular_atrito.grid(row=2, columnspan=2, pady=5)

# Velocidade da Onda
frame_velocidade_onda = tk.Frame(root)
frame_velocidade_onda.pack(pady=10)
tk.Label(frame_velocidade_onda, text="Comprimento de Onda (m):").grid(row=0, column=0)
entry_comprimento_onda = tk.Entry(frame_velocidade_onda)
entry_comprimento_onda.grid(row=0, column=1)
tk.Label(frame_velocidade_onda, text="Frequência (Hz):").grid(row=1, column=0)
entry_frequencia = tk.Entry(frame_velocidade_onda)
entry_frequencia.grid(row=1, column=1)
btn_calcular_velocidade_onda = tk.Button(frame_velocidade_onda, text="Calcular Velocidade da Onda", command=lambda: calcular_velocidade_onda(float(entry_comprimento_onda.get()), float(entry_frequencia.get())))
btn_calcular_velocidade_onda.grid(row=2, columnspan=2, pady=5)

# Velocidade do Carro
frame_velocidade = tk.Frame(root)
frame_velocidade.pack(pady=10)
tk.Label(frame_velocidade, text="Distância (km):").grid(row=0, column=0)
entry_distancia = tk.Entry(frame_velocidade)
entry_distancia.grid(row=0, column=1)
tk.Label(frame_velocidade, text="Tempo (h):").grid(row=1, column=0)
entry_tempo = tk.Entry(frame_velocidade)
entry_tempo.grid(row=1, column=1)
btn_calcular_velocidade = tk.Button(frame_velocidade, text="Calcular Velocidade", command=velocidade_carro)
btn_calcular_velocidade.grid(row=2, columnspan=2, pady=5)

# Trajetória
frame_trajetoria = tk.Frame(root)
frame_trajetoria.pack(pady=10)
tk.Label(frame_trajetoria, text="Velocidade Inicial (m/s):").grid(row=0, column=0)
entry_v0 = tk.Entry(frame_trajetoria)
entry_v0.grid(row=0, column=1)
tk.Label(frame_trajetoria, text="Ângulo (graus):").grid(row=1, column=0)
entry_theta = tk.Entry(frame_trajetoria)
entry_theta.grid(row=1, column=1)
tk.Label(frame_trajetoria, text="Gravidade (m/s²):").grid(row=2, column=0)
entry_gravidade = tk.Entry(frame_trajetoria)
entry_gravidade.grid(row=2, column=1)
btn_calcular_trajetoria = tk.Button(frame_trajetoria, text="Calcular Trajetória", command=calcular_trajetoria)
btn_calcular_trajetoria.grid(row=3, columnspan=2, pady=5)

# Lei de Ohm
frame_ohm = tk.Frame(root)
frame_ohm.pack(pady=10)
tk.Label(frame_ohm, text="Voltagem (V):").grid(row=0, column=0)
entry_volt = tk.Entry(frame_ohm)
entry_volt.grid(row=0, column=1)
tk.Label(frame_ohm, text="Corrente (A):").grid(row=1, column=0)
entry_amperes = tk.Entry(frame_ohm)
entry_amperes.grid(row=1, column=1)
btn_calcular_ohm = tk.Button(frame_ohm, text="Calcular Lei de Ohm", command=lei_ohm)
btn_calcular_ohm.grid(row=2, columnspan=2, pady=5)

# Conversões de temperatura
frame_temperatura = tk.Frame(root)
frame_temperatura.pack(pady=10)

tk.Label(frame_temperatura, text="Celsius para Fahrenheit").grid(row=0, column=0, padx=10, pady=10)
entrada_celsius1 = tk.Entry(frame_temperatura)
entrada_celsius1.grid(row=0, column=1, padx=10, pady=10)
tk.Button(frame_temperatura, text="Converter", command=lambda: conversao_f(entrada_celsius1.get())).grid(row=0, column=2, padx=10, pady=10)

tk.Label(frame_temperatura, text="Celsius para Kelvin").grid(row=1, column=0, padx=10, pady=10)
entrada_celsius2 = tk.Entry(frame_temperatura)
entrada_celsius2.grid(row=1, column=1, padx=10, pady=10)
tk.Button(frame_temperatura, text="Converter", command=lambda: conversao_k(entrada_celsius2.get())).grid(row=1, column=2, padx=10, pady=10)

tk.Label(frame_temperatura, text="Fahrenheit para Celsius").grid(row=2, column=0, padx=10, pady=10)
entrada_fh = tk.Entry(frame_temperatura)
entrada_fh.grid(row=2, column=1, padx=10, pady=10)
tk.Button(frame_temperatura, text="Converter", command=lambda: conversao_celsius_fahrenheit(entrada_fh.get())).grid(row=2, column=2, padx=10, pady=10)

tk.Label(frame_temperatura, text="Kelvin para Celsius").grid(row=3, column=0, padx=10, pady=10)
entrada_klv = tk.Entry(frame_temperatura)
entrada_klv.grid(row=3, column=1, padx=10, pady=10)
tk.Button(frame_temperatura, text="Converter", command=lambda: conversao_celsius_kelvin(entrada_klv.get())).grid(row=3, column=2, padx=10, pady=10)

# Onda Senoidal
frame_onda_senoidal = tk.Frame(root)
frame_onda_senoidal.pack(pady=10)
tk.Label(frame_onda_senoidal, text="Amplitude:").grid(row=2, column=2)
entry_amplitude = tk.Entry(frame_onda_senoidal)
entry_amplitude.grid(row=0, column=1)
tk.Label(frame_onda_senoidal, text="Frequência (Hz):").grid(row=2, column=2)
entry_frequencia_onda = tk.Entry(frame_onda_senoidal)
entry_frequencia_onda.grid(row=1, column=1)
tk.Label(frame_onda_senoidal, text="Fase (rad):").grid(row=2, column=2)
entry_fase = tk.Entry(frame_onda_senoidal)
entry_fase.grid(row=2, column=1)
btn_calcular_onda_senoidal = tk.Button(frame_onda_senoidal, text="Calcular Onda Senoidal", command=lambda: calcular_onda_senoidal(float(entry_amplitude.get()), float(entry_frequencia_onda.get()), float(entry_fase.get())))
btn_calcular_onda_senoidal.grid(row=3, columnspan=2, pady=5)

# Equação de Bernoulli
frame_bernoulli = tk.Frame(root)
frame_bernoulli.pack(pady=10)
tk.Label(frame_bernoulli, text="Pressão 1 (Pa):").grid(row=0, column=0)
entry_pressao1 = tk.Entry(frame_bernoulli)
entry_pressao1.grid(row=0, column=1)
tk.Label(frame_bernoulli, text="Densidade do Fluido (kg/m³):").grid(row=1, column=0)
entry_densidade_fluido = tk.Entry(frame_bernoulli)
entry_densidade_fluido.grid(row=1, column=1)
tk.Label(frame_bernoulli, text="Altura 1 (m):").grid(row=2, column=0)
entry_altura1 = tk.Entry(frame_bernoulli)
entry_altura1.grid(row=2, column=1)
tk.Label(frame_bernoulli, text="Velocidade 1 (m/s):").grid(row=3, column=0)
entry_velocidade1 = tk.Entry(frame_bernoulli)
entry_velocidade1.grid(row=3, column=1)
tk.Label(frame_bernoulli, text="Pressão 2 (Pa):").grid(row=4, column=0)
entry_pressao2 = tk.Entry(frame_bernoulli)
entry_pressao2.grid(row=4, column=1)
tk.Label(frame_bernoulli, text="Altura 2 (m):").grid(row=5, column=0)
entry_altura2 = tk.Entry(frame_bernoulli)
entry_altura2.grid(row=5, column=1)
tk.Label(frame_bernoulli, text="Velocidade 2 (m/s):").grid(row=6, column=0)
entry_velocidade2 = tk.Entry(frame_bernoulli)
entry_velocidade2.grid(row=6, column=1)
btn_calcular_bernoulli = tk.Button(frame_bernoulli, text="Calcular Equação de Bernoulli", command=lambda: calcular_bernoulli(float(entry_pressao1.get()), float(entry_densidade_fluido.get()), float(entry_altura1.get()), float(entry_velocidade1.get()), float(entry_pressao2.get()), float(entry_altura2.get()), float(entry_velocidade2.get())))
btn_calcular_bernoulli.grid(row=7, columnspan=2, pady=5)

# Dilatação Linear
frame_dilatacao_linear = tk.Frame(root)
frame_dilatacao_linear.pack(pady=10)
tk.Label(frame_dilatacao_linear, text="Comprimento Inicial (m):").grid(row=0, column=0)
entry_comprimento_inicial = tk.Entry(frame_dilatacao_linear)
entry_comprimento_inicial.grid(row=0, column=1)
tk.Label(frame_dilatacao_linear, text="Coeficiente de Dilatação Linear (1/°C):").grid(row=1, column=0)
entry_coeficiente_dilatacao = tk.Entry(frame_dilatacao_linear)
entry_coeficiente_dilatacao.grid(row=1, column=1)
tk.Label(frame_dilatacao_linear, text="Variação de Temperatura (°C):").grid(row=2, column=0)
entry_variacao_temperatura = tk.Entry(frame_dilatacao_linear)
entry_variacao_temperatura.grid(row=2, column=1)
btn_calcular_dilatacao_linear = tk.Button(frame_dilatacao_linear, text="Calcular Dilatação Linear", command=lambda: calcular_dilatacao_linear(float(entry_comprimento_inicial.get()), float(entry_coeficiente_dilatacao.get()), float(entry_variacao_temperatura.get())))
btn_calcular_dilatacao_linear.grid(row=3, columnspan=2, pady=5)

# Dilatação Volumétrica
frame_dilatacao_volumetrica = tk.Frame(root)
frame_dilatacao_volumetrica.pack(pady=10)
tk.Label(frame_dilatacao_volumetrica, text="Volume Inicial (m³):").grid(row=0, column=0)
entry_volume_inicial = tk.Entry(frame_dilatacao_volumetrica)
entry_volume_inicial.grid(row=0, column=1)
tk.Label(frame_dilatacao_volumetrica, text="Coeficiente de Dilatação Volumétrica (1/°C):").grid(row=1, column=0)
entry_coeficiente_dilatacao_volumetrica = tk.Entry(frame_dilatacao_volumetrica)
entry_coeficiente_dilatacao_volumetrica.grid(row=1, column=1)
tk.Label(frame_dilatacao_volumetrica, text="Variação de Temperatura (°C):").grid(row=2, column=0)
entry_variacao_temperatura_volumetrica = tk.Entry(frame_dilatacao_volumetrica)
entry_variacao_temperatura_volumetrica.grid(row=2, column=1)
btn_calcular_dilatacao_volumetrica = tk.Button(frame_dilatacao_volumetrica, text="Calcular Dilatação Volumétrica", command=lambda: calcular_dilatacao_volumetrica(float(entry_volume_inicial.get()), float(entry_coeficiente_dilatacao_volumetrica.get()), float(entry_variacao_temperatura_volumetrica.get())))
btn_calcular_dilatacao_volumetrica.grid(row=3, columnspan=2, pady=5)


# Resultado
label_resultado = tk.Label(root, text="")
label_resultado.pack(pady=10)


root.mainloop()