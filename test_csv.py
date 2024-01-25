import csv
from uuid import UUID

users_filepath = "./users.csv"
stocks_filepath = "./stocks.csv"
items_filepath = "./items.csv"


with open(users_filepath, encoding="UTF-8", mode="r") as users_file:
    users = csv.DictReader(users_file)
    for user in users:
        user_id = user["user_id"]
        try:
            user_id = UUID(user_id)
            print(user_id)
        except ValueError:
            print("Невадильный тип данных")

with open(stocks_filepath, encoding="UTF-8", mode="r") as stocks_file:
    stocks = csv.DictReader(stocks_file)
    for stock in stocks:
        stock_id = stock["stock_id"]
        try:
            stock_id = UUID(stock_id)
            print(stock_id)
        except ValueError:
            print("Невалидный тип данных")
        capacity_sq_m = stock[" capacity_sq_m"]
        try:
            capacity_sq_m = float(capacity_sq_m)
            print(capacity_sq_m)
        except ValueError:
            print("Невалидный тип данных")
        owner_id = stock[" owner_id"]
        try:
            owner_id = int(owner_id)
            print(owner_id)
        except ValueError:
            print("Невалидный тип данных")


def add():
    pass
