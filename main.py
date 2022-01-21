from tkinter.font import BOLD
from tkinter import *
from turtle import width
import KeywordCipher as v

#Function to clear the text fields
def clearTextInput():
  encryption_box.delete("1.0","end")
  decryption_box.delete("1.0","end")
  keyword_box.delete("1.0","end")

#Function to move the text to the decryption text field that is already encrypted
def move_text_to_decryption():
    selection = int(variation_box.get("1.0",END))
    user_input = encryption_box.get("1.0", END).lower()[:-1]
    user_keyword = keyword_box.get("1.0", END).lower()[:-1]
    empty_text = "Failed, Encryption Text Field or Keyword Text Field is empty !\n"
    keyletter = key_letter_box.get("1.0", END).lower()[:-1]
    # check if there is a empty error message 
    if empty_text in user_input in selection:
            encryption_box.delete("1.0", END)
    elif (len(user_input) < 2) or len(user_keyword) < 2:
        # checking if the text box is empty
            decryption_box.insert("1.0", empty_text)
    else:
        # encrypting the data and inserting it to the decryption box
            valid = v.check(user_input)
            if selection == 4 and str(key_letter_box.get(1.0,END)).isspace():
                decryption_box.insert("1.0", empty_text)
                return
            variant = v.switch(selection, user_keyword, keyletter)
            decryption_box.insert("1.0", v.encrypt(valid, variant))
            encryption_box.delete("1.0", END)
    
#Function to move the text to the encryption text field that is already decrypted
def move_text_to_encryption():
    selection = int(variation_box.get("1.0", END))
    user_input = decryption_box.get("1.0", END).lower()[:-1]
    user_keyword = keyword_box.get("1.0", END).lower()[:-1]
    empty_text = "Failed, Encryption Text Field or Keyword Text Field is empty !\n"
    keyletter = key_letter_box.get("1.0", END).lower()[:-1]
        # check if there is a empty error message
    if empty_text in user_input in selection:
            decryption_box.delete("1.0", END)
            
    elif (len(user_input) < 2) or len(user_keyword) < 2:
            # checking if the text box is empty
            encryption_box.insert("1.0", empty_text)
    else:
            # encrypting the data and inserting it to the decryption box
            valid = v.check(user_input)
            if selection == 4 and str(key_letter_box.get(1.0,END)).isspace():
                decryption_box.insert("1.0", empty_text)
                return
            variant = v.switch(selection, user_keyword, keyletter)
            encryption_box.insert("1.0", v.decrypt(valid, variant))
            decryption_box.delete("1.0", END)


root = Tk()
root.title('Keyword Cipher')
root.geometry('1028x560')
root.configure(background= 'light gray')
root.resizable(False, False)

# Title label
title_label = Label(root, text = "Keyword Cipher", font = ("Arial Narrow", 25, BOLD), bg = "light gray")
title_label.grid(row =0 , column =1 )

# Encryption Message
encryption_message = Label(root, text = " ENCRYPT TEXT ", font = ("Arial Narrow", 17), pady = 20, bg = "light gray", justify='center')
encryption_message.grid(row = 1, column = 0, sticky = W)

# Decryption Nessage
decryption_message = Label(root, text = "DECRYPT TEXT ", font = ("Arial Narrow", 17), pady = 20, bg = "light gray")
decryption_message.grid(row = 1, column = 2, sticky = E)

# Encryption Box
encryption_box = Text(root, height = 8, width = 40, font = ("Arial Narrow", 16))
encryption_box.grid(row = 2, column = 0, sticky = W)

# Decrption Box
decryption_box = Text(root, height = 8, width = 40, font = ("Arial Narrow", 16))
decryption_box.grid(row = 2, column = 2, sticky = E)

# Encrypting keyword label
keyword = Label(root, text = "Encrypting Keyword", font  = ("Arial Narrow", 15), bg = "light gray")
keyword.grid(row = 1, column = 1)

# Encrypting Keyword box
keyword_box = Text(root, height = 2, width = 12, font = ("Arial Narrow", 15))
keyword_box.grid(row = 2, column = 1)


clear_button = Button(root, text = "CLEAR", font = ("Arial Narrow", 15) , height= 1, width=12, command=clearTextInput)
clear_button.grid(row = 3, column = 1)

# Encryption button
encryption_button = Button(root, text = "ENCRYPT", font = ("Arial Narrow", 15) , height= 1, width=30, command=move_text_to_decryption)
encryption_button.grid(row = 3, column = 0)

# Decrption button 
decryption_button = Button(root, text = "DECRYPT",font = ("Arial Narrow", 15) , height= 1, width=30, command=move_text_to_encryption)
decryption_button.grid(row = 3, column = 2, pady = 5)

# Variation Chooser label
variation_label = Label(root, text = "Choose Variation :", font = ("Arial Narrow", 13), bg = "light gray")
variation_label.grid(row = 4, column = 0, sticky = W, padx = 10, pady = 25)


#keyletter label
keyletter_label = Label(root, text = "Key Letter :", font = ("Arial Narrow", 11), bg = "light gray")
keyletter_label.grid(row = 4, column = 1, sticky = W)

#key letter box
key_letter_box = Text(root, height = 1, width = 18, font = ("Arial Narrow", 12))
key_letter_box.grid(row = 4, column = 1, sticky = E)

#Note for key letter
note_label = Label(root, text = "This is for keyletter variation ! ", font = ('italic', 10), bg = "light gray", fg = 'red')
note_label.grid(row = 4, column = 2,sticky = W)

#Original Keyword label
original = Label(root, text = "[1] ORIGINAL KEYWORD", font = ("Arial Narrow",11,BOLD),bg = "light gray")
original.grid(row = 5, column = 0, sticky = NW)

#Reverse Keyword label
reverse = Label(root, text = "[2] REVERSE KEYWORD", font = ("Arial Narrow",11,BOLD),bg = "light gray")
reverse.grid(row = 6, column = 0, sticky = NW)

#Atbash Keyword label
atbash = Label(root, text = "[3] KEYWORD-ATBASH", font = ("Arial Narrow",11,BOLD),bg = "light gray")
atbash.grid(row = 7, column = 0,sticky = NW)

#Keyletter Keyword label
keyletter = Label(root, text = "[4] KEYWORD-KEYLETTER", font = ("Arial Narrow",11,BOLD),bg = "light gray")
keyletter.grid(row = 8, column = 0,  sticky = NW)

# Variation Combo box
variation_box = Text(root, height = 1, width = 14, font = ("Arial Narrow", 12))
variation_box.grid(row = 4, column = 0)
variation_box.insert(END, 1)

if __name__ == "__main__":
   root.mainloop()