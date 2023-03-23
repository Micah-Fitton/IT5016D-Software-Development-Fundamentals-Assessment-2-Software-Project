from tkinter import * 
root = Tk()
root.title("Ticketing software")
root.geometry("500x250")
root.configure(bg="#fabebe")

staff_id1 = ""
name1 =""
email1 =""
issue1 =""

with open("stats.txt","r") as f:
    x = f.readlines()[0]
    y = x.strip("Tickets Submitted: ")
    z = int(y)+1

with open("stats.txt","r") as f1:
    a = f1.readlines()[1]
    b = a.strip("Tickets Resolved: ")
    c = int(b)

with open("stats.txt","r") as f2:
    s = f2.readlines()[2]
    t = s.strip("Tickets to Solve: ")
    u = int(t)+1
    
def submit():
    ticket_status = "Open"
    response = "Not Yet Provided"
    class Ticket():
        staff_id:"None";
        name:"None";        
        email:"None";
        issue:"None";

    ticket1 = Ticket()

    ticket1.staff_id = label1.get()
    ticket1.name = label3.get()
    ticket1.email = label5.get()
    ticket1.issue =  label7.get()

    if label7.get() == "Password Change":
        newpassword = str(ticket1.staff_id[0:2])+str(ticket1.name[0:3])
        ticket_status = "Closed"
        c+1
        print(newpassword)
    
    
    title = "ticket{}".format(z)
    with open(title+'.txt','w') as file:
        file.write("Staff ID: "+str(ticket1.staff_id)+
                   "\nName: "+str(ticket1.name)+
                   "\nEmail: "+str(ticket1.email)+
                   "\nIssue: "+str(ticket1.issue)+
                   "\nTicket Status: "+str(ticket_status)+
                   "\nResponse: "+str(response))    

    with open("stats.txt","w") as file1:
        file1.write("Tickets Submitted: "+str(z)+
                   "\nTickets Resolved: "+str(c)+
                   "\nTickets to Solve: "+str(u))

def response():
    root1 = Toplevel(root)
    root1.title("Responses")
    root1.geometry("400x200")

    def submit1():
        ticketnumber = label11.get()
        with open("ticket"+str(ticketnumber)+".txt","r") as f3:
            i = f3.readlines()[0]
        with open("ticket"+str(ticketnumber)+".txt","r") as f3:
            j = f3.readlines()[1]
        with open("ticket"+str(ticketnumber)+".txt","r") as f3:
            k = f3.readlines()[2]
        with open("ticket"+str(ticketnumber)+".txt","r") as f3:
            l = f3.readlines()[3]
        with open("ticket"+str(ticketnumber)+".txt","r") as f3:
            m = f3.readlines()[4]
        with open("ticket"+str(ticketnumber)+".txt","r") as f3:
            n = f3.readlines()[5]
            label13 = Label(root1,text=i)
            label14 = Label(root1,text=j)
            label15 = Label(root1,text=k)
            label16 = Label(root1,text=l)
            label17 = Label(root1,text=m)
            label18 = Label(root1,text=n)
            label13.place(x = 0, y=65)
            label14.place(x = 0, y=85)
            label15.place(x = 0, y=105)
            label16.place(x = 0, y=125)
            label17.place(x = 0, y=145)
            label18.place(x = 0, y=165)

    label10 = Label(root1,text="Enter Ticket Number").place(x = 0, y = 0)
    label11 = Entry(root1, width = 20)
    label11.place(x = 0, y = 20)
    
    label12 = Button(root1,width = 20, command = submit1)
    label12.place(x = 0, y = 40)

label = Label(root,text="Staff ID :").place(x = 0, y = 0)
label1  = Entry(root,width=20, )
label1.place(x = 47, y = 1)
label2 = Label(root,text="Name   :").place(x = 0, y = 20)
label3 = Entry(root,width=20)
label3.place(x = 47, y = 21)
label4 = Label(root,text="Email    :").place(x = 0, y = 40)
label5  = Entry(root,width=20, )
label5.place(x = 47, y = 41)
label6 = Label(root,text="Issue     :").place(x = 0, y = 60)
label7  = Entry(root,width=50, )
label7.place(x = 47, y = 61)
label8 = Button(root,text="Submit ticket",command= submit).place(x = 0, y = 81)
label9 = Button(root,text="Resolve Tickets", command=response).place(x = 80, y = 81)

root.mainloop()