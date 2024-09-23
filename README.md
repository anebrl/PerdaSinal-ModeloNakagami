# PerdaSinal-ModeloNakagami
Simulação de Perda de Sinal em Canal Wireless (Modelo Nakagami)
Descrição
Este código Python simula a perda de sinal em um canal de comunicação wireless, considerando o modelo de desvanecimento Nakagami-m. O modelo de Nakagami é frequentemente utilizado para modelar canais com multicaminho severo, como em ambientes urbanos.

### Pré-requisitos
Python 3.x
### Bibliotecas: 
NumPy, Matplotlib

### Instalação
Para instalar as bibliotecas necessárias, execute o seguinte comando em seu terminal: pip install numpy matplotlib

Clone este repositório ou salve o código como um arquivo Python (por exemplo, simulacao_canal.py).
Execute o código utilizando um ambiente Python: python simulacao_canal.py

### Visualize o gráfico: 
Um gráfico será exibido mostrando a potência recebida em função da distância.

### Parâmetros Ajustáveis
freq: Frequência de operação (Hz)
distances: Vetor de distâncias (m)
tx_power: Potência de transmissão (dBm)
sensitivity: Sensibilidade mínima do receptor (dBm)
eta: Parâmetro de forma do desvanecimento Nakagami (ajusta a severidade do desvanecimento)

### Explicação do Código
Função nakagami_loss: Calcula a perda de sinal total, considerando a perda por espaço livre e o desvanecimento Nakagami.
Cálculo da potência recebida: Calcula a potência recebida subtraindo a perda da potência transmitida.
Visualização: Plota um gráfico da potência recebida em função da distância.

### Modelo Nakagami
O modelo Nakagami é uma generalização do modelo Rayleigh e é frequentemente utilizado para modelar canais com multicaminho severo. O parâmetro eta controla a severidade do desvanecimento:

eta = 1: Desvanecimento Rayleigh
eta > 1: Desvanecimento menos severo que Rayleigh
eta >> 1: Canal quase sem desvanecimento

### Aplicações
Planejamento de sistemas de comunicação wireless: Avaliar a cobertura e a qualidade do serviço em diferentes cenários.
Simulação de redes celulares: Analisar o desempenho de diferentes tecnologias e algoritmos.
Estudo de propagacao de ondas eletromagnéticas: Investigar os efeitos do ambiente na propagação de sinais.

### Possíveis Melhorias
Adicionar outros modelos de desvanecimento: Implementar modelos como Rice, lognormal, etc.
Considerar a sombragem: Adicionar um componente de sombragem para simular variações lentas na perda de sinal.
Análise estatística: Calcular métricas como a probabilidade de cobertura e a taxa de erro de bit.
Interface gráfica: Criar uma interface para permitir que o usuário ajuste os parâmetros interativamente.
