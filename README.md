# Metanit PHP Python Scraper

Цей Python скрипт автоматично завантажує уроки з PHP з сайту [metanit.com](https://metanit.com/php/tutorial/), структуровано зберігає їх у локальні HTML-файли, створюючи директорії для кожного розділу. Скрипт написаний з допомогою `штучного інтелекту`, так як я не розробник Python. Тож багато чого може бути покращено.

## Опис

Скрипт виконує наступні дії:
1. Завантажує головну сторінку з уроками.
2. Збирає всі URL-адреси уроків.
3. Завантажує контент кожного уроку.
4. Очищує контент від небажаних елементів.
5. Зберігає контент у вигляді HTML-файлів у відповідні директорії.

## Вимоги

Для запуску скрипту необхідно мати встановлені наступні бібліотеки Python:

- `requests`
- `beautifulsoup4`

## Встановлення

To use the Metanit PHP Python Parser, follow these steps:

1. Клонуйте репозиторій:
    ```sh
    git clone https://github.com/cirin0/php-metanit-scraper.git
    cd php-lessons-scraper
    ```

2. Створіть віртуальне середовище (рекомендовано) та активуйте його:
    ```sh
    python -m venv venv
    source venv/bin/activate  # Для Windows: venv\Scripts\activate
    ```
3.  Встановіть необхідні бібліотеки:
    ```sh
    pip install -r requirements.txt
    ```

## Запуск

Для запуску скрипту виконайте:
```sh
python main.py
```

