import tkinter as tk
from tkinter import messagebox

import numpy as np

import math


def velocidade_carro():
    try:
        distancia = float(entry_distancia.get())
        tempo = float(entry_tempo.get())
        velocidade = distancia / tempo
        resultado = f"A velocidade do carro é de {velocidade:.2f} km/h."
        label_resultado.config(text=resultado)
       
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos.")

def calcular_trajetoria():
    try:
        v0 = float(entry_v0.get())
        theta = float(entry_theta.get())
        gravidade = float(entry_gravidade.get())
        distancia, altura_maxima = (v0 ** 2 * np.sin(2 * np.radians(theta))) / gravidade, (v0 ** 2 * (np.sin(np.radians(theta))) ** 2) / (2 * gravidade)
        resultado = f"Distância: {distancia:.2f} m, Altura Máxima: {altura_maxima:.2f} m"
        label_resultado.config(text=resultado)
        
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos.")

def lei_ohm():
    try:
        volt = float(entry_volt.get())
        amperes = float(entry_amperes.get())
        resistencia = volt / amperes
        resultado = f"A resistência é de {resistencia:.2f} Ohms."
        label_resultado.config(text=resultado)
        
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos.")
def conversao_f(celsius1):
    try:
        celsius1 = float(celsius1)
        fahrenheit = (celsius1 * 9/5) + 32
        resultado = f"A temperatura em Fahrenheit é de {fahrenheit:.2f} °F."
        messagebox.showinfo("Resultado", resultado)
    
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico válido.")

def conversao_k(celsius2):
    try:
        celsius2 = float(celsius2)
        kelvin = celsius2 + 273.15
        resultado = f"A temperatura em Kelvin é de {kelvin:.2f} K."
        messagebox.showinfo("Resultado", resultado)
    
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico válido.")

def conversao_celsius_fahrenheit(fh):
    try:
        fh = float(fh)
        celsius = (fh - 32) * 5/9
        resultado = f"A temperatura em Celsius é de {celsius:.2f} °C."
        messagebox.showinfo("Resultado", resultado)
    
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico válido.")

def conversao_celsius_kelvin(klv):
    try:
        klv = float(klv)
        celsius = klv - 273.15
        resultado = f"A temperatura em Celsius é de {celsius:.2f} °C."
        messagebox.showinfo("Resultado", resultado)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico válido.")
def calcular_energia_cinetica(massa, velocidade):
    try:
        massa = float(massa)
        velocidade = float(velocidade)
        energia = 0.5 * massa * velocidade ** 2
        resultado = f"A energia cinética é de {energia:.2f} J."
        messagebox.showinfo("Resultado", resultado)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

def calcular_forca_atrito(coeficiente_atrito, forca_normal):
    forca_atrito = coeficiente_atrito * forca_normal
    label_resultado.config(text=f"Força de Atrito: {forca_atrito} N")

def calcular_forca(massa, aceleracao):
    forca = massa * aceleracao
    label_resultado.config(text=f"Força: {forca} N")

def calcular_velocidade_onda(comprimento_onda, frequencia):
    velocidade_onda = comprimento_onda * frequencia
    label_resultado.config(text=f"Velocidade da Onda: {velocidade_onda} m/s")

