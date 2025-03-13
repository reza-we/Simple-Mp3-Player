try:
    import customtkinter as C
except:
    import pip
    pip.main(["install" , "customtkinter"])

app = C.CTk()
app.geometry("700x400")
app.title("Mp3 player")
app.mainloop()