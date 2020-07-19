from django.db import models
from django.contrib.auth.models import User
from stdimage.models import StdImageField, JPEGField

class UserRole(models.Model):
    ROLE_CHOICES = [
        ('1', 'Analista de Testes'),
        ('2', 'Testador'),
    ]
    role = models.CharField(max_length=1, choices=ROLE_CHOICES)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagem = StdImageField('Imagem', upload_to='imagemUserProfile',
                           variations={'thumb': 
                                            {'width': 60, 'height': 60, 'crop': True}
                                      },
                           default="imagemUserProfile/padrao.png", delete_orphans=True)
    reputacao = models.IntegerField('Reputação', default=0)
    experiencia = models.IntegerField('Experiência', default=0)
    role = models.OneToOneField(UserRole, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.get_full_name()
