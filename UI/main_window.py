import tkinter as tk
import config

class MainWindow(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent,bg=config.BG_COLOR)

        Welcome_Label = tk.Label(self, text='Elige una opción:', font=config.TITLE_FONT,bg=config.BG_COLOR,fg=config.FG_COLOR)
        Welcome_Label.grid(column=0,row=0,pady=(20, 10))

        btn_Conv = tk.Button(self, text='Conversor de Números', font=config.BUTTON_FONT,fg=config.BTN_FG,bg=config.BTN_BG, command=lambda: controller.show_frame("ConverterFrame"))
        btn_Conv.grid(column=0,row=1,pady=10)

        btn_Calc = tk.Button(self, text='Operaciones en Base', font=config.BUTTON_FONT,fg=config.BTN_FG,bg=config.BTN_BG, command=lambda: controller.show_frame("CalcFrame"))
        btn_Calc.grid(column=0,row=2,pady=10)
