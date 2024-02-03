import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import traceback

def send_request():
    messagebox.showinfo("Заявка принята", "Вам перезвонит специалист в течение 30 минут")

root = tk.Tk()
root.title("Приложение для компании ООО Реград МСК")

try:
    # Определяем начальные размеры окна
    initial_width, initial_height = 1600, 940

    # Загрузка изображения фона и изменение его размера
    background_image = Image.open("C:/PyThon/ShishkinNN/images/Fon.png")
    background_image = background_image.resize((initial_width, initial_height), Image.ANTIALIAS)

    # Преобразование изображения фона в формат PhotoImage для tkinter
    background_img = ImageTk.PhotoImage(background_image)

    # Установка размеров окна приложения
    root.geometry(f"{initial_width}x{initial_height}")

    # Создание виджета Canvas
    canvas = tk.Canvas(root, width=initial_width, height=initial_height)
    canvas.pack()

    # Отображение фона
    canvas.create_image(0, 0, anchor=tk.NW, image=background_img, tags="bg_images")

    # Загрузка и изменение размеров изображения background2.png
    background2_image = Image.open("C:/PyThon/ShishkinNN/images/Logo.png")
    background2_image = background2_image.resize((500, 300), Image.ANTIALIAS)
    background2_img = ImageTk.PhotoImage(background2_image)

    # Загрузка и изменение размеров изображения background3.png
    background3_image = Image.open("C:/PyThon/ShishkinNN/images/Fon2.png")
    background3_image = background3_image.resize((500, 300), Image.ANTIALIAS)
    background3_img = ImageTk.PhotoImage(background3_image)

    # Отображение background2.png в правом нижнем углу
    bottom_right_image_id = canvas.create_image(1600, 940, anchor=tk.SE, image=background2_img, tags="images")

    # Функция для смены изображений каждые 5 секунд
    def change_images():
        current_image_id = bottom_right_image_id
        current_image = canvas.itemcget(current_image_id, "image")
        next_image = background3_img if current_image == str(background2_img) else background2_img
        canvas.itemconfig(current_image_id, image=next_image)
        root.after(5000, change_images)  # Вызов функции через 5 секунд

    # Запуск смены изображений
    root.after(5000, change_images)

    # Добавим рамку вокруг формы для заявки
    form_frame = tk.Frame(root, bd=2, relief=tk.SOLID)
    form_frame.place(x=20, y=20, width=250, height=150)

    name_label = tk.Label(form_frame, text="Имя:")
    name_label.grid(row=0, column=0, padx=5, pady=5)

    name_entry = tk.Entry(form_frame)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    phone_label = tk.Label(form_frame, text="Номер телефона:")
    phone_label.grid(row=1, column=0, padx=5, pady=5)

    phone_entry = tk.Entry(form_frame)
    phone_entry.grid(row=1, column=1, padx=5, pady=5)

    submit_button = tk.Button(form_frame, text="Отправить заявку", command=send_request)
    submit_button.grid(row=2, columnspan=2, padx=5, pady=5)

    # Реализация возможности перемещения формы
    def move_start(event):
        form_frame.x = event.x
        form_frame.y = event.y

    def move_drag(event):
        form_frame.place(x=root.winfo_pointerx() - root.winfo_rootx() - form_frame.x,
                         y=root.winfo_pointery() - root.winfo_rooty() - form_frame.y,
                         anchor=tk.NW)

    form_frame.bind("<Button-1>", move_start)
    form_frame.bind("<B1-Motion>", move_drag)

    root.mainloop()

except Exception as e:
    traceback.print_exc()
    print("Ошибка при загрузке и изменении размеров изображения фона, Fon.png и Fon2.png:", e)