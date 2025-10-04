import tkinter as tk
from UI.main_window import MainWindow
from UI.converter_frame import ConverterFrame
from UI.calc_frame import CalcFrame
import config
import os

class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title(config.App_Name)

        # Fondo general de la ventana
        self.configure(bg=config.BG_COLOR)

        # Desactivar redimensionar y maximizar
        self.resizable(False, False)

        # Establecer icono de la ventana
        icon_path = os.path.join('Assets', 'logo.ico')

        try:
            self.iconbitmap(icon_path)
        except Exception:
            logo = tk.PhotoImage(file=os.path.join('Assets', 'logo.png'))
            self.iconphoto(False, logo)

        # Estilo global para todos los Entry
        self.option_add('*Entry.insertBackground', config.CARET_COLOR)  
        self.option_add('*Entry.insertWidth', 2)               

        # Contenedor donde se cargan las pantallas
        self.container = tk.Frame(self, bg=config.BG_COLOR)
        self.container.grid(row=0, column=0)

        # Diccionario de pantallas
        self.frames = {
            'MainWindow': MainWindow,
            'ConverterFrame': ConverterFrame,
            'CalcFrame': CalcFrame
        }

        # Mostrar pantalla
        self.show_frame('MainWindow')
        self.center_window(offset_y=100)

    def show_frame(self, frame_key):

        # Limpiar el contenedor
        for widget in self.container.winfo_children():
            widget.destroy()

        # Crear y mostrar el nuevo frame
        frame_class = self.frames[frame_key]
        frame = frame_class(self.container, self)
        frame.grid(row=0, column=0)

    def center_window(self, offset_y=100):

        # Calcula el tamaño real de la ventana
        self.update_idletasks()

        # Dimensiones actuales de la ventana
        width = self.winfo_width()
        height = self.winfo_height()

        # Dimensiones de la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calcular coordenadas
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2) - offset_y

        # Evitar que se salga por arriba si offset es muy grande
        if y < 0:
            y = 0

        self.geometry(f"+{x}+{y}")    

if __name__ == '__main__':
    app = App()
    app.mainloop()



