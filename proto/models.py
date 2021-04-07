from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, ValidationError
import re
# Create your models here.
def number_only(value):
    if (re.match(r'^[0-9]*$', value) == None):
        raise ValidationError('%(value)s is not Number!', params={'value': value},)
class Rank(models.Model):
    name = models.CharField(max_length=100)
    point = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100000000)])
    datepoint = models.DateField()

    def __str__(self):
        return '<Rank:id=' + str(id) + ', ' + self.name + '(' +str(self.point) + ')>'

class Message(models.Model):
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '<Message:id=' + str(self.id) + ', ' + self.title +'(' +str(self.pub_date) + ')>'
    
    class Meta:
        ordering = ('pub_date',)