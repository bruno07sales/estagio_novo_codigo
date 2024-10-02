#Crie um programa que calcule o IMC do usuário, em Flet. Ao terminar, envie o link do repositório.
import flet as ft

#Rever essa parte para criar logica nova do codigo
def main(page: ft.Page):
    def calcular_imc(e):
        imc = float(peso.value.replace(',','.')) / (float(altura.value.replace(',','.')) ** 2)
        ##result.value = f'{nome.value} seu IMC é: {imc:.2f}'
        nome_ferramenta.value= str

        if imc < 18.5:
                result.value += ' (Abaixo do peso)'
        elif 18.5 <= imc < 24.9:
            result.value += ' (Peso normal)'
        elif 25 <= imc < 29.9:
            result.value += ' (Sobrepeso)'
        else:
            result.value += ' (Obesidade)'
        

        page.update()

    

    nome = ft.TextField(label='Nome')
    nome_ferramenta = ft.TextField(label='Nome da Ferramenta')
    peso = ft.TextField(label='Cor', suffix_style=ft.TextStyle(color='grey'))
    altura = ft.TextField(label='Relatorio', suffix_text='metros', suffix_style=ft.TextStyle(color='grey'), on_submit=calcular_imc)
    result = ft.Text(size=30, color= '#D02323')

    botao = ft.ElevatedButton('Registrar',
         bgcolor='#53B63B',
         color='white',
         
         elevation=10,
         on_click= calcular_imc,
         width=300, #largura
         height=50 #altura
         
         
         
    )

    page.title = 'Registro de Ferramentas'
    page.scroll = 'adaptive'
    page.theme_mode = ft.ThemeMode.LIGHT

    page.add(
         ft.Row(
              [ft.Text('Registro de Ferramentas', size=40, weight='bold')],
              alignment=ft.MainAxisAlignment.CENTER
         ),
         ft.Row(
              [nome],
              alignment=ft.MainAxisAlignment.CENTER
         ),
         ft.Row(
              [nome_ferramenta],
              alignment=ft.MainAxisAlignment.CENTER
         ),
         ft.Row(
              [peso],
              alignment=ft.MainAxisAlignment.CENTER
         ),
         ft.Row(
              [altura],
              alignment=ft.MainAxisAlignment.CENTER
         ),
         ft.Row(
              [botao],
              alignment=ft.MainAxisAlignment.CENTER
         ),
         ft.Row(
            [result],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
    page.update()

ft.app(main)