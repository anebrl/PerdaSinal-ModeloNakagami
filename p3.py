import numpy as np
import matplotlib.pyplot as plt

def nakagami_loss(frequency, distance, eta):
    c = 3e8  # Velocidade da luz (m/s)
    wavelength = c / frequency
    # Perda de percurso em espaço livre
    PL_free_space = 20 * np.log10((4 * np.pi * distance) / wavelength)
    # Ganho de desvanecimento Nakagami com η=1 (equivalente ao desvanecimento Rayleigh)
    nakagami_fading = np.random.gamma(eta, 1/eta, size=len(distance))
    # Perda total considerando Nakagami
    loss = PL_free_space - 10 * np.log10(nakagami_fading)
    return loss

# Parâmetros
freq = 2.6e9  # Frequência de 2.6 GHz (4G)
distances = np.arange(1, 1000, 100)  # Distâncias de 100 a 1000 metros
tx_power = 43  # Potência de transmissão de 20 dBm
sensitivity = -100  # Sensibilidade mínima do receptor
eta = 1 # entre 0.5 e 1, semelhante a Rayleigh
          # m = 1, Rayleigh
          # m > 1, desvanecimento é menos severo do que o desvanecimento Rayleigh
          # m >> 1, comunicação se comporta quase como um canal sem desvanecimento
# Cálculo da perda de percurso e potência recebida
losses = nakagami_loss(freq, distances, eta)
received_power = tx_power - losses  # Potência recebida em dBm

# Plot
plt.plot(distances, received_power, label="Potência Recebida (dBm)")
plt.axhline(y=sensitivity, color='r', linestyle='--', label="Sensibilidade Mínima (-100 dBm)")
plt.title("Potência Recebida vs. Distância (Modelo Nakagami, η=1, 2.6 GHz, 4G)")
plt.xlabel("Distância (m)")
plt.ylabel("Potência Recebida (dBm)")
plt.grid(True)
plt.legend()
plt.show()
