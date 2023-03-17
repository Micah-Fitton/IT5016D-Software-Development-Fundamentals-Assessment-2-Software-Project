from tkinter import * 
root = Tk()
root.title("Ticketing software")
root.geometry("500x250")
root.configure(bg="#fabebe")

staff_id1 = ""
name1 =""
email1 =""
issue1 =""
def submit():
    
    name1 = label3.get()
    email1 = label5.get()
    issue1 = label7.get()
    class Ticket():
        staff_id:"None";
        name:"None";        
        email:"None";
        issue:"None";
        def display(self):
            print("staffid:", self.staff_id);
            print("name:", self.name);
            print("email:",self.email);
            print("issue:", self.issue);

    ticket1 = Ticket()

    ticket1.staff_id = label1.get()
    ticket1.name = name1
    ticket1.email = email1
    ticket1.issue = issue1
    ticket1.display()

    
    

label = Label(text="Staff ID :").place(x = 0, y = 0)
label1  = Entry(width=20, )
label1.place(x = 47, y = 1)
label2 = Label(text="Name   :").place(x = 0, y = 20)
label3 = Entry(width=20)
label3.place(x = 47, y = 21)
label4 = Label(text="Email    :").place(x = 0, y = 40)
label5  = Entry(width=20, )
label5.place(x = 47, y = 41)
label6 = Label(text="Issue     :").place(x = 0, y = 60)
label7  = Entry(width=50, )
label7.place(x = 47, y = 61)
label8 = Button(text="Submit ticket",command= submit).place(x = 0, y = 81)



root.mainloop()