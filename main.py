import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class SetarNote:
    # inicializar a janela
    __root = Tk()
    # configurando o bloco de notas
    __width = 300
    __height = 300
    __textArea = Text(__root, pady=10, padx=10, wrap="word", font=('Consoles 12'))
    __menuBar = Menu(__root)
    __fileMenu = Menu(__menuBar, tearoff=0)
    __editMenu = Menu(__menuBar, tearoff=0)
    __viewMenu = Menu(__menuBar, tearoff=0)
    __helpMenu = Menu(__menuBar, tearoff=0)

    __ScrollBar = Scrollbar(__textArea)
    __file = None

    def __init__(self, **kwargs):
        # icone
        try:
            self.__root.wm_iconbitmap('icone.ico')
        except:
            pass

        # tamanho da tela
        try:
            self.__width = kwargs['width']
        except KeyError:
            pass

        try:
            self.__height = kwargs['height']
        except KeyError:
            pass

        self.__root.title('Sem Título - Nota')

        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        left = (screenWidth / 2) - (self.__width / 2)
        top = (screenHeight / 2) - (self.__height / 2)

        self.__root.geometry("%dx%d+%d+%d" % (self.__width, self.__height, left, top))

        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)

        self.__textArea.grid(sticky=N + E + S + W)

        # File Menu
        self.__fileMenu.add_command(label='Novo', command=self.__newFile)
        self.__fileMenu.add_command(label='Abrir', command=self.__openFile)
        self.__fileMenu.add_command(label='Salvar', command=self.__saveFile)
        self.__fileMenu.add_separator()
        self.__fileMenu.add_command(label='Sair', command=self.__exitApplication)
        self.__menuBar.add_cascade(label='Ficheiro', menu=self.__fileMenu)

        # Edit Menu
        self.__editMenu.add_command(label='Recortar', command=self.__cut)
        self.__editMenu.add_command(label='Copiar', command=self.__copy)
        self.__editMenu.add_command(label='Colar', command=self.__paste)
        self.__menuBar.add_cascade(label='Editar', menu=self.__editMenu)

        # Help Menu
        self.__helpMenu.add_command(label='Sobre Aplicação', command=self.__showAbout)
        self.__menuBar.add_cascade(label='Ajuda', menu=self.__helpMenu)

        # Mostrar menu e scrollBar na tela
        self.__root.config(menu=self.__menuBar)

        self.__ScrollBar.pack(side=RIGHT, fill=Y)
        self.__ScrollBar.config(command=self.__textArea.yview)
        self.__textArea.config(yscrollcommand=self.__ScrollBar.set)

    def __newFile(self):
        self.__root.title('Sem titulo - SetNote')
        self.__file = None
        self.__textArea.delete(1.0, END)

    def __openFile(self):
        self.__file = askopenfilename(defaultextension='.txt',
                                      filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])

        if self.__file == '':
            self.__file = None
        else:
            self.__root.title(os.path.basename(self.__file) + ' - SetarNote')
            self.__textArea.delete(1.0, END)

            file = open(self.__file, 'r')
            self.__textArea.insert(1.0, file.read())
            file.close()

    def __saveFile(self):
        if self.__file is None:
            self.__file = asksaveasfilename(initialfile='Sem titulo', defaultextension='.txt',
                                            filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])

            if self.__file == '':
                self.__file = None
            else:
                file = open(self.__file, 'w')
                file.write(self.__textArea.get(1.0, END))
                file.close()

                self.__root.title(os.path.basename(self.__file) + ' - SetarNote')

        else:
            file = open(self.__file, 'w')
            file.write(self.__textArea.get(1.0, END))
            file.close()

    def __exitApplication(self):
        self.__root.destroy()

    # Funções do menu editar
    def __cut(self):
        self.__textArea.event_generate('<<Cut>>')

    def __copy(self):
        self.__textArea.event_generate('<<Copy>>')

    def __paste(self):
        self.__textArea.event_generate('<<Paste>>')

    # Funções do Help Menu
    def __showAbout(self):
        showinfo('Informação do Software - Bloco de Notas',
                 'Versão: 1.0.0\nLicença: Grátis\nDesenvolvedor: Ana')

    def run(self):
        self.__root.mainloop()


note = SetarNote()
note.run()
