import PySimpleGUI as sg
import database 

db = database.DBCliente()

tp_f = db.get_tipo_telefone()
fones = []
for f in tp_f:
    fones.append(tp_f[f])
tp_e = db.get_tipo_endereco()
ends = []
for e in tp_e:
    ends.append(tp_e[e])



sg.theme('Reddit')

menu_def = [
    ['Cadastro', ['Pesquisar','Sair']],
    ['Ajuda', ['Ajuda','Sobre']]
]

tab_pessoal = [
    [sg.T('CPF:'),sg.Input(key='-CPF-',size=12,enable_events=True),sg.Text('somente números, não digitar pontos e traços ', font='Arial 10', text_color='grey' )],
    [sg.Text('Nome: '),sg.Input(key='-NAME-')],
    [sg.Text('email:'),sg.Input(key='-EMAIL-')]
]

tab_endereco = [
    [sg.T('Tipo endereço:'),sg.OptionMenu(values=ends,key='-END1-')],
    [sg.Text('Logradouro:'),sg.Input(key='-ADDRESS-')],
    [sg.Text('Numero:'),sg.Input(key='-NUMBER-',size=(6,1)),sg.Text('Complemento:'),sg.Input('optional',key='-COMP-')]
]

tab_telefone = [
    [sg.T('         '),sg.T('DDD'),sg.T('Número     '),sg.T('Tipo')],
    [sg.T('Telefone:'),sg.Input(key='-DDD1-',size=(3,1)),sg.Input(key='-FONE1-',s=(10,1)),sg.OptionMenu(values=fones,key='-TIPO-F1-')],
    [sg.T('Telefone:'),sg.Input(key='-DDD1-',size=(3,1)),sg.Input(key='-FONE2-',s=(10,1)),sg.OptionMenu(values=fones,key='-TIPO-F2-')],
    [sg.T('Telefone:'),sg.Input(key='-DDD1-',size=(3,1)),sg.Input(key='-FONE2-',s=(10,1)),sg.OptionMenu(values=fones,key='-TIPO-F3-')]
]

tab_grupo = [
    sg.Tab('Dados Pessoais', layout=tab_pessoal),
    sg.Tab('Endereço', layout=tab_endereco),
    sg.Tab('Contato', layout=tab_telefone)
]


layout = [
    [sg.Menu(menu_def)],
    [sg.T('Cadastro de Clientes')],
    [sg.TabGroup([tab_grupo])],
    [sg.VPush()],
    [sg.Push(),sg.Button('Cancelar',button_color='RED'),sg.Button('Salvar')]
]

window = sg.Window('Cadastro de Clientes',layout=layout,size=(800,600),font="Monaco 14",resizable=True,margins=(1,1))

while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED or event == 'Sair':
        break
    if event == '-CPF-':
        digits = '0123456789'
        if value['-CPF-'][-1] not in digits or len(value['-CPF-']) > 11:
            window['-CPF-'].update(value['-CPF-'][:-1])
    if event == 'Pesquisar':
        termo = sg.popup_get_text('Digite o CPF ou o nome:',font='Monaco 14')
        cliente_dict = db.get_cliente(termo)
        print(cliente_dict)


window.close()