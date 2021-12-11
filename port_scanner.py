
from tkinter import*
import socket


window = Tk()
window.geometry("330x500")
window.title("PORT SCANNER")
window.resizable(FALSE, FALSE)


def scanning():
    s1 = str(enturl.get())
    liste =[21,22,23,25,80,139,443,445,3389]
    try:
        for port in liste:
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            result = sock.connect_ex((s1,port))
            if result == 0:
                listresult.insert(1, "Port{} Open".format(port))
            else: 
                listresult.insert(1, "Port{} Close".format(port))
            sock.close()
    except socket.error:
            print("the computer is not reachable.")
        


lblurl = Label(window, text="URL or IP adress", font="Verdana 12 bold", fg="white", bg = "black")
lblurl.place(x=60, y =20)
listresult = Listbox(window, font = "Verdana 12 bold", width= "25", height="17", fg = "white", bg = "black")
listresult.place(x = 27, y =140)

enturl = Entry(window, font="Verdana 12 bold", fg="blue")
enturl.place(x=50, y = 50)
btnscann = Button(window,text="Port Scannning", font= "Verdana 12 bold", fg="white",bg="black", command=scanning)
btnscann.place(x=80,y=90)



window.mainloop()