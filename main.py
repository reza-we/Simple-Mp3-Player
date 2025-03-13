try:
    import customtkinter as C
except:
    import pip
    pip.main(["install" , "customtkinter"])

app = C.CTk()
app.geometry("700x400")
app.title("Mp3 player")
app.configure(fg_color="#33001a")

lframe = C.CTkFrame(app , 160 , 400 ,fg_color="#660033", border_width=2 ,
     border_color= "#b30059" ,corner_radius=15)
lframe.place(x = 1 , y = 1  )

app.mainloop()