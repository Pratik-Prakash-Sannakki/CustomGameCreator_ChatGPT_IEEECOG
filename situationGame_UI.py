import tkinter as tk
import situationGame

# initialize Tkinter window
window = tk.Tk()
window.geometry("300x150")
window.title("Interactive Game")

# define functions for buttons
def update_output():
    # get user input and update output label
    input_text = input_entry.get()
    output_label.config(text=f"You entered: {input_text}")
    Situation_label.config(text=situationGame.outcomes[input_text]["text"])
    action_label.config(text="")
    location_label.config(text="")
    if "location" in situationGame.outcomes[input_text]:
        location_label.config(text=situationGame.outcomes[input_text]["location"])
    else:
        location_label.config(text="")
        
        
    if "actions" in situationGame.outcomes[input_text]:
        if len(situationGame.outcomes[input_text]["actions"])==2:
            action_label.config(text=situationGame.outcomes[input_text]["actions"][0]+"  or  "+situationGame.outcomes[input_text]["actions"][1])
        elif len(situationGame.outcomes[input_text]["actions"])==1:
            action_label.config(text=situationGame.outcomes[input_text]["actions"][0])
    else:
        action_label.config(text="")

    

    
# destroy game and Quit game
def quit_game():
    window.destroy()

# create widgets
Situation_label=tk.Label(window, text="")
location_label = tk.Label(window, text=situationGame.location)
action_label = tk.Label(window, text=situationGame.actions[0]+"  or  "+situationGame.actions[1])
input_entry = tk.Entry(window)
submit_button = tk.Button(window, text="Submit", command=update_output)
output_label = tk.Label(window, text="")
quit_button = tk.Button(window, text="Quit", command=quit_game)

# add widgets to window
Situation_label.pack()
location_label.pack()
action_label.pack()
input_entry.pack()
submit_button.pack()
output_label.pack()
quit_button.pack()

# start the main event loop
window.mainloop()
