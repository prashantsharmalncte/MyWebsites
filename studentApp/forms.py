from django import forms  
from studentApp.models import studentdetails 
class StudentForm(forms.ModelForm):  
    class Meta:  
        model = studentdetails  
        fields = "__all__"  