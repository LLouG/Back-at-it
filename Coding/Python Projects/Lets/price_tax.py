
game_prices = {
    "Blasphemous": 33,
    "Bloodstained": 75,
    "La-Mulana": 27,
    "Timespinner": 36,
    "Factorio": 101,
    "Rimworld": 79,
}

# tax = []
# for game in game_prices:
#     tax.append(game_prices[game] * 0.1)
# print(tax)

tax = [game_prices[game] * 0.1 for game in game_prices]  # List comprehension
print(tax)


sales = 1000
meta = 500

# if sales >= meta:
#     bonus = 30
# else:
#     bonus = 0

bonus = 30 if sales >= meta else 0  # Ternary Operator
print(bonus)
