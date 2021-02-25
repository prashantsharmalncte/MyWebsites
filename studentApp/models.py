from django.db import models  
class studentdetails(models.Model):  
    studentName = models.CharField(max_length=30)  
    studentRollNo = models.CharField(max_length=30)  
    class Meta:  
        db_table = "studentdetails"  
