import tkinter as tk
from tkinter import messagebox

class UnitConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Sree's Multi-Unit Converter")
        self.root.geometry("400x350")
        self.root.resizable(False, False)
        
        # Color Palette
        bg_color = "#E0F2F7"  # Pastel Light Sky Blue
        btn_color = "#27ae60" # Green
        
        self.root.configure(bg=bg_color)

        # Conversion Options
        self.options = [
            "Celsius to Fahrenheit",
            "Fahrenheit to Celsius",
            "Km to Miles",
            "Miles to Km",
            "Kg to Pounds",
            "Pounds to Kg"
        ]
        
        # UI Elements
        tk.Label(root, text="Select Conversion:", font=("Arial", 10, "bold"), 
                 bg=bg_color).pack(pady=10)
        
        self.selected_option = tk.StringVar(root)
        self.selected_option.set(self.options[0])
        self.dropdown = tk.OptionMenu(root, self.selected_option, *self.options)
        self.dropdown.config(bg="white", activebackground=bg_color)
        self.dropdown.pack(pady=5)

        tk.Label(root, text="Enter Value:", font=("Arial", 10), 
                 bg=bg_color).pack(pady=5)
        self.entry_input = tk.Entry(root, font=("Arial", 12), width=15)
        self.entry_input.pack(pady=5)

        # Updated Green Button
        self.btn_convert = tk.Button(root, text="Convert", command=self.perform_conversion, 
                                     bg=btn_color, fg="white", font=("Arial", 10, "bold"),
                                     activebackground="#219150", activeforeground="white",
                                     cursor="hand2", padx=20)
        self.btn_convert.pack(pady=20)

        self.label_result = tk.Label(root, text="Result: --", font=("Arial", 12, "bold"), 
                                     fg="#2c3e50", bg=bg_color)
        self.label_result.pack(pady=10)

    def convert_logic(self, val, mode):
        """Mathematical formulas for precision handling."""
        if mode == "Celsius to Fahrenheit":
            return (val * 9/5) + 32
        elif mode == "Fahrenheit to Celsius":
            return (val - 32) * 5/9
        elif mode == "Km to Miles":
            return val * 0.621371
        elif mode == "Miles to Km":
            return val / 0.621371
        elif mode == "Kg to Pounds":
            return val * 2.20462
        elif mode == "Pounds to Kg":
            return val / 2.20462
        return None

    def perform_conversion(self):
        try:
            user_input = self.entry_input.get()
            value = float(user_input)
            
            mode = self.selected_option.get()
            result = self.convert_logic(value, mode)
            
            # Handling float precision
            formatted_result = round(result, 4)
            
            self.label_result.config(text=f"Result: {formatted_result}")
            
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid numeric value.")

if __name__ == "__main__":
    root = tk.Tk()
    app = UnitConverter(root)
    root.mainloop()