import tkinter as tk
from UI.custom_combobox import CustomCombobox as Combobox
from Logic import converters
import config

class ConverterFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=config.BG_COLOR)

        # Etiqueta de título
        Welcome_Label = tk.Label(self, text='Conversor de Bases', font=config.LABEL_FONT, bg=config.BG_COLOR, fg=config.FG_COLOR)
        Welcome_Label.grid(column=0,row=0,pady=(20,15))

        # Entrada de número
        Number_Label = tk.Label(self, text='Número:', font=config.LABEL_FONT, bg=config.BG_COLOR, fg=config.FG_COLOR)
        Number_Label.grid(column=0,row=1,pady=(5,0))
        self.entry_num = tk.Entry(self, width=20, font=config.ENTRY_FONT, bg=config.ENTRY_BG, fg=config.ENTRY_FG)
        self.entry_num.grid(column=0,row=2,pady=(0,15))

        # Selección de base origen
        Base_Label_origin =tk.Label(self, text='Base de origen:', font=config.LABEL_FONT, bg=config.BG_COLOR, fg=config.FG_COLOR)
        Base_Label_origin.grid(column=0,row=3,pady=(5,0))
        self.base_origen = Combobox(self, values=['2 (Binario)', '8 (Octal)', '10 (Decimal)', '16 (Hexadecimal)'])
        self.base_origen.set(self.base_origen.values[2])  
        self.base_origen.grid(column=0,row=4,pady=(0,15))

        # Selección de base destino
        Base_Label_goal = tk.Label(self, text='Base de destino:', font=config.LABEL_FONT, bg=config.BG_COLOR, fg=config.FG_COLOR)
        Base_Label_goal.grid(column=0,row=5,pady=(5,0))
        self.base_destino = Combobox(self, values=['2 (Binario)', '8 (Octal)', '10 (Decimal)', '16 (Hexadecimal)'])
        self.base_destino.set(self.base_destino.values[0])  
        self.base_destino.grid(column=0,row=6,pady=(0,15))

        # Botón de conversión
        btn_Conv = tk.Button(self, text='Convertir', font=config.BUTTON_FONT, bg=config.BTN_BG, fg=config.BTN_FG, command=self.convertir)
        btn_Conv.grid(column=0,row=7,pady=(15,10))


        # Resultado
        self.resultado_label = tk.Label(self, text='Resultado: ', font=config.LABEL_FONT, bg=config.BG_COLOR, fg=config.FG_COLOR)
        self.resultado_label.grid(column=0,row=8,pady=(5,15))

        # Botón de Volver
        btn_Back = tk.Button(self, text='Volver', font=config.BUTTON_FONT, bg=config.BTN_BG, fg=config.BTN_FG, command=lambda: controller.show_frame('MainWindow'))
        btn_Back.grid(column=0,row=9,pady=(20,10))

    def convertir(self):
        numero = self.entry_num.get()
        base_origen = int(self.base_origen.get().split()[0])
        base_destino = int(self.base_destino.get().split()[0])

        try:
            resultado = converters.convert(numero, base_origen, base_destino)
            self.resultado_label.config(text=f'Resultado: {resultado}')
        except ValueError as e:
            self.resultado_label.config(text=f'Error: {e}')
