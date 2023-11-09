from django.db import models

# Create your models here.

class Qrgen(models.Model):
    titolo = models.CharField(max_length=100)
    contenuto = models.TextField()
    image = models.FileField(upload_to='qrgen_images/',blank=True)
    note = models.TextField()

# funzione per restituire il nome dell'istanza nel pannello admin di django
    def __str__(self):
        return self.titolo #or self.name
    

    