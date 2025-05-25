import logging

#
logging.basicConfig(
    filename='error_log.txt',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Результат: {result}")
    except Exception as e:
        logging.error("Помилка при діленні чисел", exc_info=True)
        print("Виникла помилка. Деталі записані у файл 'error_log.txt'.")

divide_numbers(10, 0)
