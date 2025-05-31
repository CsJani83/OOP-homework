import tkinter as tk
from autokolcsonzo import Autokolcsonzo

kolcsonzo = Autokolcsonzo("Gyors Autókölcsönző")

def berles():
    berlo = entry_berlo.get()
    auto_rendszam = entry_rendszam.get()
    eredmeny_label.config(text=kolcsonzo.berel_auto(berlo, auto_rendszam))

def listaz():
    berlesek = kolcsonzo.listaz_berlesek()
    eredmeny_label.config(text=str(berlesek))

root = tk.Tk()
root.title("Autókölcsönző")

tk.Label(root, text="Bérlő neve:").pack()
entry_berlo = tk.Entry(root)
entry_berlo.pack()

tk.Label(root, text="Autó rendszáma:").pack()
entry_rendszam = tk.Entry(root)
entry_rendszam.pack()

tk.Button(root, text="Bérel", command=berles).pack()
tk.Button(root, text="Bérlések listázása", command=listaz).pack()

eredmeny_label = tk.Label(root, text="")
eredmeny_label.pack()

root.mainloop()
