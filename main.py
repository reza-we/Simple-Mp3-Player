try:
    import customtkinter as C
    import tkinter
except:
    import pip
    pip.main(["install" , "customtkinter" , "tkinter"])
    import customtkinter as C
    import tkinter

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


btn1 = C.CTkButton(lframe ,text="Play", width= 1 , height=1 ,corner_radius= 10 , 
    fg_color="#660033" , font= ("", 16) , text_color="#ff3333" , hover="#660033" )
btn1.place(x =110 , y =200)

btn2 = C.CTkButton(lframe ,text="Stop", width= 1 , height=1 ,corner_radius= 10 ,
    fg_color="#660033" , font= ("", 16) , text_color="#ff3333" , hover="#660033")
btn2.place(x =60 , y =155)

btn3 = C.CTkButton(lframe ,text="RePlay", width= 1 , height=1 ,corner_radius= 10, 
    fg_color="#660033" , font= ("", 15) , text_color="#ff3333" , hover="#660033")
btn3.place(x =10 , y =110)
 

app.mainloop()