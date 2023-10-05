from tkinter import*
import random
root = Tk()
root.title("Random Password Generator")
root.geometry("400x200")
root.configure(bg = "red1")

entry = Entry(root, font = ("Comic Sans MS", 12, "bold"), text = "Password Guess", bg = "red2", fg = "black")
guess_label = Label(root, font = ("Comic Sans Ms", 14, "bold"), text = "Guessed Password Will Appear Here", bg = "red2", fg = "black")
generated_label = Label(root, font = ("Comic Sans Ms", 14, "bold"), text = " Generated Password Will Appear Here", bg = "red2", fg = "black")

password_resources = [[[1,2,3,4,5,6,7,8,9,0], ["Head", "Tail", "Bob", "Cool", "Coding", "Python", "JavaScript", "Artist", "Basketball", "Joy", "Something"], ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"], ["!", "@", "#", "$", "^", "&", "*", "?", "/", "|"]],[[1,2,3,4,5,6,7,8,9,0], ["Head", "Tail", "Bob", "Cool", "Coding", "Python", "JavaScript", "Artist", "Basketball", "Joy", "Something"], ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"], ["!", "@", "#", "$", "^", "&", "*", "?", "/", "|"]]]

def generate():
    r1 = random.randint(0,9)
    r2 = random.randint(0,10)
    r3 = random.randint(0,25)
    r4 = random.randint(0,9)
    r3_2 = random.randint(0,1)
    
    c1 = str(password_resources[0][0][r1])
    c2 = password_resources[0][1][r2]
    c3 = password_resources[r3_2][2][r3]
    c4 = password_resources[0][3][r4]
    print(c1)
    print(c2)
    print(c3)
    print(c4)    
    generated_label["text"] = "Generated Password: " + c1 + c2 + c3 + c4
    guessed_password = entry.get()
    guess_label["text"] = "Guessed Password: " + guessed_password
    

button = Button(root, text = "Compare To Generated Password", font = ("Comic Sans Ms", 10, "bold"), command = generate, padx = 2, pady = 2, relief = RAISED)





entry.place(relx = 0.5, rely = 0.2, anchor = CENTER)
guess_label.place(relx = 0.5, rely = 0.4, anchor = CENTER)
generated_label.place(relx = 0.5, rely = 0.8, anchor = CENTER)
button.place(relx = 0.5, rely = 0.6, anchor = CENTER)


root.mainloop()