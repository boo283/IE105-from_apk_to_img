import tkinter as tk
import a2i, os
from tkinter import filedialog
from tkinter.ttk import *

def convert_image(input_path, output_path):
    try:
        image_format = select_type_img.get()
        msg, colorMsg = "Chuyển đổi thành công!", "green"
        if os.path.isfile(input_path):
            a2i.convert_apk_to_img(input_path, output_path, image_format)
        elif os.path.isdir(input_path):
            a2i.convert_apks_to_imgs(input_path, output_path, image_format)
        else:
            msg, colorMsg = "Vui lòng kiểm tra lại đường dẫn", "red"
        result_label.config(text=msg, fg=colorMsg)
    except Exception as e:
        result_label.config(text=f"Lỗi: {e}", fg="red")

def browse_file():
    input_path = None
    input_type = select_input.get()
    if input_type == "Chọn tập tin apk":
        input_path = filedialog.askopenfilename(title="Chọn file", filetypes=[("APK files", "*.apk")])
    else:
        input_path = filedialog.askdirectory(title="Chọn thư mục")
    input_entry.delete(0, tk.END)
    input_entry.insert(0, input_path)
def browse_output():
    folder_path = filedialog.askdirectory(title="Chọn thư mục")
    output_entry.delete(0, tk.END)
    output_entry.insert(0, folder_path)
def save_file():
    input_path = input_entry.get()
    output_path = output_entry.get()
    if input_path and output_path:
        convert_image(input_path, output_path)
    else:
        result_label.config(text="Vui lòng chọn đường dẫn", fg="red")


# Tạo cửa sổ chính
root = tk.Tk()
root.title("Chuyển đổi tập tin APK sang ảnh PNG")

# Tạo và định vị các widget

select_input = Combobox(root, font = ('Arial',10),width = 30)
select_input['value'] = ('Chọn tập tin apk','Chọn thư mục chứa tập tin apk')
select_input.grid(row=0, column=0, padx=10, pady=10)
select_input.current(0)


input_entry = tk.Entry(root, width=60)
input_entry.grid(row=0, column=1, padx=10, pady=10)

output_label = tk.Label(root, text="Chọn thư mục lưu:")
output_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
output_entry = tk.Entry(root, width=60)
output_entry.grid(row=1, column=1, padx=10, pady=10)

browse_output_file_button = tk.Button(root, text="Chọn", command=browse_output)
browse_output_file_button.grid(row=1, column=2, padx=10, pady=10)

browse_button = tk.Button(root, text="Chọn", command=browse_file)
browse_button.grid(row=0, column=2, padx=10, pady=10)

select_type_img = Combobox(root, font = ('Arial',10),width = 20)
select_type_img['value'] = ('Grayscale','RGB')
select_type_img.grid(row=2, column=1, padx=10, pady=10)
select_type_img.current(0)

convert_button = tk.Button(root, text="Chuyển đổi", command=save_file)
convert_button.grid(row=3, column=1, pady=10)

result_label = tk.Label(root, text="", fg="black")
result_label.grid(row=4, column=0, columnspan=3, pady=10)

# Bắt đầu vòng lặp sự kiện
root.mainloop()
