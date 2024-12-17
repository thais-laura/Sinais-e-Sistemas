# Dupla: Gabriella Castelari (14755082) e Thaís Laura (14608765)
# O programa realiza a convolução de sinais e plota estes e o resultado final

import numpy as np
import matplotlib.pyplot as plt 

def plota(intervalo, sinal, titulo):
    plt.plot(intervalo, sinal)
    plt.title(titulo)
    plt.xlabel("Índice")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.show()
    
def conv(sinal1, sinal2, x_vals1, x_vals2, titulo):
    n = len(sinal1) + len(sinal2) - 1
    c = np.zeros(n)
    
    # Calcula a convolução
    for i in range(n):                   # Pontos onde os sinais são diferentes de 0
        for j in range(len(sinal1)):     # Pontos do sinal 1
            if 0<= i - j < len(sinal2):  # Verifica se o índice i-j está dentro dos limites
                c[i] += sinal1[j] * sinal2[i - j]    # O sinal 2 é invertido e transladado
        
    x_min = x_vals1[0] + x_vals2[0]    # Limite inferior
    x_max = x_vals1[-1] + x_vals2[-1]  # Limite superior
    # Criação do intervalo do sinal gerado pela convolução
    x_conv = np.linspace(x_min, x_max, len(c))

    # Plota o gráfico
    plota(x_conv, c, titulo)

def sinalPulso(x, largura, amplitude, atraso):
    return 0 if x < (-largura + atraso) or x > (largura + atraso) else amplitude

def main():
    # Características 1
    larg1 = 20
    atr1 = 0
    amplt1 = 5
    # Características 2
    larg2 = 10
    atr2 = -20
    amplt2 = 10
    
    # Intervalo do sinal
    x_vals = np.arange(-50, 50, 0.1)  

    # Definições dos pulsos com diferentes características
    p1 = np.array([sinalPulso(x, larg1, amplt1, atr1 ) for x in x_vals])
    p2 = np.array([sinalPulso(x, larg1, amplt2, atr1) for x in x_vals])
    p3 = np.array([sinalPulso(x, larg1, -amplt2, atr1) for x in x_vals])
    p4 = np.array([sinalPulso(x, larg1, amplt1, atr2) for x in x_vals])
    p5 = np.array([sinalPulso(x, larg2, amplt1, atr1) for x in x_vals])
    
    # Gráficos dos pulsos
    plota(x_vals, p1, "Pulso 1")
    plota(x_vals, p2, "Pulso 2")
    plota(x_vals, p3, "Pulso 3")
    plota(x_vals, p4, "Pulso 4")
    plota(x_vals, p5, "Pulso 5")
    
    # Testes: pulso <conv> pulso
    conv(p1, p1, x_vals, x_vals, "Pulsos iguais")
    conv(p1, p2, x_vals, x_vals, "Pulsos com diferença de amplitude (positiva)")  
    conv(p1, p3, x_vals, x_vals, "Pulsos com diferença de amplitude (negativa)")  
    conv(p1, p4, x_vals, x_vals, "Pulsos com diferença de fase")   
    conv(p1, p5, x_vals, x_vals, "Pulsos com diferença de largura")
    

if __name__ == "__main__":
    main()
