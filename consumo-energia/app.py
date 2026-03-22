# Programa de cálculo de consumo de energia
# Autor: Lucas Santos Silva

# Entrada
aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência (em watts): "))
horas_dia = float(input("Digite o tempo médio de uso diário (em horas): "))

# Processamento
consumo_mensal = (potencia * horas_dia * 30) / 1000
custo_mensal = consumo_mensal * 0.70

# Saída
print(f"\nO aparelho {aparelho} consome em média {consumo_mensal:.2f} kWh/mês.")
print(f"Em São Paulo, o custo estimado é de R$ {custo_mensal:.2f} por mês.")