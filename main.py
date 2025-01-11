import os
import threading
import time
import asyncio
try:
    from telethon.sync import TelegramClient
    import customtkinter
    import tkinter
except:
    os.system("python -m pip install telethon")
    os.system("python -m pip install customtkinter")
    os.system("python -m pip install tkinter")
    from telethon.sync import TelegramClient
    import customtkinter
    import tkinter
try:
    os.mkdir("Sessions")
except:
    pass
async def send_sms(user,account_name, message):
    client=TelegramClient("secret297",3882903,"040e4e7cf86962d4c670f2d97aab0fd8")
    print(account_name)
    async with client:
        await client.send_message(user, message)

class TelegramAddAccount:
    def __init__(self,nameAccount,id,api_hash,phone_number):
        self.result=True
        self.nameAccount=nameAccount
        try:
            os.mkdir("Sessions/"+nameAccount)
        except:
            self.result = False
        if (self.result == True):
            self.phone_number = phone_number
            try:
                self.client = TelegramClient("Sessions/" + nameAccount + "/" + nameAccount, id, api_hash)
                self.client.connect()
                if not self.client.is_user_authorized():
                    self.client.send_code_request(phone_number)
                else:
                    self.client.disconnect()
                    del self.client
                    os.remove(f"Sessions/{nameAccount}/{nameAccount}.session")
                    os.rmdir(f"Sessions/{nameAccount}")
                    self.result = False
            except:
                self.client.disconnect()
                del self.client
                os.remove(f"Sessions/{nameAccount}/{nameAccount}.session")
                os.rmdir(f"Sessions/{nameAccount}")
                self.result = False
    def __protect__(self):
        return self.result
    def __send_code__(self,code):
        try:
            self.client.sign_in(self.phone_number, code)
            result = True
        except:
            result = False
        return result
class Registrations:
    def __init__(self):
        self.registration_frame = customtkinter.CTk()
        self.registration_frame.title("Add Account")
        self.registration_frame.geometry("240x320")
        self.registration_frame.resizable(False,False)
        self.account_name_label = customtkinter.CTkLabel(master=self.registration_frame, text="Account name : ")
        self.account_name = customtkinter.CTkEntry(master=self.registration_frame, width=120, height=1)
        self.account_ID_label = customtkinter.CTkLabel(master=self.registration_frame, text="Account ID : ")
        self.account_ID = customtkinter.CTkEntry(master=self.registration_frame, width=120, height=1)
        self.account_HASH_label = customtkinter.CTkLabel(master=self.registration_frame, text="Account HASH : ")
        self.account_HASH = customtkinter.CTkEntry(master=self.registration_frame, width=120, height=1)
        self.account_NUM_label = customtkinter.CTkLabel(master=self.registration_frame, text="Account number : ")
        self.account_NUM = customtkinter.CTkEntry(master=self.registration_frame, width=120, height=1)
        self.continue_register = customtkinter.CTkButton(master=self.registration_frame, text="Continue",
                                                         command=self.__protect__)
        self.account_name_label.place(x=70, y=25)
        self.account_ID_label.place(x=70, y=80)
        self.account_HASH_label.place(x=60, y=135)
        self.account_NUM_label.place(x=60, y=200)
        self.account_name.place(x=55, y=55)
        self.account_ID.place(x=55, y=105)
        self.account_HASH.place(x=55, y=170)
        self.account_NUM.place(x=55, y=230)
        self.continue_register.place(x=45, y=270)
        self.registration_frame.mainloop()
    def __protect__(self):
        try:
            self.client = TelegramAddAccount(self.account_name.get(), int(self.account_ID.get()), self.account_HASH.get(), self.account_NUM.get())
            if (self.client.__protect__()):
              
                self.account_name_label.destroy()
                self.account_ID_label.destroy()
                self.account_HASH_label.destroy()
                self.account_NUM_label.destroy()
                self.account_name.destroy()
                self.account_ID.destroy()
                self.account_HASH.destroy()
                self.account_NUM.destroy()
                self.continue_register.destroy()
                self.account_code_label = customtkinter.CTkLabel(master=self.registration_frame, text="Enter code : ")
                self.account_code = customtkinter.CTkEntry(master=self.registration_frame, width=80, height=1)
                self.account_code_btn = customtkinter.CTkButton(master=self.registration_frame, text="SEND CODE",command=self.__send__)
                self.account_code_label.place(x=65,y=40)
                self.account_code.place(x=60,y=80)
                self.account_code_btn.place(x=40,y=120)
                self.registration_frame.geometry("230x180")
            else:
                self.account_code_status = customtkinter.CTkLabel(master=self.registration_frame,
                                                                  text="Error information account!")
                self.account_code_status.place(x=80)
        except:
            self.account_code_status = customtkinter.CTkLabel(master=self.registration_frame,
                                                              text="Error ID account!")
            self.account_code_status.place(x=80)
    def __send__(self):
            try:
                result=self.client.__send_code__(int(self.account_code.get()))
                print(result)
                if(result==True):
                    file=open("account_db.txt","a+")
                    ###
                    ###
                    ###
                    ###
                    self.registration_frame.quit()
                else:
                    self.account_code_status = customtkinter.CTkLabel(master=self.registration_frame, text="Error code!")
                    self.account_code_status.place(x=70, y=10)
            except:
                self.account_code_status= customtkinter.CTkLabel(master=self.registration_frame, text="Error code!")
                self.account_code_status.place(x=70, y=10)
