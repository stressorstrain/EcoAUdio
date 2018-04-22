import simpleaudio as sad
import tkinter as tk


class Audior:
    def __init__(self):
        self.path = "/home/guibax/Programs/AUdior/"
        self.nv_prod = 'Produtores'
        self.nv_cons_1 = 'Consumidores Primários'
        self.nv_cons_2 = 'Consumidores Secundários'
        self.nv_cons_3 = 'Consumidores Terciários'
        self.nv_decomp = 'Decompositores'
        self.greter = "Greeter"
        self.inst = "Produtores"
        self.lista_indx = [[self.path+self.nv_prod+'.wav', 0], [self.path+self.nv_cons_1+'.wav', 1],
                           [self.path+self.nv_cons_2+'.wav', 2], [self.path+self.nv_cons_3+'.wav', 3],
                           [self.path+self.nv_decomp+'.wav', 4]]

        self.nvs_troficos = ["Produtores", "Consumidores Primários", "Consumidores Segundários", "Decompositores"]
        self.nv_produtor = ["Buriti", "Pequi"]
        self.nv_cons_1_ = ["Borboleta", "Rato-Silvestre", "Formiga-Saúva"]
        self.nv_cons_2_ = ["Sapo", "Carcará", "Tamanduá"]
        self.nv_cons_3_ = ["Urutu", "Carcará", "Onça Parda"]
        self.nvc_decomp = ["Decompositores"]
        self.faixa = 'Faixa Atual:'
        self.index = 0
        self.ind_str = str(self.index)
        self.current = self.currents()
        self.cont = 0
        self.wave_obj = self.grab_aud()
        self.gui()


    def greeter(self):
        wave_obj = sad.WaveObject.from_wave_file(self.path+self.greter+'.wav')
        #  self.play(wave_obj)

    def instructions(self, event):
        wave_obj = sad.WaveObject.from_wave_file(self.path+self.inst+'.wav')
        #self.play(wave_obj)

    def bind_foward(self, event):

        self.bind_pls()

    def bind_backward(self, event):
        self.bind_lss()

    def alt_lb1(self):
        texs = str(self.currents())
        print(texs)

        self.lb1.config(text=self.faixa+'\n'+texs)
        self.root.after(20, self.bind_play)

    def bind_play(self):
        self.wave_obj = self.grab_aud()

        self.play(self.wave_obj)

    def bind_play_b(self, event):
        self.bind_play()

    def bind_pls(self):
        if self.index == 4:
            self.alt_lb1()
        else:
            if self.index < 4:
                self.index += 1
                self.alt_lb1()

    def bind_lss(self):
        if self.index == 0:
            self.alt_lb1()
        else:
            if self.index >= 0:
                self.index += -1
                self.alt_lb1()

    def bind_quit(self, event):
        self.quit()

    def grab_aud(self):

        for lista in self.lista_indx:
            if lista[1] == self.index:
                wave_obj = sad.WaveObject.from_wave_file(lista[0])
                return wave_obj

    def play(self, wave_obj):

        play_obj = wave_obj.play()
        play_obj.wait_done()

    def gui( self):
        strings = self.current
        self.root = tk.Tk()
        self.root.geometry('490x100')
        self.root.config(
                                        bg='black', relief='raised', bd=3, highlightbackground='green',
                                        highlightcolor='green', highlightthickness=1)
        self.root.overrideredirect(1)

        self.frame = tk.Frame(self.root, bg='black', relief='flat')
        self.frame.bind("<i>", self.instructions)
        self.frame.bind("<space>", self.bind_play_b)
        self.frame.bind("<Right>", self.bind_foward)
        self.frame.bind("<Left>", self.bind_backward)
        self.frame.bind("<r>", self.bind_play_b)
        self.frame.bind("<Escape>", self.bind_quit)
        self.frame.bind("<ButtonPress-1>", self.start_window_move)
        self.frame.bind("<ButtonRelease-1>", self.stop_window_move)
        self.frame.bind("<B1-Motion>", self.on_move)
        self.frame.grid(column=0, row=0)

        self.lbl0 = tk.Label(self.frame, bg='black', fg='white', text='Controle de faixa:')
        self.lbl0.grid(column=0, row=0, padx=(0, 0))
        self.lb1 = tk.Label(
                            self.frame, bg='black', fg='yellow', text=self.faixa+'\n'+strings)
        self.lb1.grid(column=1, row=0, padx=(10, 90))

        self.bt0 = tk.Button(self.frame, bg='black', fg='white', text='<<<', command=self.bind_lss)
        self.bt0.grid(column=0, row=1, padx=(10, 0), pady=(20, 0), sticky='w')
        self.bt1 = tk.Button(self.frame, bg='black', fg='white', text='R')
        self.bt1.grid(column=0, row=1, padx=(60,0), pady=(20, 0), sticky='w')

        self.bt2 = tk.Button(self.frame, bg='black', fg='white', text=' S', command=self.bind_play)
        self.bt2.grid(column=0, row=1, padx=(98,0),  pady=(20, 0), sticky='w')
        self.bt3 = tk.Button(self.frame, bg='black', fg='white', text='D')
        self.bt3.grid(column=0, row=1, padx=(138, 0), pady=(20, 0), sticky='w')
        self.bt4 = tk.Button(self.frame, bg='black', fg='white', text='>>>', command=self.bind_pls)
        self.bt4.grid(column=0, row=1, padx=(176, 0),pady=(20, 0), sticky='w')
        self.bt5 = tk.Button(self.frame, bg='black', fg='grey', text='x', command=self.quit)
        self.bt5.grid(column=1, row=0, sticky='ne', padx=(220, 0))
        self.center()
        self.root.after(100, self.greeter)

        self.root.mainloop()



    def center(self):
        w = self.root.winfo_reqwidth()
        h = self.root.winfo_reqheight()
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        p = (ws / 2) - (w / 2)
        q = (hs / 2) - (h / 2)
        self.root.geometry('+%d+%d' % (p, q))
        self.frame.focus_set()

    def currents(self):
        if self.index == 0:
            self.current = self.nv_prod
        if self.index == 1:
            self.current = self.nv_cons_1
        if self.index == 2:
            self.current = self.nv_cons_2
        if self.index == 3:
            self.current = self.nv_cons_3
        if self.index == 4:
            self.current = self.nv_decomp
        return self.current

    def start_window_move(self,event):
        self.x = event.x
        self.y = event.y

    def stop_window_move(self, event):

        self.x = None
        self.y = None

    def on_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.root.winfo_x() + deltax
        y = self.root.winfo_y() + deltay
        self.root.geometry("+%s+%s" % (x, y))


    def quit(self):
        self.root.destroy()


if __name__ == '__main__':
    Audior()
