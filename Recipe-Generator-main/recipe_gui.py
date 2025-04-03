import tkinter as tk
from tkinter import ttk, scrolledtext
from main import recipe_search  # Import the function from main.py
import os
from datetime import datetime

def generate_recipe():
    ingredient = ingredient_entry.get()
    if ingredient:
        opname = ingredient.replace(" ", "_") + '-recipes.txt'
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Same folder
        outFileName = os.path.join(script_dir, opname)

        # Generate recipe using function from main.py
        with open(outFileName, "w", encoding="utf-8") as report:
            now = datetime.now()
            dt = now.strftime("%d/%m/%Y %H:%M:%S")
            hits = recipe_search(ingredient)

            report.write(f"------------ Recipe Generated {dt} -------------\n\n")
            for single_hit in hits:
                recipe_json = single_hit['recipe']
                report.write(f"{recipe_json['label']}\n")
                report.write(f"{recipe_json['ingredientLines']}\n\n")

        display_file_content(outFileName)
    else:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Please enter an ingredient!")

def display_file_content(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        file_content = file.read()

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, file_content)

# GUI setup
root = tk.Tk()
root.title("Recipe Generator")
root.geometry("800x600")  # Increased window size
root.configure(bg="#e6f7ff")  # Light blue background

# Styling
style = ttk.Style()
style.configure("TButton", font=("Arial", 14, "bold"), padding=10, foreground="white", background="#007acc")
style.map("TButton", background=[("active", "#005999")], foreground=[("!disabled", "red")])  # Ensure text is always visible
style.configure("TLabel", font=("Arial", 14), background="#e6f7ff", foreground="#004080")
style.configure("TEntry", font=("Arial", 14), padding=7)

# UI Components
frame = ttk.Frame(root, padding=30, style="TFrame")
frame.pack(expand=True)

ingredient_label = ttk.Label(frame, text="Enter Ingredient:")
ingredient_label.pack(pady=10)

ingredient_entry = ttk.Entry(frame, width=50)
ingredient_entry.pack(pady=10)

generate_button = ttk.Button(frame, text="Recipe Generator", command=generate_recipe, style="TButton")
generate_button.pack(pady=15)

# Scrollable Text Box
result_text = scrolledtext.ScrolledText(frame, height=18, width=80, wrap=tk.WORD, font=("Arial", 12))
result_text.pack(padx=10, pady=10)

root.mainloop()
