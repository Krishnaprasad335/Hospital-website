from django.db import models

# Create your models here.
class Department(models.Model):
    depart_name=models.CharField(max_length=100,blank=True,null=True)
    depart_decs=models.TextField()

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Department'

    def __str__(self):
        return   self.depart_name 

class Doctors(models.Model):
    doc_name=models.CharField(max_length=100,null=True,blank=True) 
    doc_spec=models.CharField(max_length=100,null=True,blank=True) 
    depart_name=models.ForeignKey(Department,on_delete=models.CASCADE)
    doc_image=models.ImageField(upload_to='doctor')   

    class Meta:
        verbose_name = 'Doctors'
        verbose_name_plural = 'Doctors' 
    def __str__(self):
        return   self.doc_name 

class booking(models.Model):
    p_name=models.CharField(max_length=100)
    p_phone=models.CharField(max_length=100)
    p_email=models.EmailField()
    doc_name=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)
    class Meta:
        verbose_name = 'booking'
        verbose_name_plural = 'booking'                

    