import json
import os
import matplotlib.pyplot as plt

FILE = "finance.json"


def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_data():
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(operations, f, ensure_ascii=False, indent=4)


operations = load_data()


def add_operation():
    kind = input("Доход или расход (д/р): ").lower()

    if kind not in ["д", "р"]:
        print("Неверный тип операции!")
        return

    try:
        amount = float(input("Сумма: "))
        if amount <= 0:
            print("Сумма должна быть больше нуля!")
            return
    except ValueError:
        print("Введите правильное число!")
        return

    category = input("Категория: ")

    operations.append({
        "type": kind,
        "amount": amount,
        "category": category
    })

    save_data()
    print("Операция сохранена!")


def show_balance():
    income = sum(
        x["amount"] for x in operations if x["type"] == "д"
    )
    expenses = sum(
        x["amount"] for x in operations if x["type"] == "р"
    )

    print("\n--- Финансы ---")
    print("Доходы:", round(income, 2))
    print("Расходы:", round(expenses, 2))
    print("Остаток:", round(income - expenses, 2))

    if expenses > income:
        print("Совет: расходы превышают доходы.")
    elif income > 0 and expenses / income >= 0.8:
        print("Совет: большая часть дохода уже потрачена.")
    else:
        print("Финансовая ситуация выглядит нормально.")


def show_operations():
    if not operations:
        print("Операций пока нет.")
        return

    for i, x in enumerate(operations, 1):
        kind = "Доход" if x["type"] == "д" else "Расход"
        print(
            f"{i}. {kind}: {x['amount']} - {x['category']}"
        )


def show_graph():
    income = sum(
        x["amount"] for x in operations if x["type"] == "д"
    )
    expenses = sum(
        x["amount"] for x in operations if x["type"] == "р"
    )

    plt.bar(
        ["Доходы", "Расходы"],
        [income, expenses]
    )
    plt.title("Доходы и расходы")
    plt.ylabel("Сумма")
    plt.show()


while True:
    print("\n=== FinTrack ===")
    print("1. Добавить операцию")
    print("2. Посмотреть баланс")
    print("3. Посмотреть операции")
    print("4. Показать график")
    print("0. Выход")

    choice = input("Выбери действие: ")

    if choice == "1":
        add_operation()
    elif choice == "2":
        show_balance()
    elif choice == "3":
        show_operations()
    elif choice == "4":
        show_graph()
    elif choice == "0":
        break
    else:
        print("Неверный пункт меню!")