class Templates:
    def __init__(self):
        self.Templates = customtkinter.CTk()
        self.Templates.title("Add Templates")
        self.Templates.geometry("640x480")
        self.Templates.resizable(False, False)
        self.radiobutton_frame = customtkinter.CTkFrame(self.Templates,width=620,height=460)
        self.radiobutton_frame.place(x=10,y=10)
        self.radio_var = tkinter.IntVar(value=0)
        self.label_theme_templates = customtkinter.CTkLabel(master=self.radiobutton_frame,
                                                        text="Theme Templates:",font=("Arial",20))
        self.label_theme_templates.place(x=180, y=20)
        self.theme_templates=customtkinter.CTkEntry(master=self.radiobutton_frame,width=600)
        self.theme_templates.place(x=10,y=60)
        self.label_theme_templates = customtkinter.CTkLabel(master=self.radiobutton_frame,
                                                            text="Text Templates:", font=("Arial", 20))
        self.label_theme_templates.place(x=180, y=100)
        self.text_templates = customtkinter.CTkTextbox(master=self.radiobutton_frame, width=600,height=200)
        self.text_templates.place(x=10, y=150)
        self.templates_btn = customtkinter.CTkButton(master=self.radiobutton_frame,text="Save",command=self.__writer__)
        self.templates_btn.place(x=460, y=400)
              

        self.Templates.mainloop()
    def __writer__(self):
        file=open("templates.txt","a+")
        msg=str()
        for i in self.text_templates.get(0.0,tkinter.END).strip().split("\n"):
            msg+=i+"!:!"
        file.write(self.theme_templates.get()+"#"+msg+"\n")
        self.Templates.destroy()
def __read_size__():
        size = 0
        file = open("templates.txt", "r")
        for line in file.readlines():
            if line != "\n":
                size+=1
        return size

def __read_val__(num):
    file = open("templates.txt", "r")
    result="not found"
    size=0
    for line in file.readlines():
        key, val = line.strip().split("#")
        if num==size:
            result=key
        size+=1
    return result

