"GRAFICOS COM PYTHON"
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = x ** 2

plt.plot(x, y ,color='red', linestyle='--', label='y = x^2')
plt.title("Gráficos em linhas simples")
plt.xlabel("EIXO X")
plt.ylabel("EIXO Y")
plt.grid(True)

plt.show() 


