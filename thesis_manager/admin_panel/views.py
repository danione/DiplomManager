from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Student, ManagementAndReview, Thesis, Commission, Choice
from django.shortcuts import get_object_or_404
from operator import itemgetter,attrgetter
import csv
import os


def get_archive_dir():
    return os.getcwd() + '/archives/'

def init_list():
    return list(Student.objects.order_by('class_char','name'))


def admin_homepage(request):
    students_list_thesis = init_list()
    students_list_document = init_list()
    students_list_assignment = init_list()
    students_list_documentation = init_list()
    students_list_reviewer = init_list()
    students_list_commission  = init_list()

    students_list_document = [student for student in students_list_document
                              if student.handed_document_over == False and student.did_graduate == False]
    students_list_thesis = [student for student in students_list_thesis
                            if student.has_prearranged_thesis == False and student.current_thesis is None]
    students_list_assignment = [student for student in students_list_assignment
                                if student.handed_assignment_over == False and student.did_graduate == False]
    students_list_documentation = [student for student in students_list_documentation
                                   if student.handed_documentation_over == False and student.did_graduate == False]
    students_list_reviewer = [student for student in students_list_reviewer
                              if student.assigned_reviewer is None and student.did_graduate == False]
    students_list_commission = [student for student in students_list_commission
                                if not student.commission  and student.did_graduate == False]

    context = {'students_list_document': students_list_document,'students_list_thesis' : students_list_thesis,
               'students_list_assignment' : students_list_assignment,'students_list_documentation': students_list_documentation,
               'students_list_reviewer': students_list_reviewer,'students_list_commission' : students_list_commission}
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
        category_ = request.POST.get('Category')
        titles_ = request.POST.get('Title')
        workplace_ = request.POST.get('Work')
        ManagementAndReview(name = name_ , category = category_, titles = titles_ , workplace = workplace_).save()
        return HttpResponseRedirect('redirection')
    return render(request, 'upload_supervisors.html')

def upload_supervisors(request):
    return render(request, 'upload_supervisors.html')

def upload_reviewers(request):
    return render(request, 'upload_reviewers.html')

def reviewer_handler(request):
    if request.method == 'POST':
        name_ = request.POST.get('FullName')
        category_ = request.POST.get('Category')
        titles_ = request.POST.get('Title')
        workplace_ = request.POST.get('Work')
        ManagementAndReview(name = name_ ,category = category_, titles = titles_ , workplace = workpace_).save()
        return HttpResponseRedirect('redirection')
    return render(request, 'upload_reviewers.html')

def upload_thesis(request):
    supervisors = ManagementAndReview.objects.all()
    thesis_topics = Thesis.objects.all()
    context = {'supervisors': supervisors, 'thesis_topics': thesis_topics}
    return render(request, 'upload_thesis.html', context)


def thesis_handler(request):
    if request.method == 'POST':
        description_ = request.POST.get('ThesisDescription')
        category_ = request.POST.get('Category')
        supervisor_ = request.POST.get('Supervisor')
        Thesis(name = description_, category = category_, supervisor = ManagementAndReview.objects.get(name = supervisor_)).save()
        return HttpResponseRedirect('redirection')

    return render(request, 'upload_thesis.html')

