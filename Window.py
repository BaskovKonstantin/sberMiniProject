import sqlite3
import tkinter as tk
from tkinter import ttk
import xlsxwriter

def export_to_xlsx():
    workbook = xlsxwriter.Workbook('example.xlsx')
    worksheet = workbook.add_worksheet()
    row = 0
    col = 0

    for item in tree.get_children(''):

        for i in range(len(tree.item(item)['values'])):
            worksheet.write(row, col, tree.item(item)['values'][i])
            worksheet.write(row, col + 1, tree.item(item)['values'][i])
            worksheet.write(row, col + 2, tree.item(item)['values'][i])
            row += 1
    workbook.close()



def filter_bad():
    for item in tree.get_children(''):
        if (float(tree.item(item)['values'][5]) > 2 and float(tree.item(item)['values'][11]) > 2 ):
            tree.delete(item)


def clear_treeview():
    for i in tree.get_children():
        tree.delete(i)

def view_records():
    clear_treeview()
    conn = sqlite3.connect("entertainment.db")
    c = conn.cursor()
    c.execute("SELECT * FROM movies JOIN albums ON albums.id = movies.id")
    rows = c.fetchall()
    for row in rows:
        tree.insert("", tk.END, values=row)
    conn.close()

def sort(col_name):
    clear_treeview()
    name = col_name.split()
    conn = sqlite3.connect("entertainment.db")
    c = conn.cursor()
    c.execute(f"SELECT * FROM movies JOIN albums  ON albums.id = movies.id ORDER BY {name[0]}.{name[1]} DESC")
    rows = c.fetchall()
    # print(rows)

    for row in rows:
        tree.insert("", tk.END, values=row)



    conn.close()

root = tk.Tk()
root.title("Books Information")

tree = ttk.Treeview(root, columns=("ID", "movies Title", "movies Artist", "movies Release Date", "movies Duration", "movies Rating", 'ID music', "albums Title", "albums Director", "albums Release Date", "albums Tracks", "albums Rating"), show="headings")
tree.pack()

tree.heading("ID", text="ID")
tree.column("ID", width=50, anchor="center")

tree.heading("movies Title", text="movies Title", command=lambda: sort("movies title"))
tree.column("movies Title", width=200, anchor="center")

tree.heading("movies Artist", text="movies Artist", command=lambda: sort("movies director"))
tree.column("movies Artist", width=200, anchor="center")

tree.heading("movies Release Date", text="movies Release Date", command=lambda: sort("movies release_date") )
tree.column("movies Release Date", width=200, anchor="center")

tree.heading("movies Duration", text="movies Duration", command=lambda: sort("movies duration"))
tree.column("movies Duration", width=50, anchor="center")

tree.heading("movies Rating", text="movies Rating", command=lambda: sort("movies rating"))
tree.column("movies Rating", width=50, anchor="center")

tree.heading("ID music", text="ID music")
tree.column("ID music", width=50, anchor="center")

tree.heading("albums Title", text="albums Title", command=lambda: sort("albums title"))
tree.column("albums Title", width=200, anchor="center")

tree.heading("albums Director", text="albums Director", command=lambda: sort("albums artist"))
tree.column("albums Director", width=200, anchor="center")

tree.heading("albums Release Date", text="albums Release Date", command=lambda: sort("albums release_date"))
tree.column("albums Release Date", width=200, anchor="center")

tree.heading("albums Tracks", text="albums Tracks", command=lambda: sort("albums tracks"))
tree.column("albums Tracks", width=50, anchor="center")

tree.heading("albums Rating", text="albums Rating", command=lambda: sort("albums rating"))
tree.column("albums Rating", width=50, anchor="center")

view_records_button = tk.Button(root, text="View Records", command=view_records)
view_records_button.pack()

filter_bad_button = tk.Button(root, text="Filter bad button", command=filter_bad)
filter_bad_button.pack()
export_to_xlsx_button = tk.Button(root, text="Export to xlsx", command=export_to_xlsx)
export_to_xlsx_button.pack()

root.mainloop()