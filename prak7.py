import json
import os
from datetime import datetime, timedelta


def check_file(): #проверка файна на наличие
    if os.path.exists("task.json"):
        with open("task.json", 'r') as taskjson:
            try:
                name = json.load(taskjson)
            except json.JSONDecodeError:
                name = []
    else:
        name = []
    return name

def output_view(pop, i):
    print("++++++++++++++++++++++++++++++++++++++++")
    print(f"Название - {pop.get("task_name")}, Номер - {i}")
    print(f"Дата создания - {pop.get("date_begin")}")
    print(f"Описание задачи - {pop.get("desc")}")
    print(f"Дата выполнения - {pop.get("date_end")}")
print("++++++++++++++++++++++++++++++++++++++++")


def input_json_file(): #добавление задач
    time = datetime.now()
    task = {
        "task_name": input("Введите название задачи: "),
        "date_begin": f"{time.year}-{time.month}-{time.day}",
        "desc": input("Введите описание: "),
        "date_end": input("Введите дату окончания (ГГГГ-ММ-ДД): ")
    }
    tasks = check_file()
    tasks.append(task)
    with open("task.json", 'w') as taskjson:
        json.dump(tasks, taskjson, indent=4, ensure_ascii=False)

def view_json_file(mode):
    time = datetime.now()
    view_task = check_file()
    if len(view_task) == 0:
        print("Файл пустой. Заполните, пожалуйста\n")

    if mode == 1:
        day = time
        print("Задачи на сегодня: ")
        for i in range(len(view_task)):
            input_str_date = datetime.fromisoformat(view_task[i]["date_end"])
            input_date = datetime.date(input_str_date)
            if input_date == day.date():
                pop = view_task[i]
                output_view(pop, i)

    if mode == 2:
        print("Задачи на завтра: ")
        day = time + timedelta(days=1)
        for i in range(len(view_task)):
            if time < datetime.fromisoformat(view_task[i]["date_end"]) < day:
                pop = view_task[i]
                output_view(pop, i)

    if mode == 3:
        print("Задачи на неделю: ")
        day = time + timedelta(days=6)
        for i in range(len(view_task)):
            input_str_date = datetime.fromisoformat(view_task[i]["date_end"])
            input_date = datetime.date(input_str_date)
            if time.date() <= input_date < day.date():
                pop = view_task[i]
                output_view(pop, i)

    if mode == 4:
        print("Предстоящие задачи: ")
        day = time
        for i in range(len(view_task)):
            input_str_date = datetime.fromisoformat(view_task[i]["date_end"])
            input_date = datetime.date(input_str_date)
            if input_date >= day.date():
                pop = view_task[i]
                output_view(pop, i)

    if mode == 5:
        print("Прошлые задачи: ")
        day = time
        for i in range(len(view_task)):
            input_str_date = datetime.fromisoformat(view_task[i]["date_end"])
            input_date = datetime.date(input_str_date)
            if input_date < day.date():
                pop = view_task[i]
                output_view(pop, i)

    if mode == 0:
        print("Все задачи: ")
        for i in range(len(view_task)):
            pop = view_task[i]
            output_view(pop, i)
    print("++++++++++++++++++++++++++++++++++++++++")

def edit_json():
    read_task = check_file()
    view_json_file(mode = 0)
    if len(read_task) == 0:
        print("Файл пустой. Заполните, пожалуйста\n")
    else:
        edit_num = int(input("Введите номер задачи для изменения: "))
        print("++++++++++++++++++++++++++++++++++++++++")
        print(f"Название - ",end="")
        read_task[edit_num]["task_name"] = input()
        print(f"Описание задачи - ",end="")
        read_task[edit_num]["desc"] = input()
        print(f"Дата выполнения - (ГГГГ-ММ-ДД) ",end="")
        read_task[edit_num]["date_end"] = input()
        print("++++++++++++++++++++++++++++++++++++++++")
        with open("task.json", 'w') as taskjson:
            json.dump(read_task, taskjson, indent=4, ensure_ascii=False)

def delete_json():
    read_task = check_file()
    view_json_file(mode=0)
    if len(read_task) == 0:
        print("Файл пустой. Заполните, пожалуйста\n")
    else:
        delete_num = int(input("Введите номер задачи для удаления: "))
        read_task.pop(delete_num)
        print("Удалено!")
        with open("task.json", 'w') as taskjson:
            json.dump(read_task, taskjson, indent=4, ensure_ascii=False)


if not os.path.exists("task.json"):
    print("Файл task.json будет создан, так как его нет.\n")
else:
    print("Файл task.json уже существует.\n")
def main():
    num_input_var = 1
    while num_input_var != 0:
        today = datetime.now()
        print("-----------------------------------------")
        print(f"Сегодня: {today.year}-{today.month}-{today.day}\n")
        print("Добавить задачу в ежедневник - Введите 1")
        print("Очистить ежедневник - Введите -1")
        print("Завершение работы - Введите 0")
        print("Все записи - Введите 2")
        print("Записи на сегодня - Введите 3")
        print("Записи на завтра - Введите 4")
        print("Записи на неделю - Введите 5")
        print("Отредактировать запись - Введите 6")
        print("Удалить запись - Введите 7")
        print("Посмотреть все предстоящие задачи - Введите 8")
        print("Посмотреть все предыдущие задачи - Введите 9")
        print("-----------------------------------------")
        try:
            num_input_var = int(input())
            print("-----------------------------------------")
        except ValueError:
            print("Пожалуйста, введите корректный номер задачи\n")
            print("-----------------------------------------")

        if num_input_var == -1:
            with open("task.json", 'w') as task_json:
                print("Файл task.json очищен.\n")

        elif num_input_var == 1:
            input_json_file()
        elif num_input_var == 2:
            view_json_file(mode=0)
        elif num_input_var == 3:
            view_json_file(mode=1)
        elif num_input_var == 4:
            view_json_file(mode=2)
        elif num_input_var == 5:
            view_json_file(mode=3)
        elif num_input_var == 6:
            edit_json()
        elif num_input_var == 7:
            delete_json()
        elif num_input_var == 8:
            view_json_file(mode=4)
        elif num_input_var == 9:
            view_json_file(mode=5)
            
    else:
        print("До свидания!")

if __name__ == "__main__":
    main()

