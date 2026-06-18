import tkinter as tk
from tkinter import messagebox, ttk
import storage
import logic

class DiaryList:
    def __init__(self, ui):
        self.ui = ui
        self.ui.title("Мой Дневник Практики")
        self.ui.geometry("450x550")

        # Настройка стилей ttk
        style = ttk.Style()
        style.configure("TButton", padding=5)

        # Верхняя панель (Ввод)
        self.frame_top = ttk.LabelFrame(ui, text="Добавить данные")
        self.frame_top.pack(padx=10, pady=10, fill="x")

        ttk.Label(self.frame_top, text="Дата:").grid(row=0, column=0, padx=5, pady=5)
        self.val_date = ttk.Entry(self.frame_top)
        self.val_date.grid(row=0, column=1, sticky="ew")

        ttk.Label(self.frame_top, text="Работа:").grid(row=1, column=0, padx=5, pady=5)
        self.val_work = ttk.Entry(self.frame_top)
        self.val_work.grid(row=1, column=1, sticky="ew")

        ttk.Label(self.frame_top, text="Часы:").grid(row=2, column=0, padx=5, pady=5)
        self.val_hours = ttk.Entry(self.frame_top)
        self.val_hours.grid(row=2, column=1, sticky="ew")

        self.btn_add = ttk.Button(self.frame_top, text="Сохранить (AddRec)", command=self.AddRec)
        self.btn_add.grid(row=3, column=0, columnspan=2, pady=10)

        # Средняя панель (Список)
        self.frame_mid = ttk.LabelFrame(ui, text="Список выполненных работ")
        self.frame_mid.pack(padx=10, pady=5, fill="both", expand=True)

        self.box = tk.Listbox(self.frame_mid, font=("Arial", 10), selectmode=tk.SINGLE)
        self.box.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        
        # Студенты часто добавляют скроллбар через ttk
        scroll = ttk.Scrollbar(self.frame_mid, orient="vertical", command=self.box.yview)
        scroll.pack(side="right", fill="y")
        self.box.config(yscrollcommand=scroll.set)

        # Нижняя панель (Кнопки)
        self.frame_bot = ttk.Frame(ui)
        self.frame_bot.pack(pady=10)

        self.btn_del = ttk.Button(self.frame_bot, text="Удалить (DelRec)", command=self.DelRec)
        self.btn_del.pack(side="left", padx=5)

        self.btn_calc = ttk.Button(self.frame_bot, text="Итого часов", command=self.ShowSum)
        self.btn_calc.pack(side="left", padx=5)

        self.UpdateList()

    def UpdateList(self):
        self.box.delete(0, tk.END)
        items = logic.MakeList()
        for it in items:
            self.box.insert(tk.END, it)

    def AddRec(self):
        d = self.val_date.get()
        w = self.val_work.get()
        h = self.val_hours.get()

        if not d or not w or not h:
            messagebox.showwarning("Внимание", "Пустые поля!")
            return

        try:
            h_float = float(h)
            storage.SaveToFile(d, w, h_float)
            self.UpdateList()
            # Очистка
            self.val_work.delete(0, tk.END)
            self.val_hours.delete(0, tk.END)
        except:
            messagebox.showerror("Ошибка", "Часы должны быть числом")

    def DelRec(self):
        select = self.box.curselection()
        if select:
            idx = select[0]
            ok, name = logic.KillRecord(idx)
            if ok:
                messagebox.showinfo("Готово", f"Удалено: {name}")
                self.UpdateList()
        else:
            messagebox.showwarning("?", "Выделите строку для удаления")

    def ShowSum(self):
        total = logic.GetSum()
        messagebox.showinfo("Результат", f"Всего наработано: {total} ч.")

if __name__ == "__main__":
    ui = tk.Tk()
    app = DiaryList(ui)
    ui.mainloop()
