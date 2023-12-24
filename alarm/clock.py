# Importando os módulos necessários
import tkinter
from time import strftime

# Criando a janela principal da aplicação
top = tkinter.Tk()
top.title("Relógio")  # Definindo o título da janela
top.resizable(False, False)  # Tornando a janela não redimensionável

# Função para atualizar a exibição do tempo
def time():
    # Obtendo a hora atual no formato HH:MM:SS AM/PM
    string = strftime("%H:%M:%S %p")

    # Atualizando o texto do rótulo clockTime com a hora atual
    clockTime.config(text=string)

    # Agendando a função time para ser chamada novamente após 1000 milissegundos (1 segundo)
    global after_id
    after_id = clockTime.after(1000, time)

# Criando um widget Label para exibir o tempo
clockTime = tkinter.Label(
    top,
    font=("courier new", 40),
    background="black",
    foreground="yellow",
)

# Posicionando o widget Label no centro da janela
clockTime.pack(anchor="center")

# Chamando a função time para começar a atualizar a exibição do tempo
time()

def quit_app(_=None):  # substituí 'event=None' por '_=None' para retirar o aviso de 'Parameter 'event' value is not used'.
    clockTime.after_cancel(after_id)
    top.destroy()

top.protocol("WM_DELETE_WINDOW", quit_app)

try:
    # Iniciando o loop principal de eventos Tkinter
    top.mainloop()

except KeyboardInterrupt:
    print("Programa interrompido pelo usuário.")
