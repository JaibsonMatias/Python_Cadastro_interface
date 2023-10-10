from tkinter import *

janela = Tk()
class Aplicacao():
    ### função inicializa
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames_Tela()
        self.widegts_frame1()
        janela.mainloop()

    def tela(self):
        ### Criando a Titulo e editando estilo da janela de fundo
        self.janela.title("Cadastro de Clientes")
        self.janela.configure(background= "#696969")
        self.janela.geometry("700x500")
        self.janela.resizable(True, True)
        self.janela.maxsize(width= 900, height= 700)
        self.janela.minsize(width= 500, height= 400)

    def frames_Tela(self):
        ### Criando as frame 1 ( janela de cima )
        self.frame_1 = Frame(self.janela, bd= 4, bg= '#B0C4DE', highlightbackground='#DCDCDC',
                             highlightthickness= 6) ### editando estilo
        self.frame_1.place(relx=0.02, rely=0.02, relwidth= 0.96, relheight= 0.46)

        ### Criando as frame 2 ( janela de baixo )
        self.frame_2 = Frame(self.janela, bd=4, bg='#B0C4DE', highlightbackground='#DCDCDC',
                             highlightthickness= 6) ### editando estilo
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widegts_frame1(self):
        ### Criando botão limpar
        self.bt_limpar = Button(self.frame_1, text="Limpar", bd= 4, bg= '#4682B4', fg="white",
                                font= ("verdana", 8, "bold"))
        self.bt_limpar.place(relx= 0.2, rely= 0.1, relwidth= 0.1, relheight= 0.15) ### posicionando no frame
        ### Criando botão Buscar
        self.bt_buscar = Button(self.frame_1, text="Buscar", bd= 4, bg= '#4682B4', fg="white",
                                font= ("verdana", 8, "bold"))
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criando botão Novo
        self.bt_novo = Button(self.frame_1, text="Novo", bd= 4, bg= '#4682B4', fg="white",
                                font= ("verdana", 8, "bold"))
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criando botão Alterar
        self.bt_alterar = Button(self.frame_1, text="Alterar", bd= 4, bg= '#4682B4', fg="white",
                                font= ("verdana", 8, "bold"))
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criando botão Apagar
        self.bt_apagar = Button(self.frame_1, text="Apagar", bd= 4, bg= '#4682B4', fg="white",
                                font= ("verdana", 8, "bold"))
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        ### Criação da label e entrada do codigo

        self.lb_codigo = Label(self.frame_1, text= "Código", bd= 4, bg= '#B0C4DE', fg="#191970",
                               font= ("verdana", 8, "bold"))
        self.lb_codigo.place(relx= 0.05, rely= 0.015)

        self.codigo_entrada = Entry(self.frame_1)
        self.codigo_entrada.place(relx= 0.05, rely= 0.15, relwidth= 0.10, relheight= 0.09)

        self.lb_nome = Label(self.frame_1, text="Nome", bg= '#B0C4DE', fg="#191970",
                               font= ("verdana", 8, "bold"))
        self.lb_nome.place(relx=0.05, rely=0.30)

        self.codigo_nome = Entry(self.frame_1)
        self.codigo_nome.place(relx=0.05, rely=0.45, relwidth=0.70, relheight=0.12)

        self.lb_telefone = Label(self.frame_1, text="Telefone", bg= '#B0C4DE', fg="#191970",
                               font= ("verdana", 8, "bold"))
        self.lb_telefone.place(relx=0.05, rely=0.62)

        self.codigo_telefone = Entry(self.frame_1)
        self.codigo_telefone.place(relx=0.05, rely=0.75, relwidth=0.15, relheight=0.12)

        self.lb_cidade = Label(self.frame_1, text="Cidade", bg= '#B0C4DE', fg="#191970",
                               font= ("verdana", 8, "bold"))
        self.lb_cidade.place(relx=0.25, rely=0.62)

        self.codigo_cidade = Entry(self.frame_1)
        self.codigo_cidade.place(relx=0.25, rely=0.75, relwidth=0.50, relheight=0.12)




Aplicacao()



