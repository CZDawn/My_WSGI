# That module contains the controllers of the web application

from own_framework.templator import render

class Index:
    def __call__(self):
        return '200 OK', render('index.html')

class About:
    def __call__(self):
        return '200 OK', 'about' #TODO: сделать страницу о курсах и передать в render

class Contacts:
    def __call__(self):
        return '200 OK', 'contacts' #TODO: сделать страницу с контактами и передать в render

