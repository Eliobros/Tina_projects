from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.clock import Clock
from datetime import datetime

Window.size = (400, 600)


class GerenciadorTelas(ScreenManager):
    pass

class PrimeiraTela(Screen):
    pass


class SegundaTela(Screen):
    pass

class VerHoras(Screen):
    def __init__(self, **kwargs):
        super(VerHoras, self).__init__(**kwargs)
        Clock.schedule_once(self.init_ver_horas)  # Chama o método para iniciar a atualização após a construção
        Clock.schedule_interval(self.ver_horas, 1)  # Atualiza a cada segundo
    
    def init_ver_horas(self, dt):
        self.ver_horas(0)  # Chama a função para exibir a hora
    
    def ver_horas(self, dt):
        horas = datetime.now().strftime("%H:%M:%S")
        self.ids.hora_label.text = f' {horas}'
        
class HoraApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(VerHoras(name='ver_horas'))
        
        
    
class FalarTina(Screen):
    pass






class TinaApp(App):
    def build(self):
        return GerenciadorTelas()


class ChatTina(Screen):
    def start_chat(self):
        # Oculta a interface inicial e exibe o chat
        self.ids.initial_box.opacity = 0
        self.ids.chat_box.opacity = 1

    def send_message(self):
        message = self.ids.input_message.text
        
        if message:
            # Adicionar a mensagem ao BoxLayout do chat
            self.ids.messages_box.add_widget(
                ChatBubble(text=message)
            )
            
            # Limpar a caixa de entrada
            self.ids.input_message.text = ''
            
            # Scroll para a última mensagem
            self.ids.scroll_chat.scroll_y = 0

class ChatBubble(BoxLayout):
    def __init__(self, text, **kwargs):
        super(ChatBubble, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = '40dp'
        
        # Adiciona a label com o texto da mensagem
        self.add_widget(Label(text=text, size_hint_x=None, width=200))
 
   
TinaApp().run()