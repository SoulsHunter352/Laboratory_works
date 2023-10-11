salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0  # Подушка безопасности
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
for i in range(months):
    differance = salary - spend  # Разница между зарплатой и тратами
    if differance < 0:
        money_capital -= differance
    spend *= (1 + 0.03)  # Затраты в следующем месяце
money_capital = int(money_capital)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
