from django.test import TestCase

from .models import Book
from . import views

class BookModelTestCase(TestCase):
    def setUp(self):
        Book.objects.create(name= "Jenkins & Yo",
							author= "Luis Zuniga",
							publisher= "ESPOL" )

        Book.objects.create(name= "Jenkins & Yo 2",
							author= "Luis Rosado",
							publisher= "ESPOL" )



    def test_crear_libro(self):
        nuevo_libro = Book.objects.create( name= "Mi nuevo libro",
									author= "Luis Fernando",
									publisher= "ESPOL" )
        self.assertTrue(isinstance(nuevo_libro, Book))
        self.assertEqual(str(nuevo_libro), "Mi nuevo libro")


    def test_buscar_un_libro(self):
    	self.assertEqual(1,0)


    def test_buscar_libro_por_autor(self):
    	self.assertEqual(1,0)


    def test_editar_libro(self):
    	self.assertEqual(1,0)


    def test_obtener_ruta_aboluta(self):
    	self.assertEqual(1,0)



class BookViewTests(TestCase):

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/book_list.html')

