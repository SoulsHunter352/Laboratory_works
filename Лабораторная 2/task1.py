money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count_months_without_dept = 0  # Количество месяцев без долгов
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
budget = money_capital
while budget > 0:
    if budget + (salary - spend) < 0:
        break
    budget += salary - spend  # Бюджет после текущего месяца
    count_months_without_dept += 1
    spend *= (increase + 1)  # Затраты в следующем месяце
print("Количество месяцев, которое можно протянуть без долгов:", count_months_without_dept)
