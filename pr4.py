
prices = {
    "хліб": 25,
    "молоко": 42,
    "яйця": 60,
    "цукор": 30,
    "кава": 150,
    "масло": 80
}

store_items = {
    "хліб": True,
    "молоко": True,
    "яйця": False,
    "цукор": True,
    "кава": False,
    "масло": True
}


def format_price(price):
    return f"ціна: {price:.2f} грн"



def check_items_availability(*items):
    result = {}
    for item in items:
        result[item] = store_items.get(item, False)
    return result



def make_order(order_list):
    availability = check_items_availability(*order_list)

    # які товари відсутні
    missing = [item for item, available in availability.items() if not available]

    if missing:
        return f"Неможливо оформити замовлення. Немає в наявності: {', '.join(missing)}"

    # обчислюємо загальну суму
    total = sum(prices[item] for item in order_list)
    return f"Ваше замовлення доступне. {format_price(total)}"



def user_menu():
    print("Вітаємо в магазині!")
    print("1 — Купити")
    print("2 — Переглянути ціну товарів")

    choice = input("Ваш вибір: ")

    if choice == "1":
        items = input("Введіть товари через кому: ").lower().split(",")
        items = [i.strip() for i in items]
        print(make_order(items))

    elif choice == "2":
        items = input("Введіть товари через кому: ").lower().split(",")
        items = [i.strip() for i in items]

        for item in items:
            if item in prices:
                print(f"{item}: {format_price(prices[item])}")
            else:
                print(f"{item}: товару немає в каталозі")

    else:
        print("Невірний вибір.")

if __name__ == "__main__":
    user_menu()
