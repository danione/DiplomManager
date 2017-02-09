# Look up the methods POST/PUT/DELETE
# Delete or Not?!
# Archives
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Student, ManagmentAndReview, Thesis, Commission
from django.shortcuts import get_object_or_404
import csv
import os


def get_archive_dir():
    return os.getcwd() + '/archives/'

def init_list():
    return list(Student.objects.order_by('class_char','name'))


def admin_homepage(request):
    students_list_document = init_list()
    students_list_assignment = init_list()
    students_list_documentation = init_list()
    students_list_reviewer = init_list()
    students_list_commission  = init_list()

    students_list_document = [student for student in students_list_document if student.handed_document_over == False and student.did_graduate == False]
    students_list_assignment = [student for student in students_list_assignment if student.handed_assignment_over == False and student.did_graduate == False]
    students_list_documentation = [student for student in students_list_documentation if student.assigned_supervisor is None and student.did_graduate == False]
    students_list_reviewer = [student for student in students_list_reviewer if student.assigned_reviewer is None and student.did_graduate == False]
    students_list_commission = [student for student in students_list_commission if not student.students_in_commission.all() and student.did_graduate == False]

    context = {'students_list_document': students_list_document,'students_list_assignment' : students_list_assignment,
               'students_list_documentation': students_list_documentation,'students_list_reviewer': students_list_reviewer,
               'students_list_commission' : students_list_commission}
    return render(request, 'admin_homepage.html', context)

def graduate(request):
    current_students = init_list()
    for student in current_students:
        student.did_graduate = True;
        student.save()
    return HttpResponseRedirect('redirection')

def new_year(request):
    return render(request, 'new_year.html')

# def load_database(request):
#     if request.method == 'POST':
#         directory = get_archive_dir()
#         delete_information()
#         with open(directory + request.POST.get('load'), 'r', newline='') as csvfile:
#             reader = csv.reader(csvfile)
#             for row in reader:
#                 Student(student_name = row[1], student_class = row[2], student_number = row[0], category = row[3], handed_document_over = row[4], handed_assignment_over = row[5],
#                 has_commission = row[6], has_reviewer = row[7]).save()
#             return HttpResponseRedirect('redirection')
#     return (request, 'man_years.html')

def load_database(request):
    return render(request, 'man_years.html')

def saving_database(request):
    if request.method == 'POST':
        # raw_name = request.POST.get('SaveYear')
        # students_list = init_list()
        # directory = get_archive_dir()
        #
        # if not os.path.exists(directory):
        #     os.makedirs(directory)
        #
        # with open(directory + raw_name + '.csv', 'w+', newline='') as csvfile:
        #     writer = csv.writer(csvfile)
        #
        #     for student in students_list:
        #         writer.writerow([student.student_number,student.student_name, student.student_class, student.category, student.handed_document_over,student.handed_assignment_over,
        #         student.has_reviewer, student.has_commission])
        #     return HttpResponseRedirect('redirection')

        return HttpResponseRedirect('redirection')
    return render(request,'man_years.html')

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
        category_ = request.POST.get('Category')
        Student(name = name_ , class_char = class_ , number = number_ , category = category_).save()
        return HttpResponseRedirect('redirection')

    return render(request, 'upload_students.html')

def file_handler(request):
    if request.method == 'POST':
        extension = request.FILES['text_csv'].name.split('.')[1]
        if extension == 'txt':
            my_file = request.FILES['text_csv'].read().decode('cp1251')
            rows = my_file.split('\r\n')
            class_ = None
            category_ = None
            for row in rows:
                if row[:1] == 'X':
                    class_ = row[-1:].upper()
                elif row[:1] == 'S':
                    category_ = 'System Programming'
                elif row[:1] == 'H':
                    category_ = 'Computer Networks'
                else:
                    if len(row) > 1:
                        information = row.split('.')
                        number_ = information[0]
                        student_ = information[1].replace(' ','',1)
                        Student(name=student_, category = category_ , class_char=class_, number = number_,).save()
        return HttpResponseRedirect('redirection')
    return render(request,'upload_students.html')

def upload_students(request):
    return render(request, 'upload_students.html')

def supervisor_handler(request):
    if request.method == 'POST':
        name_ = request.POST.get('FullName')
        category_ = request.POST.get('Category');
        titles_ = request.POST.get('Title')
        workpace_ = request.POST.get('Work')
        ManagmentAndReview(name = name_ , category = category_, titles = titles_ , workplace = work_ , ).save()
        return HttpResponseRedirect('redirection')
    return render(request, 'upload_supervisors.html')

def upload_supervisors(request):
    return render(request, 'upload_supervisors.html')

def upload_thesis(request):
    return render(request, 'upload_thesis.html')

def upload_reviewers(request):
    return render(request, 'upload_reviewers.html')

def reviewer_handler(request):
    if request.method == 'POST':
        name_ = request.POST.get('FullName')
        category_ = request.POST.get('Category')
        titles_ = request.POST.get('Title')
        workplace_ = request.POST.get('Work')
        ManagmentAndReview(name = name_ ,category = category_, titles = titles_ , workplace = workpace_).save()
        return HttpResponseRedirect('redirection')
    return render(request, 'upload_reviewers.html')



def thesis_handler(request):
    if request.method == 'POST':
        description_ = request.POST.get('ThesisDescription')
        category_ = request.POST.get('Category')
        Thesis(name = description_, category = category_).save()
        return HttpResponseRedirect('redirection')

    return render(request, 'upload_thesis.html')

def assign_document(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    context = {'student':student, 'thesis_topics': Thesis.objects.all()}
    return render(request, 'document_assign.html', context)

def prearranged_handler(request):


    return render(request, 'document_assign.html')


def listing(request):
    return HttpResponse("listing")
