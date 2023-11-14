import tkinter as tk
from tkinter import ttk
import pickle
import customtkinter as ctk

# Initialize an empty list to store hotel data
hotel_data = []  # You may load data from a pickle file later

def check_input(event, combo_box, list):
    value = event.widget.get()
    
    if value == '':
        combo_box['values'] = list
    else:
        data = []
        for item in list:
            if value.lower() in item.lower():
                data.append(item)
        
        combo_box['values'] = data

def on_state_select(event):
    global selected_state
    selected_state = combo_box_state.get()
    update_cities_combobox(selected_state)
    
def update_cities_combobox(selected_state):
    global list_city
    list_city = list(set([hotel['city'] for hotel in hotel_data if hotel['state'] == selected_state]))
    combo_box_city['values'] = list_city

def on_city_select(event):
    global selected_city
    selected_city = combo_box_city.get()
    update_hotel_rating_combobox(selected_city)

def update_hotel_rating_combobox(selected_city):
    global list_hotel_rating
    list_hotel_rating = list(set([hotel['hotel_star_rating'] for hotel in hotel_data if hotel['city'] == selected_city]))
    combo_box_rating['values'] = list_hotel_rating

def on_rating_select(event):
    global selected_rating,selected_city
    selected_rating = combo_box_rating.get()
    update_hotels_combobox(selected_rating,selected_city)
    
def update_hotels_combobox(selected_rating,selected_city):
    global list_hostel_name
    list_hostel_name = [hotel['property_name'] for hotel in hotel_data if hotel['city'] == selected_city and hotel['hotel_star_rating'] == selected_rating]    
    combo_box_hotels['values'] = list_hostel_name
    update_hotel_info()

def update_hotel_info():
    global selected_hotel, selected_state, selected_city, selected_rating

    # Filter the hotel data based on the selected criteria
    selected_hotel_data = [hotel for hotel in hotel_data if
                           hotel['state'] == selected_state and
                           hotel['city'] == selected_city and
                           hotel['hotel_star_rating'] == selected_rating and
                           hotel['property_name'] == selected_hotel]

    if selected_hotel_data:
        highlight_value = selected_hotel_data[0]['highlight_value']
        label_hotel_info.config(text=highlight_value)
    else:
        label_hotel_info.config(text="No information available for the selected criteria.")
window = tk.Tk()
window.title("Hotel Data Analyser")
window.geometry("400x300")
selected_state = ''
selected_city = ''
selected_rating = ''
selected_hotel = ''
list_hotel_name = [] 
list_hotel_address = []
list_hotel_type = []
list_room_type = []
list_hotel_rating = []
list_mmt_review_rating = []
list_city = []
list_state = []
list_country = []
list_highlights = []

# Load hotel data from pickle file
with open('hotel_data.pickle', 'rb') as file:
    hotel_data = pickle.load(file)


# Frame 
main_frame = ctk.CTkFrame(window,fg_color="#141414", bg_color="#eeeee4", width=1600, height=900, corner_radius=30)
main_frame.bind("<Configure>", main_frame.place(relx=0.5, rely=0.5, anchor='center'))

#labels 
label_city = ctk.CTkLabel(main_frame, text="                  Select City                     ", fg_color="#eeeee4", bg_color="#141414", font=("Arial", 24 ), text_color="#141414", corner_radius=3, width=50, height=2)
label_city.bind("<Configure>", label_city.place(relx=0.5, rely=0.5, anchor='center'))
label_city.place(x=350, y=-350)

label_hotel = ctk.CTkLabel(main_frame, text="                  Select Hotel                   ", fg_color="#eeeee4", bg_color="#141414", font=("Arial", 24 ), text_color="#141414", corner_radius=3, width=50, height=2)
label_hotel.bind("<Configure>", label_hotel.place(relx=0.5, rely=0.5, anchor='center'))
label_hotel.place(x=350, y=-200)

label_state = ctk.CTkLabel(main_frame, text="                  Select State                   ", fg_color="#eeeee4", bg_color="#141414", font=("Arial", 24 ), text_color="#141414", corner_radius=3, width=50, height=2)
label_state.bind("<Configure>", label_state.place(relx=0.5, rely=0.5, anchor='center'))
label_state.place(x=-350, y=-350)

label_rating = ctk.CTkLabel(main_frame, text="                 Select Rating                   ", fg_color="#eeeee4", bg_color="#141414", font=("Arial", 24 ), text_color="#141414", corner_radius=3, width=50, height=2)
label_rating.bind("<Configure>", label_rating.place(relx=0.5, rely=0.5, anchor='center'))
label_rating.place(x=-350, y=-200)

label_hotel_info = tk.Label(main_frame, text=None, activeforeground="#eeeee4", activebackground="#141414", font=("Arial", 24 ), width=60, height=12)
label_hotel_info.bind("<Configure>", label_hotel_info.place(relx=0.5, rely=0.5, anchor='center'))
label_hotel_info.place(x=0, y=130)
# Extract unique city names
unique_states = set()
for hotel in hotel_data:
    state = hotel['state']
    if state not in unique_states:
        unique_states.add(state)
        list_state.append(state)

# Create the Co+mbobox for cities
combo_box_state = ttk.Combobox(main_frame, width=31, font=("Arial", 16),height=20)
combo_box_state['values'] = list_state
combo_box_state.bind('<KeyRelease>', lambda event: check_input(event, combo_box_state, list_state))
combo_box_state.bind("<<ComboboxSelected>>", on_state_select)
combo_box_state.bind("<Configure>", combo_box_state.place(relx=0.5, rely=0.5, anchor='center'))
combo_box_state.place(x=-350, y=-320)

combo_box_city = ttk.Combobox(main_frame, width=31, font=("Arial", 16),height=20)
combo_box_city['values'] = list_city
combo_box_city.bind('<KeyRelease>', lambda event: check_input(event, combo_box_city, list_city))
combo_box_city.bind("<<ComboboxSelected>>", on_city_select)
combo_box_city.bind("<Configure>", combo_box_city.place(relx=0.5, rely=0.5, anchor='center'))
combo_box_city.place(x=350, y=-320)

combo_box_rating = ttk.Combobox(main_frame, width=31, font=("Arial", 16),height=20)
combo_box_rating['values'] = list_hotel_rating
combo_box_rating.bind('<KeyRelease>', lambda event: check_input(event, combo_box_rating, list_hotel_rating))
combo_box_rating.bind("<<ComboboxSelected>>", on_rating_select)
combo_box_rating.bind("<Configure>", combo_box_rating.place(relx=0.5, rely=0.5, anchor='center'))
combo_box_rating.place(x=-350, y=-170)

# Create the Combobox for hotels
combo_box_hotels = ttk.Combobox(main_frame, width=31, font=("Arial", 16),height=20)
combo_box_hotels.bind("<Configure>", combo_box_hotels.place(relx=0.5, rely=0.5, anchor='center'))
combo_box_hotels.bind('<KeyRelease>', lambda event: check_input(event, combo_box_hotels, list_hotel_name))
combo_box_hotels.place(x=350, y=-170)

window.mainloop()
