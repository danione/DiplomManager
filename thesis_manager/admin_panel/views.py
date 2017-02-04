# Look up the methods POST/PUT/DELETE
# Delete or Not?!
# Archives
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Student, ManagmentAndReview, Thesis
import csv
import os


def get_archive_dir():
    return os.getcwd() + '/archives/'

def init_list():
    return list(Student.objects.order_by('student_class','student_name'))

def delete_information():
    Student.objects.all().delete()


def admin_homepage(request):
    students_list_document = init_list()
    students_list_assignment = init_list()
    students_list_reviewer = init_list()
    students_list_commission  = init_list()

    students_list_document = [student for student in students_list_document if student.handed_document_over == False]
    students_list_assignment = [student for student in students_list_assignment if student.handed_assignment_over == False]
    students_list_reviewer = [student for student in students_list_reviewer if student.has_reviewer == False]
    students_list_commission = [student for student in students_list_commission if student.has_commission == False]

    context = {'students_list_document': students_list_document,'students_list_assignment' : students_list_assignment,
               'students_list_reviewer': students_list_reviewer,'students_list_commission' : students_list_commission}
    return render(request, 'admin_homepage.html', context)
# We need to keep it secret, keep it safe! Every student gets a field -> graduated? and it is PUT!
def empty_tables(request):
    delete_information()
    return HttpResponseRedirect('redirection')

def new_year(request):
    return render(request, 'new_year.html')

def deleting_database(request):
    if request.method == 'POST':
        directory = get_archive_dir()
        os.remove(directory + request.POST.get('delete'))
        return HttpResponseRedirect('redirection')

    return (request,'man_years.html')

def load_database(request):
    if request.method == 'POST':
        directory = get_archive_dir()
        delete_information()
        with open(directory + request.POST.get('load'), 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                Student(student_name = row[1], student_class = row[2], student_number = row[0], category = row[3], handed_document_over = row[4], handed_assignment_over = row[5],
                has_commission = row[6], has_reviewer = row[7]).save()
            return HttpResponseRedirect('redirection')
    return (request, 'man_years.html')


def saving_database(request):
    if request.method == 'POST':
        raw_name = request.POST.get('SaveYear')
        students_list = init_list()
        directory = get_archive_dir()

        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(directory + raw_name + '.csv', 'w+', newline='') as csvfile:
            writer = csv.writer(csvfile)

            for student in students_list:
                writer.writerow([student.student_number,student.student_name, student.student_class, student.category, student.handed_document_over,student.handed_assignment_over,
                student.has_reviewer, student.has_commission])
            return HttpResponseRedirect('redirection')

    return (request,'man_years.html')

def man_years(request):
    directory = get_archive_dir()
    archives = [files for files in os.listdir(directory) if os.path.isfile(os.path.join(directory, files))]
    context = {'archives' : archives}
    return render(request, 'man_years.html', context)


def student_handler(request):
    if request.method == 'POST':
        name_ = request.POST.get('FullName')
        class_ = request.POST.get('Class')
        number_ = request.POST.get('Number')
        software_ = False;
        if request.POST.get('software-hardware') == 0:
            software_ = True;
            Student(student_name = name_ , student_class = class_ , student_number = number_ , system_programming = software_).save()
            return HttpResponseRedirect('redirection')

    return(request, 'upload_student.html')

def file_handler(request):
    if request.method == 'POST':
        extension = request.FILES['text_csv'].name.split('.')[1]
        if extension == 'txt':
            my_file = request.FILES['text_csv'].read().decode('cp1251')
            rows = my_file.split('\r\n')
            class_ = None
            software_ = False
            for row in rows:
                if row[:1] == 'X':
                    class_ = row[-1:].upper()
                elif row[:1] == 'S':
                    software_ = True
                elif row[:1] == 'H':
                    software_ = False
                else:
                    if len(row) > 1:
                        information = row.split('.')
                        number_ = information[0]
                        student_ = information[1].replace(' ','',1)
                        Student(student_name=student_, student_class=class_, student_number = number_, system_programming = software_ ).save()
        return HttpResponseRedirect('redirection')
    return(request,'upload_student.html')

def upload_students(request):
    return render(request, 'upload_student.html')

def teacher_handler(request):
    if request.method == 'POST':
        name_ = request.POST.get('FullName')
        titles_ = request.POST.get('Title')
        work_ = request.POST.get('Work')
        software_ = False;
        if request.POST.get('software-hardware') == 0:
            software_ = True;
        Teacher(teacher_name = name_ , titles = titles_ , place_of_work = work_ , system_programming = software_).save()
        return HttpResponseRedirect('redirection')
    return(request, 'upload_teacher.html')

def upload_teachers(request):
    return render(request, 'upload_teacher.html')


def upload_thesis(request):
    return render(request, 'upload_thesis.html')

def upload_reviewers(request):
    return render(request, 'upload_reviewer.html')

def reviewer_handler(request):
    if request.method == 'POST':
        name_ = request.POST.get('FullName')
        titles_ = request.POST.get('Title')
        work_ = request.POST.get('Work')
        Reviewer(teacher_name = name_ , titles = titles_ , place_of_work = work_).save()
        return HttpResponseRedirect('redirection')
    return(request, 'upload_reviewer.html')



def thesis_handler(request):
    if request.method == 'POST':
        description_ = request.POST.get('ThesisDescription')
        software_ = False;
        hardware_ = False;
        if request.POST.get('software-hardware') == 0:
            software_ = True;
        elif request.POST.get('software-hardware') == 1:
            hardware_ = True;
        Thesis(thesis_description = description_, software = software_, hardware = hardware_).save()
        return HttpResponseRedirect('redirection')

    return(request, 'upload_thesis.html')

def assign_document(request):
    return render(request, 'document_assign.html')


def listing(request):
    return HttpResponse("listing")
