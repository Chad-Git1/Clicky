import customtkinter, pyautogui, time, threading

## Global Variables
running = False  
countdown_seconds = 0  
pyautogui.FAILSAFE = False

## Asynchronous Functions
def calcTime():
    hours = int(entry1.get() or 0)
    minutes = int(entry2.get() or 0)
    seconds = int(entry3.get() or 0)
    totalTime =  3600 * hours + 60 * minutes + seconds
    if totalTime == 0:
        totalTime = 290
    return totalTime

def update_countdown(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    countdown_label.configure(text=f"{hours:02}:{minutes:02}:{seconds:02}")

## Synchronous Functions
def start_clicking():
    global running, countdown_seconds

    if running:
        running = False
        time.sleep(1.00000000001)   
        countdown_seconds = 0
        update_countdown(0)  

    if not running:  
        countdown_seconds = calcTime()
        running = True
        threading.Thread(target=clicker).start()
        
def clicker():
    global running, countdown_seconds

    while running:
        for i in range(countdown_seconds, -1, -1):
            if not running:
                countdown_seconds = 0
                update_countdown(0)
                return
            update_countdown(i)
            time.sleep(1)        

        if running:
            pyautogui.leftClick()

def stop_clicking():
    global running, countdown_seconds
    running = False   
    countdown_seconds = 0
    update_countdown(0)   

## Parameters
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()
root.geometry('400x400')

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand=False)

## Entry
entry1 = customtkinter.CTkEntry(master=frame, placeholder_text='Hours')
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text='Minutes')
entry2.pack(pady=12, padx=10)

entry3 = customtkinter.CTkEntry(master=frame, placeholder_text='Seconds')
entry3.pack(pady=12, padx=10)

## Buttons
start_button = customtkinter.CTkButton(master=frame, text="Start Clicking", command=start_clicking)
start_button.pack(pady=12, padx=10)

stop_button = customtkinter.CTkButton(master=frame, text="Stop Clicking", command=stop_clicking)
stop_button.pack(pady=12, padx=10)

## Display
countdown_label = customtkinter.CTkLabel(master=frame, text="00:00:00")
countdown_label.pack(pady=12, padx=10)

## Main
root.mainloop()