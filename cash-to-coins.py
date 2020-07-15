dollarAmount = 8.69

piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}

# Your magic Python code here


def calc_coins(dollarAmount):
    coins = dollarAmount*100
    piggyBank["quarters"] = int(coins // 25)
    coins = coins - piggyBank["quarters"]*25
    piggyBank["dimes"] = int(coins // 10)
    coins = coins - piggyBank["dimes"]*10
    piggyBank["nickels"] = int(coins // 5)
    coins = coins - piggyBank["nickels"]*5
    piggyBank["pennies"] = int(coins // 1)
    print(piggyBank)


calc_coins(dollarAmount)
