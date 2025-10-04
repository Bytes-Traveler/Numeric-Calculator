# Numeric-Calculator

Un **conversor y calculadora numérica** con estética **neón futurista/cyberpunk**, diseñado en **Python + Tkinter**.  
Permite convertir entre diferentes bases numéricas (decimal, binario, hexadecimal, etc.) y realizar cálculos básicos en una interfaz visualmente unificada y ergonómica.

---

## ✨ Características

- 🎨 **Interfaz personalizada** con paleta neón (`#9D00FF`, `#3399FF`, `#FF007A`, `#1B1B2A`).
- 🖥️ **CustomCombobox** propio, estilizado y extensible.
- 🔢 Conversión entre múltiples bases numéricas.
- ➕ Operaciones de cálculo integradas.
- ⚡ Diseño modular: cada pantalla y widget está desacoplado para facilitar mantenimiento y escalabilidad.
- 📦 Configuración centralizada en `config.py` (colores, fuentes, estilos).

---

## 📂 Estructura del proyecto
```
Numeric-Calculator/
│
├── Assets/
│   ├── logo.ico                              
│   │
│   └── logo.png     
│   
├── Logic/
│   ├── converters.py  
│   │
│   └── operations.py              
│  
├── UI/                     
│   ├── calc_frame.py                    
│   │             
│   ├── converter_frame.py
│   │
│   ├── custom_combobox.py
│   │
│   └── main_window.py
│
├── config.py                      
├── main.py                        
└── README.md
```

## 🛠️ Tecnologías

Python 3.10+

Tkinter (UI principal)
