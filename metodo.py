import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = 'InventoryPro'
    page.theme_mode = ft.ThemeMode.SYSTEM

    # Inicializa os campos de entrada e exibição
    dados_exibidos = ft.Text(value="", size=20)
    nome_usuario = ft.TextField(label="Nome do usuário", width=300)
    nome_ferramenta = ft.TextField(label="Nome da ferramenta", width=300)
    marca_ferramenta = ft.TextField(label="Marca da ferramenta", width=300)
    validade_ferramenta = ft.TextField(label="Validade (dd/mm/aaaa)", width=300)
    quantidade = ft.TextField(label="Quantidade", width=300)
    data_entrada = ft.TextField(label="Data de entrada (dd/mm/aaaa)", width=300)
    data_saida = ft.TextField(label="Data de saída (dd/mm/aaaa)", width=300)
    observacoes = ft.TextField(label="Observações adicionais", multiline=True, width=300)

    feedback_usuario = ft.Text(value="", color=ft.colors.GREEN)

    # Função para validar entradas
    def validar_dados():
        if not nome_usuario.value or not nome_ferramenta.value or not quantidade.value.isdigit():
            feedback_usuario.value = "Erro: Preencha todos os campos corretamente."
            feedback_usuario.color = ft.colors.RED
            page.update()
            return False
        try:
            datetime.strptime(validade_ferramenta.value, '%d/%m/%Y')
            datetime.strptime(data_entrada.value, '%d/%m/%Y')
            if data_saida.value:
                datetime.strptime(data_saida.value, '%d/%m/%Y')
        except ValueError:
            feedback_usuario.value = "Erro: Datas devem estar no formato dd/mm/aaaa."
            feedback_usuario.color = ft.colors.RED
            page.update()
            return False
        return True

    # Função para gravar novo dado no arquivo
    def gravar_arquivo(e):
        if not validar_dados():
            return

        novo_dado = (
            f'\n\n{"-"*30}\n'
            f'Nome: {nome_usuario.value}\n'
            f'Ferramenta: {nome_ferramenta.value}\n'
            f'Marca: {marca_ferramenta.value}\n'
            f'Validade: {validade_ferramenta.value}\n'
            f'Quantidade: {quantidade.value}\n'
            f'Data de entrada: {data_entrada.value}\n'
            f'Data de saída: {data_saida.value}\n'
            f'Adicional: {observacoes.value}'
        )
        with open('arquivo.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(novo_dado)

        # Limpa os campos após salvar
        resetar_campos()
        feedback_usuario.value = "Dados gravados com sucesso!"
        feedback_usuario.color = ft.colors.GREEN
        page.update()
        ler_arquivos()

    # Função para resetar os campos
    def resetar_campos():
        nome_usuario.value = ""
        nome_ferramenta.value = ""
        marca_ferramenta.value = ""
        validade_ferramenta.value = ""
        quantidade.value = "0"
        data_entrada.value = ""
        data_saida.value = ""
        observacoes.value = ""
        page.update()

    # Função para ler dados do arquivo
    def ler_arquivos():
        try:
            with open('arquivo.txt', 'r', encoding='utf-8') as arquivo:
                dados = arquivo.read()
                dados_exibidos.value = dados
                page.update()
        except FileNotFoundError:
            dados_exibidos.value = "Nenhum dado disponível."
            page.update()

    # Função para encerrar o programa
    def encerrar_programa(e):
        page.window_close()

    # Função para aumentar a quantidade
    def aumentar_quantidade(e):
        if quantidade.value.isdigit():
            quantidade.value = str(int(quantidade.value) + 1)
            page.update()

    # Função para diminuir a quantidade
    def diminuir_quantidade(e):
        if quantidade.value.isdigit() and int(quantidade.value) > 0:
            quantidade.value = str(int(quantidade.value) - 1)
            page.update()

    # Layout da interface gráfica
    page.add(
        ft.Column(
            controls=[
                ft.Text("InventoryPro", size=40, weight="bold"),
                ft.Text("Escolha uma opção:", size=20),
                feedback_usuario,  # Mostra feedback ao usuário

                # Botões para opções
                ft.ElevatedButton("Ler relatório completo", on_click=lambda e: ler_arquivos()),
                ft.ElevatedButton("Gravar dados de nova ferramenta", on_click=gravar_arquivo),

                # Layout para os dados de inscrição e container à direita
                ft.Row([
                    # Coluna para os campos de entrada
                    ft.Column(
                        controls=[
                            nome_usuario,
                            nome_ferramenta,
                            marca_ferramenta,
                            validade_ferramenta,
                            quantidade,

                            # Botões para aumentar e diminuir a quantidade
                            ft.Row([
                                ft.ElevatedButton("+", on_click=aumentar_quantidade),
                                ft.ElevatedButton("-", on_click=diminuir_quantidade),
                            ]),

                            data_entrada,
                            data_saida,
                            observacoes,
                        ],
                        width=450,  # Largura fixa para os campos de entrada
                    ),

                    # Container à direita para exibição dos dados com ListView para rolagem
                    ft.Container(
                        content=ft.ListView(
                            controls=[dados_exibidos],
                            expand=True
                        ),
                        height=1000,  # Altura fixa para a área de exibição
                        width=550,   # Largura fixa para o container
                        bgcolor=ft.colors.BLACK12,  # Cor de fundo
                        border_radius=10,  # Raio da borda
                        margin=ft.margin.only(left=20),  # Margem à esquerda
                    ),
                ]),

                # Botão para encerrar
                ft.ElevatedButton("Encerrar programa", on_click=encerrar_programa),
            ],
            scroll="auto",  # Barra de rolagem automática
            expand=True  # Expande o layout conforme o conteúdo
        )
    )

    page.update()

# Inicia o app Flet
ft.app(target=main)
