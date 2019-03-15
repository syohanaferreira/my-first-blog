from django.db import models
# Importamos la misma hora que tiene la carpeta mysite.
from django.utils import timezone
# Class hace referencia a que estamos creando un objeto
# models.Model hace referencia a que Post es un modelo Django
class Post(models.Model):
    # author, title, text, created_date, published_date son propiedades
    # modelos.ForeignKey significa que hay una relación con otro modelo, es clave foránea.
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    #CharField es para un texto con un
    # numero limitado de caracteres, en este caso son 200 caracteres
    title = models.CharField(max_length=200)
    #TextField es para textos largos, sin limite
    text = models.TextField()
    # DateTimeField es para definir horas y fechas
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
