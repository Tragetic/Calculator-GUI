import PySimpleGUIWeb as sg

layout = [
  [sg.InputText()],
  [sg.Button('CE', size=(50,50)), sg.Button('Backspace', size=(80,50)), sg.Button('Enter', size=(80,50))],
  [sg.Button('7', size=(50,50)), sg.Button('8', size=(50,50)), sg.Button('9', size=(50,50)), sg.Button('/', size=(50,50))],
  [sg.Button('4', size=(50,50)), sg.Button('5', size=(50,50)), sg.Button('6', size=(50,50)), sg.Button('*', size=(50,50))],
  [sg.Button('1', size=(50,50)), sg.Button('2', size=(50,50)), sg.Button('3', size=(50,50)), sg.Button('-', size=(50,50))],
  [sg.Button('+/-', size=(50,50)), sg.Button('0', size=(50,50)), sg.Button('.', size=(50,50)), sg.Button('+', size=(50,50))],
]

window = sg.Window('Py Calculator', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()