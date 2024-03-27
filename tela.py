from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MainLayout(GridLayout):
    def __init__(self,**kwargs):
        super(MainLayout,self).__init__(**kwargs)

        self.cols = 1

        self.sub_layout = GridLayout()
        self.sub_layout.cols = 2

        #Criando a label nome
        self.nome_do_label = Label(text='Nome:')
        #Adicionando label nome ao layout
        self.sub_layout.add_widget(self.nome_do_label)

        #Criando o textinput nome
        self.nome_do_cliente = TextInput(multiline=False)
        self.sub_layout.add_widget(self.nome_do_cliente)

        ################################################################

        #Criando a label mesa
        self.mesa_label = Label(text='Mesa:')
        #Adicionando label mesa ao layout
        self.sub_layout.add_widget(self.mesa_label)

        #Criando o textinput mesa
        self.mesa = TextInput(multiline=False)
        self.sub_layout.add_widget(self.mesa)

        ################################################################

        #Criando a label pedido
        self.pedido_label = Label(text='Pedido:')
        #Adicionando label pedido ao layout
        self.sub_layout.add_widget(self.pedido_label)

        #Criando o textinput pedido
        self.pedido = TextInput(multiline=True)
        self.sub_layout.add_widget(self.pedido)

        ################################################################


        #Adicionando o sublayout ao layout principal
        self.add_widget(self.sub_layout)

    #Criando botao enviar
        self.enviar = Button(text='Enviar pedido')
    #Adicionando a função de callback ao botão
        self.enviar.bind(on_press=self.enviar_pedido)
    #Adicionando boatao enviar no label
        self.add_widget(self.enviar)

    def enviar_pedido(self, instance):
        #Criando o label de confirmação
        self.confirmacao = Label(
            text=f'Cliente: {self.nome_do_cliente.text}\nMesa:{self.mesa.text}\nPedido:{self.pedido.text}'
            )
        
        self.add_widget(self.confirmacao)


        #limpando os campos de texto
        self.nome_do_cliente.text = ''
        self.mesa.text = ''
        self.pedido.text = ''



class LanchoneteApp(App):
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    LanchoneteApp().run()