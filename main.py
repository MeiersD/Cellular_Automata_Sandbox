from tkinter import *
import RulesBook

def change_color(button: Button):
    """Change the color of the button when clicked."""
    current_color = button.cget("bg")
    new_color = "black" if current_color == "white" else "white"
    button.config(bg=new_color)


def create_gui():
    """Create and run the GUI application"""
    master = Tk()
    master.geometry("600x600")
    master.title("Main Window")
    #make grid in main window
    display = Frame(master)
    display.grid(row=0, column=0, columnspan=4, sticky="ew", padx=5, pady=5)
    
    for i in range(14):
        for j in range(33):
            if is_part_of_rules(i, j):
                if i == 1: #in this case, the square will be either white or black but non-interactable
                    square_color = determine_square_color(j)
                    square = Frame(master, bg=square_color)
                    square.grid(row=i, column=j, sticky="nsew")
                if i == 2: #in this case the user can choose if the square will be white or black
                    button = Button(master, text="", bg="white")
                    button.config(command=lambda b=button: change_color(b))
                    button.grid(row=i, column=j, sticky="nsew")
            else:
                label = Label(master, text=f"", bg="grey")
                label.grid(row=i, column=j, sticky="nsew")


    # Make cells expand with window
    for i in range(14):
        master.rowconfigure(i, weight=1)
    for j in range(33):
        master.columnconfigure(j, weight=1)

    master.mainloop()

# Init the rules for the cellular automata
# The rules can be customized when the user clicks on the corresponding button in the grid

def determine_square_color(col: int) -> str:
    """Determine the color of the square based on its position."""
    list_of_black_squares = [5, 10, 13, 14, 19, 21, 23, 25, 26, 29, 30, 31]
    if col in list_of_black_squares:
        return "black"
    return "white"

def is_part_of_rules(row: int, col: int) -> bool:
    if row == 0 or row == 3:
        return False
    if row == 1 and col % 4 != 0:
        return True
    if row == 2 and (col-2) % 4 == 0:
        return True
    return False

def main():
    rules = RulesBook.RulesBook()
    create_gui()  # Start the GUI after other setup

main()




# new_window = Toplevel()  # Create new independent window
# new_window.title("New Window")
# new_window.geometry("250x150")
# Label(new_window, text="This is a new window").pack(pady=20)