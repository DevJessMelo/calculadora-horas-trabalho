# Calculadora de Horas de Trabalho vs. Consumo

# Entrada de dados do usuário
salario = float(input("Digite o seu salário mensal (R$): "))
horas_semanais = float(input("Digite a quantidade de horas trabalhadas por semana: "))
preco_item = float(input("Digite o preço do item que deseja comprar (R$): "))

# Cálculos
# Considerando em média 4.33 semanas por mês
horas_mensais = horas_semanais * 4.33
valor_hora = salario / horas_mensais

horas_necessarias = preco_item / valor_hora
dias_trabalho = horas_necessarias / (horas_semanais / 5)

# Resultados
print("\n--- RESULTADO ---")
print(f"Sua hora de trabalho vale: R$ {valor_hora:.2f}")
print(f"Para comprar este item, você precisará trabalhar: {horas_necessarias:.1f} horas")
print(f"Isso equivale a aproximadamente {dias_trabalho:.1f} dias de trabalho.")
