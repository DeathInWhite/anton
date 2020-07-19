import webbrowser

class Python():
        
    def recibiendo_pregunta(self,pregunta,tipo_respuesta):
        if 'creo' and 'clase' or 'crear' and 'clase' in pregunta:
            return self.como_crear_clase(tipo_respuesta)
            
        
    def como_crear_clase(self,tipo_respuesta):
        if tipo_respuesta in 'palabras':
            return 'Para crear una clase primero debes escribir: class, nombre de la clase, parentesis y dos puntos'
        else:
            webbrowser.get().open('https://www.w3schools.com/python/python_classes.asp')
            return 'Aca te abro una pagina'
        
    