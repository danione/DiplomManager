from django.db import models
import datetime


class BasicModel(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 300, default = "none")
    category = models.CharField(max_length = 60, default = "System Programming")

    class Meta:
        abstract = True

class ManagementAndReview(BasicModel):
    titles = models.CharField(max_length = 100)
    workplace = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Thesis(BasicModel):
    supervisor = models.ForeignKey(ManagementAndReview, on_delete=models.CASCADE, null=True)
    place = models.CharField(max_length = 5, default = '1st')

    def get_sorted_by_number_thesis(self):
        return self.choice_set.order_by('number', '-student__progress')

    def __str__(self):
        return self.name

class Student(BasicModel):
    class_char = models.CharField(max_length = 1)
    number = models.IntegerField()
    progress = models.FloatField(default = 0.00)
    handed_document_over = models.BooleanField(default = False)
    handed_assignment_over = models.BooleanField(default = False)
    handed_documentation_over = models.BooleanField(default = False)
    assigned_supervisor = models.ForeignKey(ManagementAndReview, on_delete=models.CASCADE, null=True, related_name = "supervisor")
    current_thesis = models.ForeignKey(Thesis,on_delete=models.CASCADE, null=True)
    assigned_reviewer = models.ForeignKey(ManagementAndReview, on_delete=models.CASCADE, null=True, related_name = "reviewer")
    study_period = models.CharField(max_length = 30,default = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().year + 1))
    did_graduate = models.BooleanField(default = False)
    has_prearranged_thesis = models.BooleanField(default = True)


    def __str__(self):
        return self.name

class Choice(models.Model):
    id = models.AutoField(primary_key = True)
    number = models.IntegerField()
    student = models.ForeignKey(Student, on_delete = models.CASCADE, null = True)
    thesis = models.ForeignKey(Thesis, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return self.student.name + "'s choice"

class Commission(BasicModel):
    chairman = models.ForeignKey(ManagementAndReview, on_delete=models.CASCADE, null = True)
    commissioners = models.ManyToManyField(ManagementAndReview, related_name = "commissioners")
    place = models.CharField(max_length = 50, default = "none")
    time = models.CharField(max_length = 60,default = "none")
    when = models.CharField(max_length = 30, default = "never")
    students = models.ManyToManyField(Student, related_name = "students_in_commission")


    def __str__(self):
        return self.name
