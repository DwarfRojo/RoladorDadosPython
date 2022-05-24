from random import randint
import PySimpleGUI as sg

saida = ''
#Geradores de dados
def d4():

    generator = randint(1, 4)
    return generator

def d6():
    generator = randint(1, 6)
    return generator

def d8():
    generator = randint(1, 8)
    return generator

def d10():
    generator = randint(1, 10)
    return generator

def d12():
    generator = randint(1, 10)
    return generator

def d20():
    generator = randint(1, 20)
    return generator

def d100():
    generator = randint(1, 100)
    return generator

def custom(valor):
    generator = randint(1, valor)
    return generator

#Interface
column1 = [
    [sg.Button('D4', size=(4, 1), key='D4'), sg.Button('D6', size=(4, 1), key='D6')],
    [sg.Button('D8', size=(4, 1), key='D8'),sg.Button('D10', size=(4, 1), key='D10')],
    [sg.Button('D12',size=(4, 1), key='D12'), sg.Button('D20',size=(4, 1), key='D20')],
    [sg.Button('D100', size=(4, 1), key='D100')]
        ]
column2 = [
    [sg.Text('Boas Rolagens!', size=(8,5), key='Resultado', justification='center')]
           ]

layout = [[
    sg.Column(column1), sg.Column(column2)
]]

window = sg.Window('Rolador de dados', layout)

#Eventos
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'D4':
        window['Resultado'].update(f'{d4()}')
    elif event == 'D6':
        window['Resultado'].update(f'{d6()}')
    elif event == 'D8':
        window['Resultado'].update(f'{d8()}')
    elif event == 'D10':
        window['Resultado'].update(f'{d10()}')
    elif event == 'D12':
        window['Resultado'].update(f'{d12()}')
    elif event == 'D20':
        window['Resultado'].update(f'{d20()}')
    elif event == 'D100':
        window['Resultado'].update(f'{d100()}')



window.close()
