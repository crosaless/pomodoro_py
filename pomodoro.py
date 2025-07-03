import tkinter as tk
from tkinter import messagebox 
from ttkbootstrap import ttk, Style
import winsound  
import datetime
import json
import os

class Pomodoro: 
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x500")
        self.root.title("Cronómetro Pomodoro")
        self.style = Style(theme="simplex")
        self.style.theme_use()

        # Variables para estadísticas
        self.stats_file = "pomodoro_stats.json"
        self.load_stats()

        # Crear interfaz
        self.create_widgets()
        
        # Variables de control
        self.work_time = 25 * 60
        self.short_break = 5 * 60
        self.long_break = 15 * 60
        self.break_time = self.short_break
        self.is_work_time = True
        self.pomodoros_completed = 0
        self.is_running = False
        self.current_time = 0

        self.root.mainloop()

    def create_widgets(self):
        # Frame para configuración
        config_frame = ttk.LabelFrame(self.root, text="Configuración (minutos)", padding=10)
        config_frame.pack(pady=10, padx=10, fill="x")

        # Entradas de tiempo
        ttk.Label(config_frame, text="Minutos de trabajo:").grid(row=0, column=0, sticky="w", pady=2)
        self.input_trabajo = ttk.Entry(config_frame, width=10)
        self.input_trabajo.insert(0, "25")
        self.input_trabajo.grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(config_frame, text="Descanso corto:").grid(row=1, column=0, sticky="w", pady=2)
        self.input_corto = ttk.Entry(config_frame, width=10)
        self.input_corto.insert(0, "5")
        self.input_corto.grid(row=1, column=1, padx=5, pady=2)

        ttk.Label(config_frame, text="Descanso largo:").grid(row=2, column=0, sticky="w", pady=2)
        self.input_largo = ttk.Entry(config_frame, width=10)  # ¡Aquí estaba el error!
        self.input_largo.insert(0, "15")
        self.input_largo.grid(row=2, column=1, padx=5, pady=2)

        # Timer display
        self.timer_label = tk.Label(self.root, text="25:00", font=("Arial", 36, "bold"))
        self.timer_label.pack(pady=20)

        # Estado actual
        self.status_label = tk.Label(self.root, text="Listo para trabajar", font=("Arial", 12))
        self.status_label.pack(pady=5)

        # Botones
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=10)

        self.start_button = ttk.Button(button_frame, text="Iniciar", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = ttk.Button(button_frame, text="Parar", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=5)

        self.reset_button = ttk.Button(button_frame, text="Reiniciar", command=self.reset_timer)
        self.reset_button.pack(side=tk.LEFT, padx=5)

        # Frame de estadísticas
        stats_frame = ttk.LabelFrame(self.root, text="Estadísticas", padding=10)
        stats_frame.pack(pady=10, padx=10, fill="x")

        self.stats_today = ttk.Label(stats_frame, text="Hoy: 0 pomodoros")
        self.stats_today.pack(anchor="w")

        self.stats_total = ttk.Label(stats_frame, text="Total: 0 pomodoros")
        self.stats_total.pack(anchor="w")

        self.stats_streak = ttk.Label(stats_frame, text="Racha: 0 días")
        self.stats_streak.pack(anchor="w")

        # Botón para limpiar estadísticas
        ttk.Button(stats_frame, text="Limpiar Estadísticas", command=self.clear_stats).pack(pady=5)

        self.update_stats_display()

    def load_stats(self):
        """Carga las estadísticas desde archivo"""
        if os.path.exists(self.stats_file):
            try:
                with open(self.stats_file, 'r') as f:
                    self.stats = json.load(f)
            except:
                self.stats = {"daily": {}, "total": 0, "last_date": ""}
        else:
            self.stats = {"daily": {}, "total": 0, "last_date": ""}

    def save_stats(self):
        """Guarda las estadísticas en archivo"""
        try:
            with open(self.stats_file, 'w') as f:
                json.dump(self.stats, f)
        except:
            pass

    def update_stats_display(self):
        """Actualiza la visualización de estadísticas"""
        today = datetime.date.today().isoformat()
        today_count = self.stats["daily"].get(today, 0)
        
        self.stats_today.config(text=f"Hoy: {today_count} pomodoros")
        self.stats_total.config(text=f"Total: {self.stats['total']} pomodoros")
        
        # Calcular racha
        streak = self.calculate_streak()
        self.stats_streak.config(text=f"Racha: {streak} días")

    def calculate_streak(self):
        """Calcula la racha de días consecutivos"""
        today = datetime.date.today()
        streak = 0
        
        for i in range(365):  # Máximo 365 días
            check_date = (today - datetime.timedelta(days=i)).isoformat()
            if self.stats["daily"].get(check_date, 0) > 0:
                streak += 1
            else:
                break
        
        return streak

    def add_pomodoro_stat(self):
        """Añade un pomodoro completado a las estadísticas"""
        today = datetime.date.today().isoformat()
        
        if today not in self.stats["daily"]:
            self.stats["daily"][today] = 0
        
        self.stats["daily"][today] += 1
        self.stats["total"] += 1
        self.stats["last_date"] = today
        
        self.save_stats()
        self.update_stats_display()

    def clear_stats(self):
        """Limpia todas las estadísticas"""
        if messagebox.askyesno("Confirmar", "¿Estás seguro de que quieres limpiar todas las estadísticas?"):
            self.stats = {"daily": {}, "total": 0, "last_date": ""}
            self.save_stats()
            self.update_stats_display()

    def play_sound(self, sound_type="default"):
        """Reproduce un sonido de notificación"""
        try:
            if sound_type == "work_end":
                # Sonido para fin de trabajo (más relajante)
                winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
            elif sound_type == "break_end":
                # Sonido para fin de descanso (más energético)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            else:
                winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
        except:
            # Si no puede reproducir sonido, simplemente continúa
            pass

    def start_timer(self):
        """Inicia el temporizador"""
        try:
            trabajo_min = int(self.input_trabajo.get())
            corto_min = int(self.input_corto.get())
            largo_min = int(self.input_largo.get())
            
            if trabajo_min <= 0 or corto_min <= 0 or largo_min <= 0:
                raise ValueError("Los valores deben ser mayores a 0")
                
        except ValueError:
            messagebox.showerror("Error", "Ingresá tiempos válidos en minutos.")
            return

        # Configurar tiempos
        self.work_time = trabajo_min * 60
        self.short_break = corto_min * 60
        self.long_break = largo_min * 60
        
        # Si es la primera vez o después de reset, configurar tiempo actual
        if not self.is_running:
            self.current_time = self.work_time
            self.is_work_time = True
            self.status_label.config(text="¡Trabajando!")

        # Cambiar estado de botones
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.is_running = True
        
        self.update_timer()

    def stop_timer(self):
        """Pausa el temporizador"""
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.is_running = False
        self.status_label.config(text="Pausado")

    def reset_timer(self):
        """Reinicia el temporizador"""
        self.is_running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        
        # Resetear variables
        self.is_work_time = True
        self.pomodoros_completed = 0
        
        try:
            trabajo_min = int(self.input_trabajo.get())
            self.work_time = trabajo_min * 60
            self.current_time = self.work_time
        except:
            self.work_time = 25 * 60
            self.current_time = self.work_time
        
        # Actualizar display
        minutos, segundos = divmod(self.current_time, 60)
        self.timer_label.config(text=f"{minutos:02d}:{segundos:02d}")
        self.status_label.config(text="Listo para trabajar")

    def update_timer(self):
        """Actualiza el temporizador cada segundo"""
        if self.is_running:
            if self.current_time > 0:
                self.current_time -= 1
                
                # Actualizar display
                minutos, segundos = divmod(self.current_time, 60)
                self.timer_label.config(text=f"{minutos:02d}:{segundos:02d}")
                
                # Programar próxima actualización
                self.root.after(1000, self.update_timer)
            else:
                # Tiempo completado
                self.handle_time_complete()

    def handle_time_complete(self):
        """Maneja cuando se completa un período de tiempo"""
        if self.is_work_time:
            # Completó trabajo
            self.play_sound("work_end")
            self.add_pomodoro_stat()
            self.pomodoros_completed += 1
            
            # Determinar tipo de descanso
            if self.pomodoros_completed % 4 == 0:
                self.current_time = self.long_break
                messagebox.showinfo("¡Excelente!", f"¡Completaste {self.pomodoros_completed} pomodoros!\n¡Descanso largo!")
                self.status_label.config(text="Descanso largo")
            else:
                self.current_time = self.short_break
                messagebox.showinfo("¡Bien!", "¡Pomodoro completado!\n¡Descanso corto!")
                self.status_label.config(text="Descanso corto")
                
            self.is_work_time = False
            
        else:
            # Completó descanso
            self.play_sound("break_end")
            self.current_time = self.work_time
            self.is_work_time = True
            messagebox.showinfo("¡A trabajar!", "¡Descanso terminado!\nVolvemos al trabajo.")
            self.status_label.config(text="¡Trabajando!")
        
        # Continuar con el siguiente período
        self.update_timer()

Pomodoro()
  