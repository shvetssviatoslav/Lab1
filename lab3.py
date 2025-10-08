student_magazine = {}
while True:
    print("Виберіть дію:")
    print("1.Додати нового студента")
    print("2.Вивести журнал студентів")
    print("3.Вивести середній бал студентів")
    print("4.Вивести категорії студентів за оцінками")
    print("Щоб вийти з програми введіть (stop)")
    choice = input("_> ")
    if choice == "1":
        name = input("Введіть ім'я студента: ")
        mark = int(input("Введіть оцінку студента: "))
        if mark < 1 or mark > 12:
            print("Такої оцінки не існує")
        else:
            student_magazine[name] = mark
    elif choice == "2":
        if not student_magazine:
            print("Список студентів порожній.")
        else:
            print("Список успішності студентів:")
            for name, mark in student_magazine.items():
                print(f"{name}: {mark}")
    elif choice == "3":
        if not student_magazine:
            print("Список студентів порожній.")
        else:
            ball = sum(student_magazine.values()) / len(student_magazine)
            print(f"Середній бал серед студентів - {ball}")
    elif choice == "4":
        if not student_magazine:
            print("Список студентів порожній.")
        else:
            excellent = []
            good = []
            struggling = []
            failed = []
            for name in student_magazine:
                mark = student_magazine[name]
                if 10 <= mark <= 12:
                    excellent.append(name)
                elif 7 <= mark <= 9:
                    good.append(name)
                elif 4 <= mark <= 6:
                    struggling.append(name)
                elif 1 <= mark <= 3:
                    failed.append(name)
            print(f"Відмінники (10-12): {len(excellent)} ( {', '.join(excellent)})")
            print(f"Хорошисти (7-9): {len(good)} ( {', '.join(good)})")
            print(f"Відстаючі (4-6): {len( struggling)} ( {', '.join( struggling) })")
            print(f"Не здали (1-3): {len(failed)} ({', '.join(failed) })")
    elif choice.lower() == "stop":
        print("Дякую що відвідали нашу програму")
        break
    else:
        print("Ви ввели неправильну дію. Спробуйте ще раз")


