import tkinter.ttk as ttk
import tkinter as tk

class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), array = [[]],heigh =12):
        super().__init__(parent)
        rows = GetR(array)
        table = ttk.Treeview(self, show="headings", selectmode="browse",height=heigh)
        table["columns"]=headings
        table["displaycolumns"]=headings

        for head in headings:
            table.heading(head, text=head, anchor=tk.CENTER)
            table.column(head, anchor=tk.CENTER)

        for row in rows:
            table.insert('', tk.END, values=tuple(row))

        scrolltable = tk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)

        scrolltable2 = tk.Scrollbar(self,orient = tk.HORIZONTAL,  command=table.xview)
        table.configure(xscrollcommand=scrolltable2.set)
        scrolltable2.pack(side=tk.BOTTOM, fill=tk.X)
        table.pack(expand=tk.YES, fill=tk.BOTH)




# def Create_table1(New_win, headline,n_of_point):
#     # New_win = tk.Tk()
#     # New_win.title("Table of variables")
#     Rows = []
#     for i in range(n_of_point):
#         Rows.append([])
#     for k in range(n_of_point):
#         Rows[k].append(k)
#         Rows[k].append(k+1)
#         # Rows[k].append(l1[k])
#         # Rows[k].append(l2[k])
#         # Rows[k].append(l3[k])
#         # Rows[k].append(l4[k])
#         # Rows[k].append(l5[k])
#         # Rows[k].append(l6[k])

#     Rows = tuple(Rows)
#     table = Table(New_win, headings=headline, rows=Rows)
#     table.pack(expand=tk.YES, fill=tk.BOTH)
#     # New_win.mainloop()

def GetR(Arr_2d = [[]]):
    Rows = []
    for i in range(len(Arr_2d)):
        Rows.append([])
        for k in range(len(Arr_2d[0])):
            Rows[i].append(Arr_2d[i][k])
    Rows = tuple(Rows)
    return Rows


