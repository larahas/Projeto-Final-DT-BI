import pandas as pd
import matplotlib.pyplot as plt 

## CARREGANDO OS ARQUIVOS CSV ##

df_query1 = pd.read_csv('query_1.csv')
df_query2 = pd.read_csv('query_2.csv')

print("1.VISUALIZAÇÃO DOS DADOS")
print("Dados de Salário por Departamento e Cargo (query_01.csv)")
print(df_query1.head())

print("Dados de Funcionários por Região (query_02.csv)")
print(df_query2.head())

print("2. CÁLCULO DAS MEDIDAS ESTATÍSTICAS BÁSICAS")
# Cálculo da Mádia, Mediana, Valor Mínimo e Valor Máximo dos Salários 
media_salario = df_query1['SALARY'].mean()
mediana_salario = df_query1['SALARY'].median()
min_salario = df_query1['SALARY'].min()
max_salario = df_query1['SALARY'].max()

print(f"Média Salarial: {media_salario}")
print(f"Mediana Salarial: {mediana_salario}")
print(f"Valor Mínimo Salarial: {min_salario}")
print(f"Valor Máximo Salarial: {max_salario}")

print("Resumo Estatístico dos Salários")
print(df_query1['SALARY'].describe())

# Média de salário por departamento
print("Média Salarial por Departamento")
media_dept = df_query1.groupby('DEPARTMENT_NAME')['SALARY'].mean()
print(media_dept)

print("3. VISUALIZAÇÃO GRÁFICA DOS DADOS")

# Gráfico 1: Histograma da Distribuição de Salários
plt.figure(figsize=(8, 5))
plt.hist(df_query1['SALARY'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribuição de Salários dos Funcionários')
plt.xlabel('Salário ($)')
plt.ylabel('Número de Funcionários')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('histograma_salarios.png') #Imagem salva na pasta do projeto
plt.show()

# Gráfico 2: Boxplot do Salário por Departamento
plt.figure(figsize=(10, 6))
df_query1.boxplot(column='SALARY', by='DEPARTMENT_NAME', grid=False)
plt.title('Distribuição e Variabilidade de Salários por Departamento')
plt.xlabel('Departamento')
plt.ylabel('Salário ($)')
plt.suptitle('')  # Remove o título automático
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('boxplot_salarios_departamento.png')  # Imagem salva na pasta do projeto
plt.show()
