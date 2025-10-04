import tkinter as tk
from UI.custom_combobox import CustomCombobox as Combobox
from Logic import operations
import config

class CalcFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=config.BG_COLOR)

        # Etiqueta de título
        Welcome_Label = tk.Label(self, text='Operaciones', font=config.LABEL_FONT, bg=config.BG_COLOR, fg=config.FG_COLOR)
        Welcome_Label.grid(column=0,row=0,pady=(20,15))

        # --- Entrada de números ---
        n1_label = tk.Label(self, text='Número 1:', font=config.LABEL_FONT, bg=config.BG_COLOR, fg=config.FG_COLOR)
        n1_label.grid(column=0,row=1,pady=(5,0))
        self.entry_num1 = tk.Entry(self, width=20, font=config.ENTRY_FONT, bg=config.ENTRY_BG, fg=config.ENTRY_FG)
        self.entry_num1.grid(column=0,row=2,pady=(0,15))

        n2_label = tk.Label(self, text='Número 2:', font=config.LABEL_FONT, bg=config.BG_COLOR, fg=config.FG_COLOR)
        n2_label.grid(column=0,row=3,pady=(5,0))
        self.entry_num2 = tk.Entry(self, width=20, font=config.ENTRY_FONT, bg=config.ENTRY_BG, fg=config.ENTRY_FG)
        self.entry_num2.grid(column=0,row=4,pady=(0,15))

        # --- Selección de base ---
        Base_Label = tk.Label(self, text='Base:', font=config.LABEL_FONT, bg=config.BG_COLOR, fg=config.FG_COLOR)
        Base_Label.grid(column=0,row=5,pady=(5,0))
        self.base = Combobox(self, values=['binario', 'octal', 'decimal', 'hexadecimal'])
        self.base.set(self.base.values[2])
        self.base.grid(column=0,row=6,pady=(0,15))

        # --- Selección de operación ---
        Op_Label = tk.Label(self, text='Operación:', font=config.LABEL_FONT, bg=config.BG_COLOR, fg=config.FG_COLOR)
        Op_Label.grid(column=0,row=7,pady=(5,0))
        self.operacion = Combobox(self, values=['suma', 'resta', 'multiplicación', 'división'])
        self.operacion.set(self.operacion.values[0])
        self.operacion.grid(column=0,row=8,pady=(0,20))

        # --- Botón calcular ---
        Calc_Btn = tk.Button(self, text='Calcular', font=config.BUTTON_FONT, bg=config.BTN_BG, fg=config.BTN_FG, command=self.calcular)
        Calc_Btn.grid(column=0,row=9,pady=(10,15))

        # --- Resultado ---
        self.resultado_label = tk.Label(self, text='Resultado: ', font=config.LABEL_FONT, bg=config.BG_COLOR, fg=config.FG_COLOR)
        self.resultado_label.grid(column=0,row=10,pady=(5,15))

        # Botón de Volver
        Back_Btn = tk.Button(self, text='Volver', font=config.BUTTON_FONT, bg=config.BTN_BG, fg=config.BTN_FG, command=lambda: controller.show_frame('MainWindow'))
        Back_Btn.grid(column=0,row=11,pady=(20,10))

    def calcular(self):
        num1 = self.entry_num1.get()
        num2 = self.entry_num2.get()
        base = self.base.get()
        op = self.operacion.get()

        try:
            resultado = operations.calculate(num1, num2, base, op)
            self.resultado_label.config(text=f'Resultado: {resultado}')
        except ValueError as e:
            self.resultado_label.config(text=f'Error: {e}')
