# school marksheet
from tkinter import *
from tkinter.messagebox import askokcancel

# ----------------------------

def getdata():
	name = st_name_1.get()

	english = english_name_1.get()
	hindi = hindi_name_1.get()
	maths = maths_name_1.get()
	science = science_name_1.get()
	sanskrit = sans_name_1.get()
	 
	total = english+hindi+maths+science+sanskrit
	percent = (total/500)*100
	div = ""
	if percent >= 80:
		div = "1st division"
	elif percent < 80:
		div = "2nd division"
	elif percent < 60:
		div = "3rd division"
	elif percent < 40:
		div = "4rt division"
	else:
		div = "fail"

	message_box(name,total,percent,div)

def message_box(*data):
	print_1 = f"""
	Name : {data[0]}
	Total : {data[1]}
	Percentage : {data[2]}
	Division : {data[3]}"""
		
	askokcancel(title= "Your result",message= print_1)

# ----------------------------
win = Tk()
win.config(bg = "#ffd6ee" )
win.title("------------------------YOUR MARKSHEET-----------------------")
win.geometry("600x620")
win.resizable(False,False)

# ----------------------------
# school name

school_N = Label(win,text="British School", font=("Times new Roman",40,"bold"),bg = "#ffd6ee")
school_N.place(x=100,y=20,height=60,width=400)

# ------------------------------
# student name

st_n = Label(win,text="Student Name", font=("Times New Roman",20,"bold"))
st_n.place(x=30,y=100,height=40,width=200)
st_name_1 = StringVar() 
st_n_entry = Entry(win,font=("Times New Roman",20,"bold"),textvariable=st_name_1)
st_n_entry.place(x=270,y=100,height=40,width=300)

# --------------------------------
# subject name

subject_N = Label(win,text="Subject Number", font=("Times new Roman",30,"bold"),bg = "#ffd6ee")
subject_N.place(x=100,y=160,height=60,width=400)

# ------------------------------
# subject no 
hindi_name_1 = DoubleVar()
english_name_1 = DoubleVar()
maths_name_1 = DoubleVar()
science_name_1 = DoubleVar()
sans_name_1 = DoubleVar()

list_1 = ["English","Hindi","Maths","Science","Sanskrit"]

englishM= Label(win,text="English", font=("Times New Roman",20,"bold"))
englishM.place(x=30,y=240,height=40,width=200)
englishent = Entry(win,font=("Times New Roman",20,"bold"),textvariable=english_name_1)
englishent.place(x=270,y=240,height=40,width=300)

hindiM = Label(win,text="Hindi", font=("Times New Roman",20,"bold"))
hindiM.place(x=30,y=300,height=40,width=200)
hindient = Entry(win,font=("Times New Roman",20,"bold"),textvariable=hindi_name_1)
hindient.place(x=270,y=300,height=40,width=300)

mathsM = Label(win,text="Maths", font=("Times New Roman",20,"bold"))
mathsM.place(x=30,y=360,height=40,width=200)
mathsent = Entry(win,font=("Times New Roman",20,"bold"),textvariable=maths_name_1)
mathsent.place(x=270,y=360,height=40,width=300)

scienceM = Label(win,text="Science", font=("Times New Roman",20,"bold"))
scienceM.place(x=30,y=420,height=40,width=200)
scienceent = Entry(win,font=("Times New Roman",20,"bold"),textvariable=science_name_1)
scienceent.place(x=270,y=420,height=40,width=300)

hindM = Label(win,text="Sanskrit", font=("Times New Roman",20,"bold"))
hindM.place(x=30,y=480,height=40,width=200)
hindent = Entry(win,font=("Times New Roman",20,"bold"),textvariable=sans_name_1)
hindent.place(x=270,y=480,height=40,width=300)

# -------------------------

button = Button(win,text="Submit",font=("Times New Roman",20,"bold"),command= getdata)
button.place(x=200,y=540,height=40,width=200)
win.mainloop()

