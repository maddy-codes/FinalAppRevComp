from django.db import models

def upload_to_docs(instance, filename):
    return 'docs/' + filename

def upload_to_excel(instance, filename):
    return 'excel/' + filename

# Create your models here.
class NameFile(models.Model):
    name = models.CharField(max_length=200)
    file = models.FileField(null=True, upload_to=upload_to_docs)

    def __str__(self):
        return self.name
    
    
class ExcelDate(models.Model):
    end_date = models.CharField(max_length=200)
    excel_sheet = models.FileField(null=True, upload_to = upload_to_excel)