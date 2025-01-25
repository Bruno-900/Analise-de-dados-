import pandas as pd
import matplotlib.pyplot as plt

# Importar os dados com delimitador correto
dados = pd.read_csv("C:\\Users\\bruno\\OneDrive\\Ambiente de Trabalho\\UMC\\powerBI\\dados_marketing.csv", delimiter=';')

# Removendo duplicatas com base na coluna ID
dados = dados.drop_duplicates(subset='ID')

# Contando o número de clientes por país
contando_paises = dados['Pais'].value_counts()

# Contando o número de clientes por escolaridade
contando_escolaridade = dados['Escolaridade'].value_counts()

# Calculando a média salarial por país
media_salarial= dados.groupby('Pais')['Salario Anual'].mean()


# Criando a figura e os eixos para os gráficos de pizza
fig, axes = plt.subplots(1, 2, figsize=(14, 7))

# Gráfico de pizza para a distribuição por país
axes[0].pie(contando_paises.values, labels=contando_paises.index, autopct='%1.1f%%', startangle=90)
axes[0].set_title('Clientes por País')

# Gráfico de pizza para a distribuição por escolaridade
axes[1].pie(contando_escolaridade.values, labels=contando_escolaridade.index, autopct='%1.1f%%', startangle=90)
axes[1].set_title('Clientes por Escolaridade')

# Ajustando o layout
plt.tight_layout()
plt.show()