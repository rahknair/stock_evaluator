import tkinter as tk
from utils.common_utils import *
def run_the_script(event=None):
    """
    This function is used to exicute the command by extracting the user date
    :return: None
    """
    current_value = extract_current_price(entry4.get())
    print(current_value)  # Display the command (you can replace this with your desired action)

def close_window_by_esc(event=None):
    """
    This function is used to exit the window by pressing the switch escape
    :return: None
    """
    root.destroy()

# Create the main window
root = tk.Tk()
root.geometry("800x600") # The resolution presetting
root.title("Automated monitering of stocks")
root.bind('<Escape>', close_window_by_esc)
root.bind('<Return>', run_the_script)

# All input column lables
lable1 = tk.Label(root, text="The entry value:")
lable2 = tk.Label(root, text="The expected growth:")
lable3 = tk.Label(root, text="The expected lose:")
lable4 = tk.Label(root, text="Enter the stock_symbol:")

# Create input fields
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry3 = tk.Entry(root)
entry4 = tk.Entry(root)


# Create "Start" button
start_button = tk.Button(root, text="Start", command=run_the_script)

# Arrange widgets using grid layout
lable1.grid(row=0, column=0)
entry1.grid(row=0, column=1)

lable2 .grid(row=1, column=0)
entry2.grid(row=1, column=1)

lable3.grid(row=2, column=0)
entry3.grid(row=2, column=1)

lable4.grid(row=2, column=2)
entry4.grid(row=2, column=3)

start_button.grid(row=3, columnspan=2)

# Start the GUI event loop
root.mainloop()
