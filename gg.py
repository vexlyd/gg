from multiprocessing import reduction
import tkinter
from tkinter import *
from tkinter import messagebox

tk = tkinter
main = Tk()  # Name of main window
main.title("House Event Calculator")  # Title
main.geometry("500x350")  # Size of the window in pixels
main.resizable(False, False) #Makes window unable to resize in x and y direction just to keep the user from interfering with the structure in the window

All_events = [] #list in which I will hold my HouseEvent object
names_list = [] #list for holding Event names to be used in drop down   

#----------------------Frames----------------------#
#These frames keep things organized
#frame for entry box
entry_frame = LabelFrame(main, text= "Details Input", font=("Fixedsys"))
entry_frame.grid(row=0, column=0, padx=10, pady=10)
#frame for details box
det_frame = LabelFrame(main)
det_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
#frame for leader board
lead_frame = LabelFrame(main)
lead_frame.grid(row=0, column=1, padx=10, pady=10)

#----------------------Widgets----------------------#
    #-entry_frame labels-#
tk.Label(entry_frame, text="Name of Event").grid(column=0, row=0, sticky=W)
tk.Label(entry_frame, text="Is the event a sport").grid(column=0, row=1, sticky=W)
tk.Label(entry_frame, text="Red House", background="#FA6C38").grid(column=0, row=2, sticky=W)
tk.Label(entry_frame, text="Blue House", background="#62A8F9").grid(column=0, row=3, sticky=W)
tk.Label(entry_frame, text="Yellow House", background="#FFBC1F").grid(column=0, row=4, sticky=W)
tk.Label(entry_frame, text="Green House", background="#01F472").grid(column=0, row=5, sticky=W)
    #-det_frame labels-#
tk.Label(det_frame, text="Event Name").grid(column=0, row=0, sticky=W)
    #-entry_frame inputs
name_entry = tk.Entry(entry_frame)
# Is sport is a StringVar for the radio button so that the StringVar can be accessed to find the current state of the button in the program
is_sport = tk.StringVar()
is_sport.set("Yes")
Radiobutton(entry_frame, text="Yes", variable=is_sport, value="Yes").grid(column=1, row=1,)
Radiobutton(entry_frame, text="No", variable=is_sport, value="No").grid(column=2, row=1,)

red_points = Spinbox(entry_frame, from_=0, to=100, state="readonly", font=("Fixedsys"), readonlybackground="#E9E9ED", foreground="#FA6C38")
blue_points = Spinbox(entry_frame, from_=0, to=100, increment=1, wrap=YES, state="readonly", font=("Fixedsys"), readonlybackground="#E9E9ED", foreground="#0656B1")
yellow_points = Spinbox(entry_frame, from_=0, to=100, increment=1, wrap=YES, state="readonly", font=("Fixedsys"), readonlybackground="#E9E9ED", foreground="#E09D00")
green_points = Spinbox(entry_frame, from_=0, to=100, increment=1, wrap=YES, state="readonly", font=("Fixedsys"), readonlybackground="#E9E9ED", foreground="#1C9C76")

# using geometry manager to arrange input widgets because we cant use .grid() on them directly because they are needed as variables
name_entry.grid(column=1, row=0, columnspan=2)
red_points.grid(column=1, row=2,columnspan=2)
blue_points.grid(column=1, row=3,columnspan=2)
yellow_points.grid(column=1, row=4,columnspan=2)
green_points.grid(column=1, row=5,columnspan=2)

#--Leader board--##
Label(lead_frame, text="Leaderboard").grid(column=0, row=0, columnspan=2, pady=10)
Label(lead_frame, text="Red      ", background="#FA6C38").grid(column=0, row=1, sticky=W, pady=5)
Label(lead_frame, text="Blue     ", background="#62A8F9").grid(column=0, row=2, sticky=W, pady=5)
Label(lead_frame, text="Yellow   ", background="#FFBC1F").grid(column=0, row=3, sticky=W, pady=5)
Label(lead_frame, text="Green    ", background="#01F472").grid(column=0, row=4, sticky=W, pady=5)
#-----------Class using which I will create my house event objects-----------#
class HouseEvent:
    def __init__(self, name, eventtype, red_points, blue_points, yellow_points, green_points, who_won):
        self.name = name
        self.eventtype = eventtype
        self.red_points = red_points
        self.blue_points = blue_points
        self.yellow_points = yellow_points
        self.green_points = green_points
        self.who_won = who_won
        
    def get_info(self):
        return(["Name : " + self.name, "Is a sport : " + self.eventtype, "Red Points : " + str(self.red_points), "Blue Points : " + str(self.blue_points), "Yellow Points : " + str(self.yellow_points), "Green Points : " + str(self.green_points), "Winner : " + self.who_won])

#----------------Drop down to select which events details need to be accessed----------------#
selected_event = tkinter.StringVar()
# Set the default value of the variable
selected_event.set("Select an event")
# Create the option menu widget and passing 
# the options_list and selected_event to it.
event_name_list_dropdown = tkinter.OptionMenu(det_frame, selected_event, All_events)
event_name_list_dropdown.config(font=("Fixedsys", 12) , background="#D2D2DA", activebackground="#E9E9ED")
event_name_list_dropdown.grid(row=0, column=1)

