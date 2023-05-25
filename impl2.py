import numpy as np
import matplotlib.pyplot as plt

def dtft(x, n, k):
    # Função para estimar a TFTD de uma sequência de duração finita
    # Parâmetros de entrada:
    # - x: vetor de entrada contendo a sequência a ser transformada
    # - n: vetor contendo os índices de tempo correspondentes à sequência x
    # - k: vetor contendo os índices de frequência para os quais a TFTD será estimada
    # Parâmetros de saída:
    # - X: vetor contendo a estimativa da TFTD

    X = np.zeros(len(k), dtype=complex)  # inicializar vetor de saída com zeros

    # Loop sobre os índices de frequência k
    for idx in range(len(k)):
        # Calcular a contribuição da sequência x para a frequência k[idx]
        X[idx] = np.sum(x * np.exp(-1j * 2 * np.pi * k[idx] * n))

    return X

# Parâmetros da sequência
n = np.arange(1, 10)  # vetor de índices de tempo
x = (0.9 * np.exp(1j * np.pi/3))**n  # sequência x[n]

# Parâmetros para a estimativa da TFTD
N = 1000  # número de pontos para a estimativa da TFTD
k = np.arange(-N//2, N//2)  # vetor de índices de frequência para a estimativa

# Estimar a TFTD da sequência
X = dtft(x, n, k)

# Plotar o módulo da TFTD
plt.figure()
plt.plot(k, np.abs(X))
plt.xlabel('Índice de Frequência (k)')
plt.ylabel('|X(k)|')
plt.title('Estimativa da TFTD de x[n] = (0.9 exp(jπ/3))^n')
plt.show()
