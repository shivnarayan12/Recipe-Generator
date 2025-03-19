import tkinter as tk
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

            report.write(f"------------Recipe Generated {dt}-------------\n\n")
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

ingredient_label = tk.Label(root, text="Enter Ingredient:")
ingredient_label.pack(pady=5)
ingredient_entry = tk.Entry(root, width=40)
ingredient_entry.pack(pady=5)
generate_button = tk.Button(root, text="Generate Recipe", command=generate_recipe)
generate_button.pack(pady=10)
result_text = tk.Text(root, height=20, width=80, wrap=tk.WORD)
result_text.pack(padx=10, pady=5)

root.mainloop()
