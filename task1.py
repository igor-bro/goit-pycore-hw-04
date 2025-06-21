def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            total = 0
            count = 0

            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    try:
                        salary = float(parts[1])
                        total += salary
                        count += 1
                    except ValueError:
                        print(f"Увага: некоректна зарплата у рядку: {line.strip()}")
                else:
                    print(f"Увага: некоректний формат рядка: {line.strip()}")
            
            if count == 0:
                return 0, 0

            average = total / count
            return total, average

    except FileNotFoundError:
        print(f"Помилка: файл '{path}' не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Невідома помилка: {e}")
        return 0, 0

# Приклад виклику
total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
