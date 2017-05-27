from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Student, ManagementAndReview, Thesis, Commission, Choice, Period
from django.shortcuts import get_object_or_404
import csv
from django.contrib.auth import logout


def init_list():
    return list(Student.objects.order_by('class_char','name'))

def get_current_period():
    if Period.objects.filter(is_current_period = 'True'):
        return Period.objects.get(is_current_period = 'True')
    else:
        return None

def log_out(request):
    logout(request)
    return HttpResponseRedirect('redirection')

def admin_homepage(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('redirection')

    students_list_thesis = init_list()
    students_list_document = init_list()
    students_list_assignment = init_list()
    students_list_documentation = init_list()
    students_list_reviewer = init_list()
    students_list_commission  = init_list()

    period = get_current_period()

    students_list_document = [student for student in students_list_document
                              if student.handed_document_over == False
                              and (student.did_graduate == False
                                   or student.study_period == period.period)]

    students_list_thesis = [student for student in students_list_thesis
                            if student.has_prearranged_thesis == False
                            and student.current_thesis is None
                            and (student.did_graduate == False or student.study_period == period.period)]

    students_list_assignment = [student for student in students_list_assignment
                                if student.handed_assignment_over == False and (student.did_graduate == False or student.study_period == period.period)]
    students_list_documentation = [student for student in students_list_documentation
                                   if student.handed_documentation_over == False and (student.did_graduate == False or student.study_period == period.period)]
    students_list_reviewer = [student for student in students_list_reviewer
                              if student.assigned_reviewer is None and (student.did_graduate == False or student.study_period == period.period)]
    students_list_commission = [student for student in students_list_commission
                                if not student.commission  and (student.did_graduate == False or student.study_period == period.period)]

    context = {'students_list_document': students_list_document,'students_list_thesis' : students_list_thesis,
               'students_list_assignment' : students_list_assignment,'students_list_documentation': students_list_documentation,
               'students_list_reviewer': students_list_reviewer,'students_list_commission' : students_list_commission}
    return render(request, 'admin_homepage.html', context)

def graduate(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('redirection')
    current_students = init_list()
    for student in current_students:
        student.did_graduate = True;
        student.save()
    if Period.objects.filter(is_current_period = True):
        period = Period.objects.get(is_current_period = True)
        period.is_current_period = False
        period.save()

    current_period = Period(period = request.POST.get('Period'), is_current_period = True)
    current_period.save()

    return HttpResponseRedirect('redirection')

def new_year(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('redirection')
    return render(request, 'new_year.html')


def man_years(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('redirection')
    periods = Period.objects.filter(is_current_period = 'False').order_by('period')
    current_period = get_current_period()
    context = {'periods': periods, 'current_period': current_period}
    return render(request, 'man_years.html', context)

def period_change(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('redirection')
    new_period = Period.objects.get(id = int(request.POST.get('load')))
    current_period = get_current_period()

    current_period.is_current_period = False
    current_period.save()

    new_period.is_current_period = True
    new_period.save()

    return HttpResponseRedirect('redirection')


def upload_students(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('redirection')
    period = get_current_period()
    if period == None:
        return HttpResponseNotFound('<h1>You did not select period</h1>')
    return render(request, 'upload_students.html')

def student_handler(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('redirection')
    name_ = request.POST.get('FullName')
    class_ = request.POST.get('Class')
    number_ = request.POST.get('Number')
    category_ = request.POST.get('Category')
    period_ = get_current_period()

    Student(name = name_ ,
            class_char = class_ ,
            number = number_ ,
            category = category_,
            study_period = period_.period).save()
    return HttpResponseRedirect('redirection')


def is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

def is_proper_length_and_type(length, string):
    if len(string) > length:
        return False
    else:
        if all(letter.isalpha() or letter.isspace() for letter in string):
            return True
        else:
            return False

def is_only_char(char):
    if len(char) == 1 and char.isalpha():
        return True
    else:
        return False

def file_handler(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('redirection')
    extension = request.FILES['text_csv'].name.split('.')[1]
    if extension == 'csv':
        my_file = request.FILES['text_csv'].read().decode('utf-8')
        rows = my_file.split('\n')
        for row in rows:
            if len(row) <= 1:
                break
            data = row.split(',')
            if is_int(data[0]) == False:
                return HttpResponseNotFound('<h1>Data in first field is not in proper type</h1><p>' + data[0] + '</p>')
            if is_proper_length_and_type(300, data[1]) == False:
                return HttpResponseNotFound('<h1>Data in second field is not in proper type or is longer</h1><p>' + data[1] + '</p>')
            if is_only_char(data[2]) == False:
                return HttpResponseNotFound('<h1>Data in third field is not in proper type or it is not a character</h1><p>' + data[2] + '</p>')
            if is_proper_length_and_type(60, data[3]) == False:
                return HttpResponseNotFound('<h1>Data in fourth field is not in proper type or is longer</h1><p>' + data[3] + '</p>')


            period_ = get_current_period()
            if data[0] and data[1] and data[2] and data[3]:
                Student(number = int(data[0]), name = data[1], class_char = data[2], category = data[3] , study_period = period_.period ).save()
    return HttpResponseRedirect('redirection')


def supervisor_handler(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('redirection')
    name_ = request.POST.get('FullName')
    category_ = request.POST.get('Category')
    titles_ = request.POST.get('Title')
    workplace_ = request.POST.get('Work')
    ManagementAndReview(name = name_ , category = category_, titles = titles_ , workplace = workplace_).save()
    return HttpResponseRedirect('redirection')

def is_proper_length_type_and_symbols(length,string):
    if len(string) >= length:
        return False
    else:
        if all(letter.isalpha() or letter.isspace() or letter == '.' for letter in string):
            return True
        else:
            return False


def supervisor_file_handler(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('redirection')
    extension = request.FILES['text_csv'].name.split('.')[1]
    if extension == 'csv':
        my_file = request.FILES['text_csv'].read().decode('utf-8')
        rows = my_file.split('\n')
        for row in rows:
            if len(row) <= 1:
                break
            data = row.split(',')

            if is_proper_length_type_and_symbols(100,data[0]) == False:
                return HttpResponseNotFound('<h1>Data in first field is not in proper type,length or having forbidden symbols</h1><p>' + data[0] + '</p>')
            if is_proper_length_and_type(300, data[1]) == False:
                return HttpResponseNotFound('<h1>Data in second field is not in proper type or is longer</h1><p>' + data[1] + '</p>')
            if is_proper_length_and_type(60, data[2]) == False:
                return HttpResponseNotFound('<h1>Data in third field is not in proper type or length</h1><p>' + data[2] + '</p>')
            if is_proper_length_and_type(200, data[3]) == False:
                return HttpResponseNotFound('<h1>Data in fourth field is not in proper type or length</h1><p>' + data[3] + '</p>')


            if data[0] and data[1] and data[2] and data[3]:
                ManagementAndReview(titles = data[0], name = data[1], category = data[2] , workplace = data[3]).save()

    return HttpResponseRedirect('redirection')


def upload_supervisors(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('redirection')
    period = get_current_period()
    if period == None:
        return HttpResponseNotFound('<h1>You did not select period</h1>')
    return render(request, 'upload_supervisors.html')

def upload_thesis(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('redirection')
    supervisors = ManagementAndReview.objects.all()
    period = get_current_period()
    if period == None:
        return HttpResponseNotFound('<h1>You did not select period</h1>')
    thesis_topics = Thesis.objects.filter(period_given = period.period)
    context = {'supervisors': supervisors, 'thesis_topics': thesis_topics}
    return render(request, 'upload_thesis.html', context)


def thesis_handler(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('redirection')
    description_ = request.POST.get('ThesisDescription')
    category_ = request.POST.get('Category')
    supervisor_ = request.POST.get('Supervisor')

    period = get_current_period()

    Thesis(name = description_, category = category_, supervisor = ManagementAndReview.objects.get(name = supervisor_), period_given = period.period ).save()
    return HttpResponseRedirect('redirection')

def thesis_file_handler(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('redirection')
    extension = request.FILES['text_csv'].name.split('.')[1]
    if extension == 'csv':
        my_file = request.FILES['text_csv'].read().decode('utf-8')
        rows = my_file.split('\n')
        for row in rows:
            if len(row) <= 1:
                break
            data = row.split(',')

            if is_proper_length_and_type(300, data[0]) == False:
                return HttpResponseNotFound('<h1>Data in first field is longer or is not in proper type</h1><p>' + data[0] + '</p>')
            if is_proper_length_and_type(60, data[1]) == False:
                return HttpResponseNotFound('<h1>Data in second field is not in proper type or is longer</h1><p>' + data[1] + '</p>')
            if is_proper_length_type_and_symbols(100, data[2]) == False:
                return HttpResponseNotFound('<h1>Data in third field is not in proper type or it is containing forbidden symbols or it is too long</h1><p>' + data[2] + '</p>')
            if is_proper_length_and_type(300, data[3]) == False:
                return HttpResponseNotFound('<h1>Data in third field is not in proper type or longer</h1><p>' + data[3] + '</p>')
            if is_proper_length_and_type(60, data[4]) == False:
                return HttpResponseNotFound('<h1>Data in fourth field is not in proper type or is longer</h1><p>' + data[4] + '</p>')


            if data[0] and data[1] and data[2] and data[3]:
                if ManagementAndReview.objects.filter(titles = data[2], name = data[3], workplace = data[4]):
                    period = get_current_period()
                    Thesis(name = data[0], category = data[1], supervisor = ManagementAndReview.objects.get(titles = data[2], name = data[3], workplace = data[4]), period_given = period.period).save()
                else:
                    return HttpResponseNotFound('<h1>Supervisor does not exist</h1><p>' + data[2] + data[3] + data[4] + '</p>')

    return HttpResponseRedirect('redirection')


def assign_document(request, student_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('redirection')
    student = get_object_or_404(Student, pk=student_id)

    period = get_current_period()
    context = {'student':student, 'thesis_topics': Thesis.objects.filter(period_given = period.period)}
    request.session['student_id'] = student_id
    return render(request, 'document_assign.html', context)

def prearranged_handler(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponseRedirect('redirection')
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
        if not request.user.is_authenticated:
            return HttpResponseRedirect('redirection')
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
    if not request.user.is_authenticated:
        return HttpResponseRedirect('redirection')
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
    if not request.user.is_authenticated:
        return HttpResponseRedirect('redirection')
    student_id = request.session['student_id']
    student = Student.objects.get(id = student_id)
    thesis = Thesis.objects.get(id = thesis_id)

    student.choice_set.clear()
    student.current_thesis = thesis
    student.assigned_supervisor = thesis.supervisor
    student.save()

    return HttpResponseRedirect('redirection')

def handed_assignment_over(request, student_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('redirection')
    student = Student.objects.get(id = student_id)
    student.handed_assignment_over = True
    student.save()

    return HttpResponseRedirect('redirection')

def handed_documentation_over(request, student_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('redirection')
    student = Student.objects.get(id = student_id)
    student.handed_documentation_over = True
    student.save()

    return HttpResponseRedirect('redirection')

def reviewer_assign(request, student_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('redirection')
    reviewers = ManagementAndReview.objects.all()
    request.session['student_id'] = student_id
    student = Student.objects.get(id = student_id)

    context = {'reviewers': reviewers,'student': student}
    return render(request, 'reviewer_assign.html', context)

def reviewer_connect(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('redirection')
    reviewer = request.POST.get('Reviewer')
    student_id = request.session['student_id']
    student = Student.objects.get(id = student_id)
    student.assigned_reviewer = ManagementAndReview.objects.get(name = reviewer)
    student.save()

    return HttpResponseRedirect('redirection')

def commission_assign(request, student_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('redirection')
    period = get_current_period()
    student = Student.objects.get(id = student_id)
    people_in_system = ManagementAndReview.objects.all()
    if student.current_thesis is None:
        return HttpResponseNotFound('<h1>No assignment</h1>')


    commissions = Commission.objects.filter(category = student.current_thesis.category, period_happened = period.period)
    request.session['student_id'] = student_id

    context = {'student': student, 'members': people_in_system, 'commissions': commissions}
    return render(request, 'commission_assign.html', context)

def new_commission_handler(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('redirection')
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

    period = get_current_period()
    category_ = student.current_thesis.category
    commission = Commission(name = category_ +
                            " " + date_ +
                            " " + time_ +
                            " " + place_,
                            category = category_,
                            chairman = chairman_,
                            place = place_,
                            date = date_,
                            time = time_,
                            period_happened = period.period)
    commission.save()
    for member in members:
        commission.commissioners.add(member)
    student.commission = commission
    student.save()
    commission.save()

    return HttpResponseRedirect('redirection')

def existing_commission_handler(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('redirection')
    student_id = request.session['student_id']
    student = Student.objects.get(id = student_id)
    commission = Commission.objects.get(id = int(request.POST.get('load')))

    student.commission = commission
    student.save()
    commission.save()

    return HttpResponseRedirect('redirection')

def listing(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('redirection')
    period = get_current_period()
    if period == None:
        return HttpResponseNotFound('<h1>You did not select period</h1>')

    students = Student.objects.filter(study_period = period.period).order_by('class_char','name')
    man_review = ManagementAndReview.objects.order_by('name')
    thesis_topics = Thesis.objects.filter(period_given = period.period).order_by('name')
    commissions = Commission.objects.filter(period_happened = period.period).order_by('place')

    context = {'students': students,'man_review' : man_review, 'thesis_topics': thesis_topics, 'commissions' : commissions}
    return render(request, 'listing.html', context)


def update_student(request, student_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('redirection')
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
    if not request.user.is_authenticated:
        return HttpResponseRedirect('redirection')
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
    if not request.user.is_authenticated:
        return HttpResponseRedirect('redirection')
    thesis = Thesis.objects.get(id = thesis_id)
    thesis.name = request.POST.get('ThesisDescription')
    thesis.category = request.POST.get('Category')
    thesis.save()

    return HttpResponseRedirect('update_thesis/redirection')

def update_commission(request, commission_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('redirection')
    commission = Commission.objects.get(id = commission_id)
    commission.place = request.POST.get('Place')
    commission.date = request.POST.get('Date')
    commission.time = request.POST.get(str(commission.id) + '-morning/afternoon')

    for student in commission.commission.all():
        if request.POST.get(str(student.id) + '-remove') == 'true':
            commission.commission.remove(student)


    commission.save()

    return HttpResponseRedirect('update_commission/redirection')
