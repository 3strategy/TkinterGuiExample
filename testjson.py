#this example load a json containing hebrew. it fails to
import tkinter as tk
import json

app = tk.Tk()

output = tk.Text(app)

output.pack()

json_val = json.loads('{"a": 5, "b": 7}')

x_file = open('2021semA.json', encoding="utf8")
s = x_file.read().encode('utf-8')
data = json.loads(s)
# print(data)
# output.insert()
# for k in data:
#     output.insert(END, '{} = {}\n'.format(k, data[k]))
# output.config(state=DISABLED)


for k in data:
    output.insert(tk.END, '{} = {}\n'.format(k,data[k]))
output.config(state = tk.DISABLED)
app.mainloop()