from django.contrib import admin
from .models import Datasample
from .models import UploadFile

# Register your models here.
admin.site.register(Datasample)
admin.site.register(UploadFile)