class Window:
    def __init__(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.app = customtkinter.CTk()
        self.app.geometry("860x460")
        self.app.title("Spammer v2.0 by Secret297")
        self.app.resizable(False,False)
        self.app.grid_rowconfigure(0, weight=1)
        self.app.columnconfigure(2, weight=1)
        self.logo=customtkinter.CTkLabel(self.app,text="Tg Spammer",font=("Ink Free",60))
        self.logo_author=customtkinter.CTkLabel(self.app,text="By Secret297",font=("Ink Free",20))
        self.logo_version=customtkinter.CTkLabel(self.app,text="v 2.0",font=("Arial",20))
        self.logo.place(x=20,y=20)
        self.logo_author.place(x=220,y=80)
        self.logo_version.place(x=790,y=20)
        self.__window_frame__("Spam")
        threading.Thread(target=self.__update__).start()
        self.__left_menu__()
        self.app.mainloop()
    def __about__(self):
        about=customtkinter.CTk()
        about.title("About")
        about.geometry("360x240")
        frame=customtkinter.CTkFrame(master=about,width=330,height=210)
        frame.place(x=15,y=15)
        title_info=customtkinter.CTkLabel(master=frame,text="Program : Tg Spammer",font=("Arial",14))
        title_info.place(x=25,y=25)
        author_info = customtkinter.CTkLabel(master=frame, text="Author : By Secret297",font=("Arial",14))
        author_info.place(x=25, y=65)
        program_info=customtkinter.CTkLabel(master=frame,text="Info : The program for sending messages,\nwith multi-accounting,\ntemplates and proxies",font=("Arial",14))
        program_info.place(x=25,y=105)
        version_info = customtkinter.CTkLabel(master=frame,text="V 2.0",font=("Arial",16))
        version_info.place(x=270, y=170)
        about.mainloop()

    def __left_menu__(self):
        self.array_left_btn=list()
        for i in ["SPAM","TEMPLATES","PROXY"]:
            self.array_left_btn.append(tkinter.Button(master=self.app,width=16,text=i,relief=tkinter.FLAT,bg="#262626",activebackground="#262626",activeforeground="white",fg="white",font=("Arial",16),command=lambda value=i:self.__frame_destroy__(value)))
          

        for i in range(len(self.array_left_btn)):
            self.array_left_btn[i].place(x=20,y=180+(i*45))
        self.array_left_btn.append(tkinter.Button(master=self.app,width=16, text="About", relief=tkinter.FLAT, bg="#262626", activebackground="#262626",activeforeground="white", command=self.__about__,fg="white", font=("Arial", 16)))
        self.array_left_btn[len(self.array_left_btn)-1].place(x=20,y=500)
    def __frame_destroy__(self,text):
        self.frame_global_window.destroy()
        self.__window_frame__(text.title())
    def __update__(self):
        size_account=len(os.listdir("Sessions"))
        size_templates=__read_size__()
        while True:
            if self.choice_menu=="Spam"and size_account!=len(os.listdir("Sessions")):
                size_account=len(os.listdir("Sessions"))
                self.__window_frame__("Spam")
            elif self.choice_menu=="Templates"and size_templates!=__read_size__():
                size_templates = __read_size__()
                self.__window_frame__("Templates")
            else:
                time.sleep(3)
            try:
                self.app.winfo_exists()
            except:
                break

    def send_sms_thread(self,num,account_name,phone, message):
        while(self.protect_sessions[num-1]):
            asyncio.run(send_sms(phone,account_name, message))

    def __send_sms__(self,num,account_name):
        if(self.protect_sessions[num-1]==False):
            self.sessions_btn = customtkinter.CTkButton(master=self.frame_sessions[num - 1],width=2,
                                                        command=lambda folder=account_name, value=num: self.__send_sms__(value, folder),
                                                         text="STOP", fg_color="red")
            self.protect_sessions[num-1]=True


            thread = threading.Thread(target=self.send_sms_thread, args=(num,'@i_am_cago', 'Я тебя жду!'))
            thread.start()
        else:
            self.sessions_btn = customtkinter.CTkButton(master=self.frame_sessions[num - 1],
                                                        command=lambda folder=account_name, value=num: self.__send_sms__(value, folder),
                                                        width=2, text=" RUN  ")
            self.protect_sessions[num-1] = False
        self.sessions_btn.place(x=90, y=66)
    def __window_frame__(self,text):
        self.frame_global_window=customtkinter.CTkScrollableFrame(master=self.app,width=620,height=280,fg_color="#303030")
        self.choice_menu=""
        if(text=="Spam"):
            self.choice_menu="Spam"
            self.btn_register = customtkinter.CTkButton(master=self.app, text="Add Account", command=Registrations)
            self.frame_sessions = list()
            self.protect_sessions=list()
            for folder_sessions in os.listdir("Sessions"):
                self.frame_sessions.append(customtkinter.CTkFrame(master=self.frame_global_window,width=140,height=100))
                self.sessions_label=customtkinter.CTkLabel(master=self.frame_sessions[len(self.frame_sessions)-1],text=folder_sessions)
                self.sessions_checkbox_frame = customtkinter.CTkCheckBox(master=self.frame_sessions[len(self.frame_sessions)-1], text="Proxy")
                self.sessions_btn = customtkinter.CTkButton(master=self.frame_sessions[len(self.frame_sessions)-1],command=lambda folder=folder_sessions,value=len(self.frame_sessions):self.__send_sms__(value,folder),width=2,text="RUN")
                self.sessions_label.place(x=10)
                self.sessions_checkbox_frame.place(x=10,y=68)
                self.sessions_btn.place(x=90,y=66)
                self.protect_sessions.append(False)
              

            ######## cordinates frames #########
            tmp=int()
            line=0
            for x_window in range(int(len(self.frame_sessions)/4)):
                for y_window in range(4):
                    self.frame_sessions[tmp].grid(row=x_window,column=y_window,pady=10,padx=7)
                    tmp+=1
                line+=1
            for x_window in range(1):
                size=len(self.frame_sessions)-tmp
                for y_window in range(size):
                    self.frame_sessions[tmp].grid(row=x_window+line,column=y_window )
                    tmp += 1

        elif (text == "Templates"):
            self.choice_menu="Templates"
            self.btn_register = customtkinter.CTkButton(master=self.app, text="Add Templates", command=Templates)
            self.frame_sessions = list()
            for folder_sessions in range(__read_size__()):
                self.frame_sessions.append(
                    customtkinter.CTkFrame(master=self.frame_global_window, width=140, height=100))
                self.nameTemplates=customtkinter.CTkLabel(master=self.frame_sessions[folder_sessions],height =10,width=10,text=f"{__read_val__(folder_sessions)}")
                self.nameTemplates.place(x=10,y=10)

            ######## cordinates frames #########
            tmp = int()
            line = 0
            for x_window in range(int(len(self.frame_sessions) / 4)):
                for y_window in range(4):
                    self.frame_sessions[tmp].grid(row=x_window, column=y_window, pady=10, padx=7)
                    tmp += 1
                line += 1
            for x_window in range(1):
                size = len(self.frame_sessions) - tmp
                for y_window in range(size):
                    self.frame_sessions[tmp].grid(row=x_window + line, column=y_window)
                    tmp += 1

        elif (text=="Proxy"):
            self.choice_menu="Proxy"
            SPAM_LABEL=customtkinter.CTkLabel(master=self.frame_global_window,text="Function not available",font=("Arial",48))
            SPAM_LABEL.grid(padx=80,pady=110)
            self.btn_register = customtkinter.CTkButton(master=self.app, text="Add Proxy")
        self.btn_register.place(x=700,y=120)
        self.frame_global_window.place(x=200, y=140)



if __name__ == '__main__':
    Window()
