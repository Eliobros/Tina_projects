from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
import requests

API_KEY = "0fd350a9b489561356ca2255db6307c3"  # Substitua pela sua chave API do TMDB
BASE_URL = "https://api.themoviedb.org/3"
SEARCH_URL = BASE_URL + "/search/movie"

class MovieSearchApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        
        self.search_input = TextInput(size_hint_y=None, height=40, multiline=False, hint_text='Digite o nome do filme')
        self.search_button = Button(text='Pesquisar', size_hint_y=None, height=40)
        self.search_button.bind(on_press=self.search_movie)
        
        self.result_label = Label(size_hint_y=None, height=800, text='Resultados aparecerão aqui.')
        self.scroll_view = ScrollView(size_hint=(1, None), size=(self.layout.width, 400))
        self.scroll_view.add_widget(self.result_label)

        self.layout.add_widget(self.search_input)
        self.layout.add_widget(self.search_button)
        self.layout.add_widget(self.scroll_view)

        return self.layout

    def search_movie(self, instance):
        query = self.search_input.text
        if query:
            response = requests.get(
                SEARCH_URL,
                params={'api_key': API_KEY, 'query': query}
            )
            data = response.json()
            self.display_results(data)

    def display_results(self, data):
        movies = data.get('results', [])
        if not movies:
            self.result_label.text = 'Nenhum filme encontrado.'
            return

        results = ''
        for movie in movies:
            title = movie.get('title', 'Título desconhecido')
            overview = movie.get('overview', 'Sem descrição')
            results += f"Title: {title}\nOverview: {overview}\n\n"
        
        self.result_label.text = results

if __name__ == '__main__':
    MovieSearchApp().run()
