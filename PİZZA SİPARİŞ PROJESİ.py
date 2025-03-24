import tkinter as tk

form = tk.Tk()
form.geometry("600x600+500+200")
form.configure(bg="brown")
form.title("MİLLA PİZZA")
tk.Label(text="MİLLA PİZZA'YA  HOŞGELDİNİZ", fg="black", bg="blue", font="Times 17 italic").place(x=130, y=160)

entr = tk.StringVar()
entr1 = tk.StringVar()
tk.Label(form, text="Ad Soyad    ", bg="yellow", font="times 12 italic").place(x=88, y=230)
tk.Label(form, text="Boyut          ", bg="yellow", font="times 12 italic").place(x=88, y=270)
tk.Label(form, text="İçindekiler  ", bg="yellow", font="times 12 italic").place(x=88, y=310)
tk.Label(form, text="Adres          ", bg="yellow", font="times 12 italic").place(x=88, y=350)

tk.Entry(textvariable=entr).place(x=230, y=230)
tk.Entry(textvariable=entr1).place(x=230, y=350)

Boyut = tk.StringVar()
tk.Radiobutton(form, text="KÜÇÜK BOY ", activebackground="yellow", value=" KÜÇÜK BOY", variable=Boyut).place(
    x=230, y=270)
tk.Radiobutton(form, text="ORTA BOY ", activebackground="yellow", value="ORTA BOY ", variable=Boyut).place(
    x=330, y=270)
tk.Radiobutton(form, text="BÜYÜK BOY ", activebackground="yellow", value=" BÜYÜK BOY", variable=Boyut).place(
    x=430, y=270)

deger1 = tk.StringVar()
deger2 = tk.StringVar()
deger3 = tk.StringVar()

tk.Checkbutton(form, text="ACI SOSLU ", variable=deger1, onvalue="ACILI SOSLU").place(x=230, y=310)
tk.Checkbutton(form, text="KARIŞIK", variable=deger1, onvalue="KARIŞIK").place(x=350, y=310)
tk.Checkbutton(form, text="SUCUKLU", variable=deger1, onvalue="SUCUKLU").place(x=430, y=310)


def siparisver():
    tk.Label(text="Siparişiniz", fg="black", bg="blue", font="Times 17 italic").place(x=50, y=390)
    tk.Label(form, text="Ad-Soyad", bg="yellow", font="times 12 italic").place(x=10, y=430)
    tk.Label(form, text="Boyut", bg="yellow", font="times 12 italic").place(x=10, y=460)
    tk.Label(form, text="İcindekiler", bg="yellow", font="times 12 italic").place(x=10, y=490)
    tk.Label(form, text="Adres", bg="yellow", font="times 12 italic").place(x=10, y=520)

    tk.Label(form, text=entr.get(), bg="yellow", font="times 12 italic").place(x=120, y=430)
    tk.Label(form, text=Boyut.get(), bg="yellow", font="times 12 italic").place(x=120, y=460)
    tk.Label(form, text=deger1.get(), bg="yellow",
             font="times 12 italic").place(x=120, y=490)
    tk.Label(form, text=entr1.get(), bg="yellow", font="times 12 italic").place(x=120, y=520)


def iptal():
    pass


tk.Button(form, text="Sipriş Ver", activebackground="green", command=siparisver).place(x=250, y=380)
tk.Button(form, text="İptal Et", activebackground="red", command=iptal).place(x=320, y=380)

form.mainloop()
