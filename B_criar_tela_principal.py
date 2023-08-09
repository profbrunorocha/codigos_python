import PySimpleGUI as sg
import sqlite3 as bbb

 # Crie a conexão com o banco de dados
conn = bbb.connect("vendas.db")
c = conn.cursor()



# Crie a GUI
layout = [
    [sg.Button("Cadastrar")],
    [sg.Button("Consultar")],
    [sg.Button("Relatório")]
]


# Definindo o tamanho da fonte
""" fonte_texto = ('Arial', 25)
fonte_input = ('Arial', 25)
fonte_botao = ('Arial', 25) """

window = sg.Window("Sistema de vendas 1.0", layout, size=(600, 400))

# CASO QUEIRA COLOCAR: 1-BOTAO MAXIMIZAR, 2-AUMENTAR TAMANHO DO TEXTO, 3-TAMANHO DA TELA
# window = sg.Window("Sistema de vendas 1.0", layout, size=(800, 600), resizable=True, font=fonte_texto)

# Loop de eventos
while True:

    #No Python, os métodos vem depois dos componentes, diferente de outras linguagens
    #1-Ao compilar, abre a janela
    #2-Ao abrir a janela, alguma ação será feita. O método read lê essa ação
    #3-Enquanto for feito alguma acao... leia a acao
    #4-values: um dicionário do PySimpleGUI que tem todos os elementos gráficos de um componente gráfico, por exemplo, o input
    #5 valores do método READ lê um das ações: Event(ações com mouse) Values (ações com o teclado)

    event, values = window.read() 
    #Print("Janela aberta")

    if event == sg.WIN_CLOSED:
        break




""" 

    # Cadastros
    if event == "Cadastrar":
        # Crie a tela de cadastro
        cadastro_layout = [
            [sg.Text("Produto:", font=fonte_texto)],
            [sg.InputText(key="produto", font=fonte_input)],
            [sg.Text("Valor (R$):", font=fonte_input)],
            [sg.InputText(key="valor", font=fonte_texto)],
            [sg.Button("Cadastrar", font=fonte_botao)],
            [sg.Button("Cancelar", font=fonte_botao)]
        ]

        cadastro_window = sg.Window("Cadastro", cadastro_layout, size=(600, 400))

        # Loop de eventos
        while True:
            event, values = cadastro_window.read()

            if event == sg.WIN_CLOSED or event == "Cancelar":
                cadastro_window.close()
                break

            # Salve os dados no banco de dados
            c.execute("INSERT INTO vendas (produto, valor) VALUES (?, ?)", (values["produto"], values["valor"]))
            conn.commit()

            # Limpar os inputs após o cadastro
            cadastro_window["produto"].update("")
            cadastro_window["valor"].update("")

            # Mostrar pop-up de confirmação de cadastro
            sg.popup("Cadastro realizado com sucesso!", title="Cadastro")

        cadastro_window.close()








    #Consultas
    elif event == "Consultar":
        # Crie a tela de consulta
        consulta_layout = [
            [sg.Text("Produto:")],
            [sg.InputText(key="produto", font=fonte_input)],
            [sg.Button("Consultar", font=fonte_botao)],
            [sg.Button("Cancelar", font=fonte_botao)],
            [sg.Table(values=[], headings=["ID", "Produto", "Valor"], display_row_numbers=False, auto_size_columns=False, num_rows=10, key="tabela")]
        ]

        consulta_window = sg.Window("Consulta", consulta_layout, resizable=True)

        # Loop de eventos
        while True:
            event, values = consulta_window.read()

            if event == sg.WIN_CLOSED or event == "Cancelar":
                consulta_window.close()
                break

            # Consulte o banco de dados (ignorando case sensitive)
            produto_busca = values["produto"].upper()
            c.execute("SELECT id, produto, valor FROM vendas WHERE UPPER(produto) = ?", (produto_busca,))
            registros = c.fetchall()

            # Atualizar os dados da tabela (grid)
            tabela = consulta_window["tabela"]
            tabela.update(values=registros)

        consulta_window.close()

    





    #Relatorios 
    elif event == "Relatório":
        # Crie a tela de relatório
        relatório_layout = [
            [sg.Text("Produto:")],
            [sg.InputText(key="produto", font=fonte_input)],
            [sg.Button("Gerar relatório", font=fonte_botao)],
            [sg.Button("Cancelar", font=fonte_botao)]
        ]

        relatório_window = sg.Window("Relatório", relatório_layout, resizable=True)

        while True:
            event, values = relatório_window.read()

            if event == sg.WIN_CLOSED or event == "Cancelar":
                break

            # Consulte o banco de dados para obter o registro correspondente ao produto
            produto_busca = values["produto"].upper()
            c.execute("SELECT * FROM vendas WHERE UPPER(produto) = ?", (produto_busca,))
            registro = c.fetchone()

            if registro:
                # Gere o relatório em um arquivo HTML externo
                with open("relatorio.html", "w") as f:
                    f.write("<html><head></head><body>")
                    f.write(f"<h1>Relatório</h1><table border='1'><tr><th>ID</th><th>Produto</th><th>Valor</th></tr>")
                    f.write(f"<tr><td>{registro[0]}</td><td>{registro[1]}</td><td>{registro[2]}</td></tr>")
                    f.write("</body></html>")

                sg.popup("Relatório gerado com sucesso!", title="Relatório")
            else:
                sg.popup("Produto não encontrado no banco de dados.", title="Relatório")

            # Limpar o input após gerar o relatório
            relatório_window["produto"].update("")

        relatório_window.close()

 """
# Feche a conexão com o banco de dados
conn.close()
