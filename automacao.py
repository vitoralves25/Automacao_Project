import pyautogui
from time import sleep
# Passo 1 - Acessar o google chrome
        #pyautogui.click - para clickar em algum lugar
        #pyautogui.write - para escrever --> lembrando somente aceita string
        #pyautogui.PAUSE - para dar uma pausa a cada comando feito pelo pyautogui
        #pyautogui.press - para pressionar algum botão do teclado --> Lembrando só aceita uma tecla

pyautogui.PAUSE = 0.5


pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")


pyautogui.press("enter")
sleep(2)

#Atualizei aqui para testar

# Passo 1.1 - Saber a posição da onde meu mouse está

# passo 1.2 - pressionar na posição do mouse

pyautogui.click(x=549, y=375)




# Passo 2 - Acessar o site


pyautogui.press("enter")
sleep(2)

# Passo 3 -  Cadastrar o Login

pyautogui.click(x=549, y=375)

pyautogui.write("alvesbazeth881@gmail.com")
pyautogui.press("tab")
pyautogui.write("26620908&v")
pyautogui.press("tab")
pyautogui.press("enter")

# Passo 4 -  Cadastrar um produto manualmente



import pandas
tabela_de_dados = pandas.read_csv("produtos.csv") # pra importar a base de dados precisa colocar esse r antes

print(tabela_de_dados)

for linha in tabela_de_dados.index:
    pyautogui.click(x=784, y=258)
    


    codigo = str(tabela_de_dados.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    

    marca = str(tabela_de_dados.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    
    
    tipo = str(tabela_de_dados.loc[linha, "tipo"])
    pyautogui.write(tipo)
    
    
    pyautogui.press("tab")

    categoria = str(tabela_de_dados.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str(tabela_de_dados.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(tabela_de_dados.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")


    
    obs = str(tabela_de_dados.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    
        
    
    
    pyautogui.press("tab")
    
    pyautogui.press("enter")    
    
    pyautogui.scroll(10000)
# Passo 5 -  Repetir todos os outros produtos