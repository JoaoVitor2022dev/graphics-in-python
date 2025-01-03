import matplotlib.pyplot as plt

numero_de_fatias = int(input("Quantas fatias do gráfico quer gerar?: "))

labels = []
sizes = []

for i in range(numero_de_fatias):
    label = input(f"Digite o rotulo para a fatia {i+1}: ")
    size = float(input(f"Digite o tamanho da fatia {i+1}: "))
    labels.append(label)
    sizes.append(size)

destacar = int(input(f"Qual fatia você quer destacar? (1 a {numero_de_fatias})")) - 1

explode = [0] * numero_de_fatias
explode[destacar] = 0.1

plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Gráficos Personalizados')
plt.axis('equal')
plt.show()


# EPLICAÇÃO DO GRAFICO 



