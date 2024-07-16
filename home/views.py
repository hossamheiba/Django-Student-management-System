from django.shortcuts import render , redirect
from .models import Students
from .forms import Students_form

def home_page(requset):
    return render (requset , 'home/home_page.html')


def students_information(requset):
    students = Students.objects.all()
    context={'students':students}
    return render(requset , "students/students.html" , context)


def students_details(requset , slug):
    students_detail = Students.objects.get(slug = slug)
    context={'students_detail': students_detail}
    return render(requset , "students/students_details.html" , context)

# CRUD
def students_edit(requset , slug):
    student_edit = Students.objects.get(slug = slug)
    if requset.method == 'POST':
        edit=Students_form(requset.POST, requset.FILES, instance=student_edit)
        if edit.is_valid():
            edit.save()
            return redirect("/")
    else:
        edit=Students_form(instance=student_edit)

    context={'edit': edit}
    return render(requset , "students/students_edit.html" , context)


def students_delete(requset , slug):
    student_delete = Students.objects.get(slug = slug)
    if requset.method == 'POST':
            student_delete.delete()
            return redirect("/students")

    return render(requset , "students/students_delete.html" )


def students_create(requset):
    if requset.method == 'POST':
        create = Students_form(requset.POST, requset.FILES, )
        if create.is_valid():
            create.save()
            return redirect('/students')
    else:
        create = Students_form()
    context={'create':create}
    return render(requset , 'students/students_create.html' , context)
        