def assign_document(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    context = {'student':student, 'thesis_topics': Thesis.objects.all()}
    request.session['student_id'] = student_id
    return render(request, 'document_assign.html', context)

def prearranged_handler(request):
    if request.method == 'POST':
        student_id = request.session['student_id']
        student = Student.objects.get(id = student_id)
        thesis = Thesis.objects.get(name = request.POST.get('Thesis'))

        student.current_thesis = thesis
        student.has_prearranged_thesis = True
        student.handed_document_over = True
        student.assigned_supervisor = thesis.supervisor
        student.save()

        return HttpResponseRedirect('redirection')
    return render(request, 'document_assign.html')

def standard_handler(request):
    if request.method == 'POST':
        choices = []
        choices.append(Thesis.objects.get(name = request.POST.get('Thesis1')))
        choices.append(Thesis.objects.get(name = request.POST.get('Thesis2')))
        choices.append(Thesis.objects.get(name = request.POST.get('Thesis3')))
        student_id = request.session['student_id']
        student = Student.objects.get(id = student_id)
        student.handed_document_over = True
        student.has_prearranged_thesis = False


        progress = request.POST.get('Progress')
        student.progress = float(progress)
        student.save()

        for index,choice in enumerate(choices):
            Choice(number = index + 1, student = student, thesis = choice).save()

        return HttpResponseRedirect('redirection')
    return render(request,'document_assign.html')

def standard_thesis(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    choices = student.choice_set.all()
    thesis = []
    students = []
    students_output = {}

    for index,choice in enumerate(choices):
        sorted_choices = choice.thesis.get_sorted_by_number_thesis()
        for sorted_choice in sorted_choices:
            if sorted_choice.student:
                students.append(sorted_choice.student)
        students_output[index] = students
        students = []
        thesis.append(choice.thesis)
        sorted_choice = []


    context = {'student':student, 'thesis' : thesis, 'students_output' : students_output}
    request.session['student_id'] = student_id
    return render(request, 'assignment_assign.html', context)

def finilize(request, thesis_id):
    student_id = request.session['student_id']
    student = Student.objects.get(id = student_id)
    thesis = Thesis.objects.get(id = thesis_id)

    student.choice_set.clear()
    student.current_thesis = thesis
    student.assigned_supervisor = thesis.supervisor
    student.save()

    return HttpResponseRedirect('redirection')

def handed_assignment_over(request, student_id):
    student = Student.objects.get(id = student_id)
    student.handed_assignment_over = True
    student.save()

    return HttpResponseRedirect('redirection')

def handed_documentation_over(request, student_id):
    student = Student.objects.get(id = student_id)
    student.handed_documentation_over = True
    student.save()

    return HttpResponseRedirect('redirection')

def reviewer_assign(request, student_id):
    reviewers = ManagementAndReview.objects.all()
    request.session['student_id'] = student_id
    student = Student.objects.get(id = student_id)

    context = {'reviewers': reviewers,'student': student}
    return render(request, 'reviewer_assign.html', context)

def reviewer_connect(request):
    if request.method == 'POST':
        reviewer = request.POST.get('Reviewer')
        student_id = request.session['student_id']
        student = Student.objects.get(id = student_id)
        student.assigned_reviewer = ManagementAndReview.objects.get(name = reviewer)
        student.save()

    return HttpResponseRedirect('redirection')

def commission_assign(request, student_id):
    student = Student.objects.get(id = student_id)
    people_in_system = ManagementAndReview.objects.all()
    commissions = Commission.objects.filter(category = student.current_thesis.category)
    request.session['student_id'] = student_id

    context = {'student': student, 'members': people_in_system, 'commissions': commissions}
    return render(request, 'commission_assign.html', context)

def new_commission_handler(request):
    chairman_ = ManagementAndReview.objects.get(id = int(request.POST.get('ChairmanId')))
    members = []
    student_id = request.session['student_id']
    student = Student.objects.get(id = student_id)
    members.append(ManagementAndReview.objects.get(id = int(request.POST.get('Member1Id'))))
    members.append(ManagementAndReview.objects.get(id = int(request.POST.get('Member2Id'))))
    members.append(ManagementAndReview.objects.get(id = int(request.POST.get('Member3Id'))))
    place_ = request.POST.get('Place')
    date_ = request.POST.get('ManualDate')
    time_ = request.POST.get('morning/afternoon')

    category_ = student.current_thesis.category
    commission = Commission(name = category_ +
                            " " + date_ +
                            " " + time_ +
                            " " + place_,
                            category = category_,
                            chairman = chairman_,
                            place = place_,
                            date = date_,
                            time = time_)
    commission.save()
    for member in members:
        commission.commissioners.add(member)
    student.commission = commission
    student.save()
    commission.save()

    return HttpResponseRedirect('redirection')

def existing_commission_handler(request):
    student_id = request.session['student_id']
    student = Student.objects.get(id = student_id)
    commission = Commission.objects.get(id = int(request.POST.get('load')))

    student.commission = commission
    student.save()
    commission.save()

    return HttpResponseRedirect('redirection')

def listing(request):
    students = init_list()
    man_review = ManagementAndReview.objects.order_by('name')
    thesis_topics = Thesis.objects.order_by('name')
    commissions = Commission.objects.order_by('place')

    context = {'students': students,'man_review' : man_review, 'thesis_topics': thesis_topics, 'commissions' : commissions}
    return render(request, 'listing.html', context)


def update_student(request, student_id):
    student = Student.objects.get(id = student_id)
    student.number = request.POST.get('Number')
    student.name = request.POST.get('Name')
    student.class_char = request.POST.get('Class')
    student.progress = request.POST.get('Progress')
    student.category = request.POST.get('Category')
    if request.POST.get('thesis-remove') == 'true':
        student.current_thesis = None
    if request.POST.get('reviewer-remove') == 'true':
        student.assigned_reviewer = None
    student.save()

    return HttpResponseRedirect('update_student/redirection')

def update_man_review(request, man_rev_id):
    man_rev = ManagementAndReview.objects.get(id = man_rev_id)
    man_rev.titles = request.POST.get('Title')
    man_rev.name = request.POST.get('FullName')
    man_rev.category = request.POST.get('Category')
    man_rev.workplace = request.POST.get('Work')
    for student in man_rev.reviewer.all():
        if request.POST.get(str(student.id) + '-remove') == 'true':
            man_rev.reviewer.remove(student)

    man_rev.save()

    return HttpResponseRedirect('update_man_review/redirection')


def update_thesis(request, thesis_id):
    thesis = Thesis.objects.get(id = thesis_id)
    thesis.name = request.POST.get('ThesisDescription')
    thesis.category = request.POST.get('Category')
    thesis.save()

    return HttpResponseRedirect('update_thesis/redirection')

def update_commission(request, commission_id):
    commission = Commission.objects.get(id = commission_id)
    commission.place = request.POST.get('Place')
    commission.date = request.POST.get('Date')
    commission.time = request.POST.get(str(commission.id) + '-morning/afternoon')

    for student in commission.commission.all():
        if request.POST.get(str(student.id) + '-remove') == 'true':
            commission.commission.remove(student)


    commission.save()

    return HttpResponseRedirect('update_commission/redirection')
