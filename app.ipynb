import tkinter as tk
import a2i
from tkinter import filedialog
from tkinter.ttk import *
from PIL import Image

def convert_image(input_path, output_path, image_format):
    try:
        if image_format == "Grayscale":
            a2i.convert_apk_to_img(input_path,output_path)
        else:
            pass
        result_label.config(text="Chuyển đổi thành công!", fg="green")
    except Exception as e:
        result_label.config(text=f"Lỗi: {e}", fg="red")

def browse_file():
    file_path = filedialog.askopenfilename(title="Chọn file", filetypes=[("APK files", "*.apk")])
    input_entry.delete(0, tk.END)
    input_entry.insert(0, file_path)

def save_file():
    input_path = input_entry.get()
    image_format = select_type_img.get()
    output_path = filedialog.asksaveasfilename(title="Chọn nơi lưu", defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if input_path and output_path:
        convert_image(input_path, output_path, image_format)


# Tạo cửa sổ chính
root = tk.Tk()
root.title("Chuyển đổi ảnh PNG")

# Tạo và định vị các widget
input_label = tk.Label(root, text="Chọn tập tin apk:")
input_label.grid(row=0, column=0, padx=10, pady=10)

input_entry = tk.Entry(root, width=60)
input_entry.grid(row=0, column=1, padx=100, pady=10)

browse_button = tk.Button(root, text="Chọn", command=browse_file)
browse_button.grid(row=0, column=2, padx=10, pady=10)

select_type_img = Combobox(root, font = ('Arial',10),width = 20)
select_type_img['value'] = ('Grayscale','RGB')
select_type_img.grid(row=1, column=1, padx=10, pady=10)
select_type_img.current(0)
type = select_type_img.get()

convert_button = tk.Button(root, text="Chuyển đổi", command=save_file)
convert_button.grid(row=1, column=2, pady=10)

result_label = tk.Label(root, text="", fg="black")
result_label.grid(row=2, column=0, columnspan=3, pady=10)

# Bắt đầu vòng lặp sự kiện
root.mainloop()
