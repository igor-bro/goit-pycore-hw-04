def get_cats_info(path):
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    cat_id, name, age = parts
                    cats.append({"id": cat_id, "name": name, "age": age})
                else:
                    print(f"Увага: некоректний рядок - {line.strip()}")    

    except FileNotFoundError:
        print(f"Помилка: файл '{path}' не знайдено.")
    except Exception as e:
        print(f"Невідома помилка: {e}")
    return cats 

cats_info = get_cats_info("cats_file.txt")
print(cats_info)

