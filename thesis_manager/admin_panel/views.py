from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Student

def admin_homepage(request):
    students_list = list(Student.objects.order_by('student_class','student_name'))
    for student in students_list:
        student.has_document = True;
        if student.has_document == True:
            students_list.remove(student)
    context = {'students_list': students_list}
    return render(request, 'admin_homepage.html', context)

def new_year(request):
    return render(request, 'new_year.html')

def man_years(request):
    return render(request, 'man_years.html')

def upload_students(request):
    return render(request, 'upload_student.html')

def upload_teachers(request):
    return render(request, 'upload_teacher.html')

def upload_thesis(request):
    return render(request, 'upload_thesis.html')

def upload_reviewers(request):
    return render(request, 'upload_reviewer.html')

def student_handler(request):
    if request.method == 'POST':
        name_ = request.POST.get('FullName')
        class_ = request.POST.get('Class')
        number_ = request.POST.get('Number')
        software_ = False;
        if request.POST.get('software') == 'on':
            software_ = True;
        Student(student_name=name_,student_class=class_,student_number=number_, system_programming=software_).save()
        return HttpResponseRedirect('redirection')

    return(request, 'upload_student.html')


def listing(request):
    return HttpResponse("listing")
