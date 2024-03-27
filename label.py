from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget

#Cria o objeto do app
class MyWidget(Widget):
    pass

class LabelApp(App):

    # Este metodo é chamado quando o aplicativo é iniciado
    # Deve sempre se chamar build
    def build(self):
    
    #Metodo para criar um label dentro do codigo usando a classe label
    #    label = Label(
    #        text="Hello World!",
    #        font_size='100sp',
    #        bold=True,
    #        italic=True,
    #        color=(222/255.0, 179/255.0, 255/255.0,1),
    #        #alinha o texto a direita
    #        halign="left",
    #        valign="middle",
    #        text_size=(400,400)
    #                  )
    #    return label

        return MyWidget()


#incia o aplicativo
if __name__ == '__main__':
    LabelApp().run()