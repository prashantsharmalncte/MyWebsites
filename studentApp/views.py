from django.shortcuts import render,redirect
from django.http import HttpResponse
from studentApp.forms import StudentForm  
from studentApp.models import studentdetails  
import mysql.connector

def showform(request):
    if request.method == "POST":  
        form = StudentForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except Exception as ex: 
                print(ex) 
                pass  
    else:  
        form = StudentForm()  
    return render(request,'studentForm.html',{'form':form})  

def deleteData(request):
    name =  request.GET["studentName"]
    studentdetails.objects.filter(studentName=name).delete()
    return HttpResponse("<h1>Deleted</h1>")
def updateData(request):
    name =  request.POST["studentName"]
    rollno =  request.POST["studentRollNo"]
    studentdetails.objects.filter(studentName=name).update(studentRollNo=rollno)
    return HttpResponse("<h1>Updated</h1>")

def index(request):
    return render(request,'index.html',{ "name" : "Prashant Sharma" })

def show(request):
    try:
        #studentdata = studentdetails.objects.filter(studentName = "anuj")
        studentdata = studentdetails.objects.all()
        str=""
        for student in studentdata:
            str = str  + student.studentName + "       " +  student.studentRollNo + "<br>"
        return HttpResponse(str)
    except:
        return HttpResponse("<h1>Not Done</h1>")
     

def insert(request):
    if request.method == "GET": 
        return render(request,'success.html',{ "name" : "Prashant Sharma" }) 
    else:
        studentName=request.POST['studentName']
        studentRollNo=request.POST['studentRollNo']
        mydb = mysql.connector.connect(host="localhost",
            user="root",
            password="root",
            database="studentdb")
        mycursor = mydb.cursor()
        sql = "INSERT INTO studentdetails (studentName, studentRollNo) VALUES (%s, %s)"
        val = (studentName, studentRollNo)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        return HttpResponse("<h1>Successfully Inserted " + str(mycursor.rowcount) + "</h1>")
        


    