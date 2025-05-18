
korystuvachi = {
    "Андрій": "Дорослий",
    "Марія": "Підліток",
    "Олег": "Дитина",
    "Ірина": "Дорослий"
}


imya = input("Введіть ім'я користувача: ")


if imya in korystuvachi:
    print(f"{imya} належить до вікової групи: {korystuvachi[imya]}")
else:
    print(f"Інформацію про користувача з іменем {imya} не знайдено.")
