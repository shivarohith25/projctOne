import tkinter as tk

def convert():
    input_text = text_input.get("1.0", tk.END).strip().split("\n")
    python_code = ""
    indent = 0

    for line in input_text:
        line = line.strip()

        if line in ["START", "END"]:
            continue

        elif line.startswith("INPUT"):
            var = line.split()[1]
            python_code += " " * indent + f"{var} = input()\n"

        elif line.startswith("PRINT"):
            text = line[6:]
            python_code += " " * indent + f"print({text})\n"

        elif line.startswith("IF"):
            condition = line[3:]
            python_code += " " * indent + f"if {condition}:\n"
            indent += 4

        elif line == "ELSE":
            indent -= 4
            python_code += " " * indent + "else:\n"
            indent += 4

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, python_code)

# GUI window
root = tk.Tk()
root.title("Flowchart ➝ Python Generator")
root.geometry("600x500")

# Input label
tk.Label(root, text="Enter Flowchart Steps:").pack()

# Input box
text_input = tk.Text(root, height=10)
text_input.pack(fill="both", padx=10, pady=5)

# Default example
text_input.insert(tk.END, """START
INPUT x
IF x > 10
PRINT "Greater"
ELSE
PRINT "Smaller"
END""")

# Convert button
tk.Button(root, text="Convert to Python", command=convert).pack(pady=10)

# Output label
tk.Label(root, text="Generated Python Code:").pack()

# Output box
output_box = tk.Text(root, height=10, bg="black", fg="lime")
output_box.pack(fill="both", padx=10, pady=5)

# Run app
root.mainloop()