import tkinter as tk
from tkinter import messagebox 
from ttkbootstrap import ttk, Style

#estas variables tengo que cambiarlas a dinamicas para q el user elija
tiempo_trabajo = 25 * 60
descanso_corto = 5 *60
descanso_largo = 15 * 60

class Pomodoro: 
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x320")
        self.root.title("cronometro pomodoro")
        self.style = Style(theme="simplex")
        self.style.theme_use()


        #entradas de tiempo por el usuario
        

        self.timer_label = tk.Label(self.root, text="", font=("TkDefaultFont", 40))
        self.timer_label.pack(pady=20)

        self.start_button = ttk.Button(self.root, text="Iniciar", command=self.start_timer)
        self.start_button.pack(pady = 5)

        self.stop_button = ttk.Button(self.root, text = "Parar", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        self.work_time, self.break_time = tiempo_trabajo, descanso_corto
        self.is_work_time, self.pomodoros_completed, self.is_running = True, 0, False

        self.root.mainloop()

    def start_timer(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.is_running = True
        self.update_timer()

    def stop_timer(self):
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.is_running = False

    def update_timer(self):
        if self.is_running:
            if self.is_work_time:
                self.work_time -= 1
                if self.work_time == 0:
                    self.is_work_time = False
                    self.pomodoros_completed += 1
                    self.break_time = descanso_largo if self.pomodoros_completed % 4 == 0 else descanso_corto 
                    messagebox.showinfo("pudiste pa" if self.pomodoros_completed % 4 ==0
                                        else "pudisteee", "PERO hace un descanso largo, tu mente lo necesita"
                                        if self.pomodoros_completed % 4 == 0
                                        else "descansemos x 5 min y sali a estirar las piernas")
                
                else: 
                    self.break_time -= 1
                    if self.break_time == 0:
                        self.is_work_time, self.work_time = True, tiempo_trabajo
                        messagebox.showinfo("a laburarrr", "no seas flojo")
                minutes, seconds = divmod(self.work_time if self.is_work_time else self.break_time, 60)
                self.timer_label.config(text="{:02d}:{:02d}".format(minutes, seconds))
                self.root.after(1000, self.update_timer)

Pomodoro()
  