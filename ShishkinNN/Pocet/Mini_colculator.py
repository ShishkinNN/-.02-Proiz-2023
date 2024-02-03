import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        if operation_var.get() == "Сложение":
            result = num1 + num2
        elif operation_var.get() == "Вычитание":
            result = num1 - num2
        elif operation_var.get() == "Умножение":
            result = num1 * num2
        elif operation_var.get() == "Деление":
            if num2 == 0:
                messagebox.showerror("Ошибка", "Деление на ноль невозможно.")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Ошибка", "Выбрана некорректная операция.")
            return

        result_label.config(text=f"Результат: {result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите числовые значения.")

# Создаем главное окно
root = tk.Tk()
root.title("Мини-калькулятор")

# Ввод первого числа
label_num1 = tk.Label(root, text="Первое число:")
label_num1.grid(row=0, column=0, padx=10, pady=10)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

# Ввод второго числа
label_num2 = tk.Label(root, text="Второе число:")
label_num2.grid(row=1, column=0, padx=10, pady=10)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

# Выбор операции
label_operation = tk.Label(root, text="Выберите операцию:")
label_operation.grid(row=2, column=0, padx=10, pady=10)
operations = ["Сложение", "Вычитание", "Умножение", "Деление"]
operation_var = tk.StringVar(value=operations[0])
operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.grid(row=2, column=1, padx=10, pady=10)

# Кнопка для выполнения вычислений
calculate_button = tk.Button(root, text="Вычислить", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Метка для отображения результата
result_label = tk.Label(root, text="Результат: ")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Запускаем цикл обработки событий
root.mainloop()