#Updates leader board by iterating the list of event objects and adding all the relevant points together to get a total points then packing latest  scores into leader board
def new_lead_func(total_red_points, total_blue_points, total_yellow_points, total_green_points):
    for obj in All_events:
        total_red_points += obj.red_points
        total_blue_points += obj.blue_points
        total_yellow_points += obj.yellow_points
        total_green_points += obj.green_points
    Label(lead_frame, text=  total_red_points, font=("Fixedsys", 12), background="#FA6C38").grid(column=1, row=1, sticky=W)
    Label(lead_frame, text=  total_blue_points, font=("Fixedsys", 12), background="#62A8F9").grid(column=1, row=2, sticky=W)
    Label(lead_frame, text=  total_yellow_points, font=("Fixedsys", 12), background="#FFBC1F").grid(column=1, row=3, sticky=W)
    Label(lead_frame, text=  total_green_points, font=("Fixedsys", 12), background="#01F472").grid(column=1, row=4, sticky=W)
    print(total_red_points, total_blue_points, total_yellow_points, total_green_points)
 
new_lead_func(0, 0, 0, 0)

#Function that takes the users input and uses the class constructor the make an object and then append it to the list we created above
def save_event_function(): 
    #Using global here because I need the option menu and stringVar to be accessible by other functions like the the show_event_details function which needs to destroy  these elements to prevent stacking.
    global selected_event
    global event_name_list_dropdown
    name = name_entry.get()
    event_type = is_sport.get()
    points_red = int(red_points.get())
    points_blue = int(blue_points.get())
    points_yellow = int(yellow_points.get())
    points_green = int(green_points.get())

    #validating name input
    if name.strip() != "" and name not in names_list and len(name) <= 15:
        #Sorting Scores
        points_list = [("Red", points_red), ("Blue", points_blue),("Yellow", points_yellow), ("Green", points_green)]
        points_list.sort(reverse=YES, key = lambda x: x[1])
        #Validating Points input
        if points_red == 0 and points_blue == 0 and points_yellow == 0 and points_green == 0:
            messagebox.showerror("Points Error", "Please enter points")
        else:
            names_list.append(str(name))  
            #These checks are used in the function to compare adjacent values in the sorted list to see if they are the same for the purpose of finding winners that are tied since we can have upto 4 tied teams we have to check upto 3 times to find all the possible tied winners  
            first_check = None
            second_check = None
            third_check = None
            
            if points_list[0][1] == points_list[1][1]:
                first_check = True
                if points_list[1][1] == points_list[2][1]:
                    second_check = True
                    if points_list[2][1] == points_list[3][1]:
                        third_check = True
                    else:
                        third_check = False
                else:
                    second_check = False   
            else:
                first_check = False
                second_check = False
                third_check = False
            #Setting the winner variable by first finding out if there are multiple winners and then setting the winner as the singular or multiple winners found
            if points_list[0][1] != 0:
                    
                if first_check == True:
                    if second_check == True:
                        if third_check == True:
                            winners = "All teams tied"
                        else:
                            winners = points_list[0][0] +", "+ points_list[1][0] + ", " + points_list[2][0]
                    else:
                        winners = points_list[0][0]+", "+ points_list[1][0]
                else:
                    winners = points_list[0][0]
            else:
                winners = 0

            #Creating the House event object and appending it to a list for it to be stored in memory
            All_events.append(HouseEvent(name, event_type, points_red, points_blue, points_yellow, points_green, winners))

            #Running the function that puts updated scores on the leader board
            new_lead_func(0, 0, 0, 0)

            #Destroying previous option menu so that when we add a new one with the updated list there is no overlap
            event_name_list_dropdown.destroy() 
            #selected_event is a StringVar for event_name_list_dropdown so that whatever option is selected can be pulled by other functions
            selected_event = tkinter.StringVar()
            selected_event.set("Select an event")
            #This option menu has to be put in because the one that is there previously will now be missing an event
            event_name_list_dropdown = tkinter.OptionMenu(det_frame, selected_event, *names_list)
            event_name_list_dropdown.config(font=("Fixedsys", 12), background="#D2D2DA", activebackground="#E9E9ED")
            event_name_list_dropdown.grid(row=0, column=1)
    #Error messages if the data is not valid
    elif name in names_list:
        messagebox.showwarning("Name Error", "An event with this name already exists please chose another name")
    elif name.strip() == "":    
       messagebox.showwarning("Name Error", "You must enter a name for the event")
    elif len(name) > 15:
       messagebox.showwarning("Name Error", "Your name is too long it must be 15 characters only")

#Function for showing event details. It takes the string var from the option menu then uses a class function get_info() to pull information from the desired object and show it in an infobox 
def show_details_function():
    entry = selected_event.get()
    for info in All_events:
        if entry == info.name:
            global event_name_list_dropdown
            event_name_list_dropdown.destroy()
            event_name_list_dropdown = tkinter.OptionMenu(det_frame, selected_event, *names_list)
            event_name_list_dropdown.grid(row=0, column=1)
            event_name_list_dropdown.config(font=("Fixedsys", 12), background="#D2D2DA", activebackground="#E9E9ED")
            tkinter.messagebox.showinfo("Event Details", "\n".join(info.get_info()))

#button for saving event it calls the save_event_function function and creates each event as an object
tk.Button(entry_frame, text="Save Event", command=save_event_function, font=("Fixedsys", 12), background="#C7C7D1", activebackground="#E9E9ED").grid(row=7, column=0,columnspan=3, pady=5)
#Button for showing details it calls the show_details_function which shows a info box with information. Refer to the comments for the show_details_function() for more details on how that works
tk.Button(det_frame, text="Show Details", command=show_details_function, font=("Fixedsys", 12), background="#C7C7D1", activebackground="#E9E9ED").grid(column=0, row=1, columnspan=2)

main.mainloop()