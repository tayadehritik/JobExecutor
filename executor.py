from selenium import webdriver
from tkinter import *
#driver = webdriver.Chrome()
#driver.maximize_window()
#driver.get("https://www.google.com/")
#driver.close()
root = Tk()
root.geometry("200x150")

frame = Frame(root)
frame.pack()

url = Entry(frame, width=20)
url.pack(padx=5,pady=5)

root.title("Test")
root.mainloop()