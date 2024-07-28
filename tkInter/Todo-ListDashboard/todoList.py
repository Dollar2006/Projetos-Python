from tkinter import *
import customtkinter as ctk
import os

"""
PASSO A PASSO PARA CRIAR UMA TO-DO LIST GERENCIAVEL

1-Criar interface ctk com um tamanho que caiba varias informações
2-Criar um sistema de login para que cada usuário tenha apenas o acesso as suas informações
3-Ao entrar aparecer uma interface mostrando a lista do item mais velho ao mais novo
4-Colocar botões interativos para que o usuário possa, adicionar mais itens a sua lista, marcar com check as completas,
remover itens da lista, etc
5(opcional)-Adicionar um sistema de personalização
"""


# Inicializando o CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("600x600")
        self.title("To-do List")
        self.resizable(0,0)

        self.login_frame = LoginFrame(master=self, switch_frame=self.switch_frame)
        self.user_data_frame = UserDataFrame(master=self, switch_frame=self.switch_frame)
        self.register_frame = RegisterFrame(master=self,switch_frame=self.switch_frame)

        self.login_frame.pack(expand=True, fill="both")
        self.register_frame.pack(expand=True, fill="both")

    def switch_frame(self, frame):
        """Remove o frame atual e exibe um novo frame."""
        for widget in self.winfo_children():
            widget.pack_forget()
        frame.pack(expand=True, fill="both")


class LoginFrame(ctk.CTkFrame):
    def __init__(self, master, switch_frame):
        super().__init__(master)

        self.switch_frame = switch_frame

        self.LoginFrame = ctk.CTkFrame(self,width=400,height=600)
        self.LoginFrame.pack(pady=150)
       

        self.label = ctk.CTkLabel(self.LoginFrame, text="Login",font=("CTKFont",35))
        self.label.pack(pady=20)

        self.username_entry = ctk.CTkEntry(self.LoginFrame, placeholder_text="Username")
        self.username_entry.pack(pady=(5,15),ipadx=100)

        self.password_entry = ctk.CTkEntry(self.LoginFrame, placeholder_text="Password", show="*")
        self.password_entry.pack(pady=(5,15),ipadx=100)

        self.login_button = ctk.CTkButton(self.LoginFrame, text="Login", command=self.login)
        self.login_button.pack(pady=(10,15))

        self.registerChange_button = ctk.CTkButton(self.LoginFrame, text="Cadastrar novo usuário", command=self.ir_cadastro)
        self.registerChange_button.pack(pady=10)


    def login(self):
        # Aqui você adicionaria a lógica de autenticação
        # Se a autenticação for bem-sucedida, troque para a tela de gerenciamento de dados
        self.switch_frame(self.master.user_data_frame)

    def ir_cadastro(self):
        self.switch_frame(self.master.register_frame)


class RegisterFrame(ctk.CTkFrame):
    def __init__(self, master, switch_frame):
        super().__init__(master)

        self.switch_frame = switch_frame

        self.label = ctk.CTkLabel(self, text="Cadastro",font=("CTKFont",35))
        self.label.pack(pady=10)

        self.username_entry = ctk.CTkEntry(self, placeholder_text="Username")
        self.username_entry.pack(pady=15,ipadx=100)

        self.password_entry = ctk.CTkEntry(self, placeholder_text="Password", show="*")
        self.password_entry.pack(pady=15,ipadx=100)

        self.confirm_password_entry = ctk.CTkEntry(self, placeholder_text="Confirmar senha", show="*")
        self.confirm_password_entry.pack(pady=15,ipadx=100)

        self.register_button = ctk.CTkButton(self, text="Register", command=self.cadastrar)
        self.register_button.pack(pady=10)

        self.back_to_login_button = ctk.CTkButton(self, text="Back to Login", command=self.ir_login)
        self.back_to_login_button.pack(pady=5)

    def cadastrar(self):
        # Aqui você adicionaria a lógica de registro
        # Se o registro for bem-sucedido, troque para a tela de login
        self.switch_frame(self.master.login_frame)

    def ir_login(self):
        # Voltar para a tela de login
        self.switch_frame(self.master.login_frame)


class UserDataFrame(ctk.CTkFrame):
    def __init__(self, master, switch_frame):
        super().__init__(master)

        self.switch_frame = switch_frame

        self.label = ctk.CTkLabel(self, text="Gerenciamento de Dados do Usuário")
        self.label.pack(pady=10)

        self.logout_button = ctk.CTkButton(self, text="Logout", command=self.logout)
        self.logout_button.pack(pady=10)

    def logout(self):
        # Lógica para deslogar o usuário e voltar para a tela de login
        self.switch_frame(self.master.login_frame)


    


if __name__ == "__main__":
    app = App()
    app.mainloop()
