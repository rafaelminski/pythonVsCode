import PySimpleGUI as sg


class TelaPython:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('Nome',size=(5,0)), sg.Input(size=(15,0), key= 'Nome')],
            [sg.Text('Idade',size=(5,0)), sg.Input(size=(15,0), key='Idade')],
            [sg.Text('Quais provedores de e-mail são aceitos?')],
            [sg.Checkbox('Gmail', key='gmail'), sg.Checkbox('Outlook', key='outlook'), sg.Checkbox('Yahoo', key='yahoo')],
            [sg.Button('Enviar Dados')]

        ]
        #Janela
        janela = sg.Window("Dados do usuário").layout(layout)
        # Extrair dados da tela
        self.button, self.values = janela.Read()

    def Iniciar(self):
        Nome = self.values['Nome']
        Idade = self.values['Idade']
        aceita_gmail = self.values['gmail']
        aceita_outlook = self.values['outlook']
        aceita_yahoo = self.values['yahoo']
        print(f'Nome: {Nome}')
        print(f'Idade: {Idade}')
        print(f'aceita gmail: {aceita_gmail}')
        print(f'aceita outlook: {aceita_outlook}')
        print(f'aceita yahoo: {aceita_yahoo}')

tela = TelaPython()
tela.Iniciar()