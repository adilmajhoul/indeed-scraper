import tkinter as tk
from tkinter import ttk
from modules.scraper import Scraper


def on_button_clicked():
    # Get the values from the input fields
    queries_input = entry_queries.get()
    location = entry_location.get()
    sort_by = entry_sort_by.get()
    country = entry_country.get()

    # If the queries field is empty, use the default values
    if not queries_input:
        queries = ["web developer", "backend engineer"]
    else:
        # Split the queries input string into a list of queries
        queries = queries_input.split(",")

    # If any of the other fields are empty, use the default values
    if not location:
        location = "rabat"
    if not sort_by:
        sort_by = "date"
    if not country:
        country = "ma"

    # Create an instance of the Scraper class
    scraper = Scraper(queries, location, sort_by, country)

    # Call the scrape method of the class
    scraper.scrape()

    # Print "Scraping finished!!"
    print("Scraping finished!!")


root = tk.Tk()
root.title("Indeed Scraper")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Queries input field
label_queries = ttk.Label(frame, text="Queries:")
label_queries.grid(row=0, column=0, sticky=tk.W)
entry_queries = ttk.Entry(frame)
entry_queries.grid(row=0, column=1, sticky=tk.E)

# Location input field
label_location = ttk.Label(frame, text="Location:")
label_location.grid(row=1, column=0, sticky=tk.W)
entry_location = ttk.Entry(frame)
entry_location.grid(row=1, column=1, sticky=tk.E)

# Sort by input field
label_sort_by = ttk.Label(frame, text="Sort by:")
label_sort_by.grid(row=2, column=0, sticky=tk.W)
entry_sort_by = ttk.Entry(frame)
entry_sort_by.grid(row=2, column=1, sticky=tk.E)

# Country input field
label_country = ttk.Label(frame, text="Country:")
label_country.grid(row=3, column=0, sticky=tk.W)
entry_country = ttk.Entry(frame)
entry_country.grid(row=3, column=1, sticky=tk.E)

# Button
button = ttk.Button(frame, text="Scrape", command=on_button_clicked)
button.grid(row=4, column=0, columnspan=2, sticky=tk.E)

root.mainloop()
