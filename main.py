try:
    import customtkinter as C
    from PIL import Image , ImageTk
except:
    import pip
    pip.main(["install" , "customtkinter" , "pillow"])
    import customtkinter as C
    from PIL import Image , ImageTk

app = C.CTk()
app.geometry("700x400")
app.title("Mp3 player")
app.configure(fg_color="#330014")
app.minsize(700 , 400)
app.maxsize(700 , 400)

lframe = C.CTkFrame(app , 160 , 400 ,fg_color="#660033", border_width=2 ,
     border_color= "#b30059" ,corner_radius=15)
lframe.place(x = 1 , y = 1  )

v_btn = C.CTkSlider(lframe , from_=0 , to=100 , width= 133 , height= 15 ,
     button_color="#ff66b3" , progress_color="#cc00ff" , button_hover_color="#e64d00" )
v_btn.place(x = 14 , y = 350)

p_bar = C.CTkProgressBar(app , width= 400 , height= 7 , progress_color= "#e64d00" )
p_bar.place(x= 235 , y = 300)

app.mainloop()