def calcular_onda_senoidal(amplitude, frequencia, fase):
    try:
        amplitude = float(amplitude)
        frequencia = float(frequencia)
        fase = float(fase)
        
        resultado = f"A função da onda senoidal é: y = {amplitude}*sin({frequencia}*x + {fase})"

        label_resultado.config(text=resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

def calcular_bernoulli():
    try:
        P = float(entry_pressao.get())
        rho = float(entry_densidade.get())
        v = float(entry_velocidade.get())
        h = float(entry_altura.get())
        g = 9.81
        constante_bernoulli = P + 0.5 * rho * v**2 + rho * g * h
        label_resultado.config(text=f"A constante de Bernoulli é: {constante_bernoulli} Pa")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

def calcular_dilatacao_linear(comprimento_inicial, coeficiente_dilatacao, variacao_temperatura):
    try:
        delta_L = comprimento_inicial * coeficiente_dilatacao * variacao_temperatura
        label_resultado.config(text=f"Variação no Comprimento: {delta_L} m")
        texto = f"Variação no Comprimento: {delta_L} metros"
        
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

def calcular_dilatacao_volumetrica(volume_inicial, coeficiente_dilatacao_volumetrica, variacao_temperatura_volumetrica):
    try:
        delta_V = volume_inicial * coeficiente_dilatacao_volumetrica * variacao_temperatura_volumetrica
        label_resultado.config(text=f"Variação no Volume: {delta_V} m³")
        texto = f"Variação no Volume: {delta_V} m³"

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

def eletricidade(r, i):
    "u flaot, em volts, resistenc float ohml, corrente em amprere float"
    u = r * i
    return u

# Função para calcular eletricidade e mostrar o resultado
def calcular_eletricidade(resistencia, corrente):
    try:
        tensao = eletricidade(resistencia, corrente)
        messagebox.showinfo("Resultado", f"Tensão (V): {tensao}")
        texto = "Resultado", f"Tensão (V): {tensao}"
        
    except Exception as e:
        messagebox.showerror("Erro", str(e))


# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora Física")

# Onda Senoidal
frame_onda_senoidal = tk.Frame(root)
frame_onda_senoidal.pack(pady=10)
tk.Label(frame_onda_senoidal, text="Amplitude:").grid(row=0, column=0)
entry_amplitude = tk.Entry(frame_onda_senoidal)
entry_amplitude.grid(row=0, column=1)
tk.Label(frame_onda_senoidal, text="Frequência (Hz):").grid(row=1, column=0)
entry_frequencia_onda = tk.Entry(frame_onda_senoidal)
entry_frequencia_onda.grid(row=1, column=1)
tk.Label(frame_onda_senoidal, text="Fase (rad):").grid(row=2, column=0)
entry_fase = tk.Entry(frame_onda_senoidal)
entry_fase.grid(row=2, column=1)
btn_calcular_onda_senoidal = tk.Button(frame_onda_senoidal, text="Calcular Onda Senoidal", command=lambda: calcular_onda_senoidal(float(entry_amplitude.get()), float(entry_frequencia_onda.get()), float(entry_fase.get())))
btn_calcular_onda_senoidal.grid(row=3, columnspan=2, pady=5)

# Pressão
label_pressao = tk.Label(root, text="Pressão (Pa):")
label_pressao.pack(pady=10)
entry_pressao = tk.Entry(root)
entry_pressao.pack(pady=10)

# Densidade
label_densidade = tk.Label(root, text="Densidade (kg/m³):")
label_densidade.pack(pady=10)
entry_densidade = tk.Entry(root)
entry_densidade.pack(pady=10)

# Velocidade
label_velocidade = tk.Label(root, text="Velocidade (m/s):")
label_velocidade.pack(pady=10)
entry_velocidade = tk.Entry(root)
entry_velocidade.pack(pady=10)

# Altura
label_altura = tk.Label(root, text="Altura (m):")
label_altura.pack(pady=10)
entry_altura = tk.Entry(root)
entry_altura.pack(pady=10)

# Botão para calcular Bernoulli
botao_calcular = tk.Button(root, text="Calcular", command=calcular_bernoulli)
botao_calcular.pack(pady=10)

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

# Frame para Eletricidade
frame_eletricidade = tk.Frame(root)
frame_eletricidade.pack(pady=10)
tk.Label(frame_eletricidade, text="Resistência (Ω):").grid(row=0, column=0)
entry_resistencia = tk.Entry(frame_eletricidade)
entry_resistencia.grid(row=0, column=1)
tk.Label(frame_eletricidade, text="Corrente (A):").grid(row=1, column=0)
entry_corrente = tk.Entry(frame_eletricidade)
entry_corrente.grid(row=1, column=1)
btn_calcular_eletricidade = tk.Button(frame_eletricidade, text="Calcular Tensão (V)", command=lambda: calcular_eletricidade(float(entry_resistencia.get()), float(entry_corrente.get())))
btn_calcular_eletricidade.grid(row=2, columnspan=2, pady=5)

# Label para exibir o resultado
label_resultado = tk.Label(root, text="")
label_resultado.pack(pady=10)

root.mainloop()