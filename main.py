import PySimpleGUI as sg
from klases import gainedFruit as gfruit
from klases import Ievarijums as iev

#Galvenais menu.
MainMenu = [[sg.Button("Pievienot dārzeņus"), sg.Button("Pieliekamais")]]

#Ražas ievades menu.
InputMenu = [[sg.Text("Ierakstiet dārzeņus")],
                [sg.Text("Dārzenis: "), sg.InputText()],
                [sg.Text("Daudzums: "), sg.InputText(), sg.Text("kg")],
                [sg.Text("Dārzenis vai auglis?: "), sg.Radio("Auglis", group_id="fruit", default=True), sg.Radio("Dārzenis", group_id="fruit")],
                [sg.Button("Pievienot"), sg.Button("Atpakaļ")]]

#Ražas menu.
StockMenu = [[sg.Listbox(values=[],key="output", size=(40,40)),
                sg.Button("Atpakaļ."), sg.Button("Pārvērst ievārijumā")]] # To Do: Atrast veidu kā "Noņemt" poga strādātu bez problēmām.

#Nodefinē kā aplikācija atverās.
Layout = [[sg.Column(MainMenu, key="Main"), sg.Column(StockMenu, visible=False, key="Inv"), sg.Column(InputMenu, visible=False, key="Input")]]

Stack=[]

sg.theme('DarkRed') #Nosaka krāsas aplikācijai.
window = sg.Window('Ražu uzskaite :D', Layout) #Aplikācijas nosaukums, un izsauc "Layout".
while True:
        event, values = window.read()
        if event == "Pievienot dārzeņus": #Pogas kontrolē kuri logi ir parādīti. 
                window['Main'].update(visible=False)
                window['Input'].update(visible=True)

        if event == "Pieliekamais":
                window['Main'].update(visible=False)
                window['Inv'].update(visible=True)

        if event == "Pievienot": #Pievieno dotos datus.
                Stack.append(gfruit(values[0], values[1], values[2]))
                stack=[]
                for i in range(len(Stack)):
                        stack.append(Stack[i].val())
                window["output"].update(values=stack)

        if event == "Atpakaļ": #Atpakaļ poga ražas ievades menu.
                window['Main'].update(visible=True)
                window['Input'].update(visible=False)
        if event == "Atpakaļ.": #Atpakaļ poga ražas menu (nevarēju atrast veidu kā izmantot tikai vienu)
                window['Main'].update(visible=True)
                window['Inv'].update(visible=False)
                
        if event == "Pārvērst ievārijumā": #Pārvērš izvēlēto uz ievārījumu.
                selected_items = values["output"]
                Stack.append(iev(values[0], values[1]))
                stack=[]
                for i in range(len(Stack)):
                        stack.append(Stack[i].val())
                window["output"].update(values=stack)
        
        if event == sg.WIN_CLOSED:
                break
          
window.close()
