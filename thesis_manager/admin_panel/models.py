from django.db import models
import datetime


class BasicModel(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 300, default = "none")
    category = models.CharField(max_length = 60, default = "System Programming")

    class Meta:
        abstract = True

class ManagmentAndReview(BasicModel):
    titles = models.CharField(max_length = 100)
    workplace = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Thesis(BasicModel):
    supervisor = models.ForeignKey(ManagmentAndReview, on_delete=models.CASCADE, null=True)
    is_prearranged = models.BooleanField(default = True)

    def __str__(self):
        return self.name

class Student(BasicModel):
    class_char = models.CharField(max_length = 1)
    number = models.IntegerField()
    handed_document_over = models.BooleanField(default = False)
    handed_assignment_over = models.BooleanField(default = False)
    handed_documentation_over = models.BooleanField(default = False)
    assigned_supervisor = models.ForeignKey(ManagmentAndReview, on_delete=models.CASCADE, null=True, related_name = "supervisor")
    assigned_thesis = models.ManyToManyField(Thesis, related_name = "thesis_topic")
    assigned_reviewer = models.ForeignKey(ManagmentAndReview, on_delete=models.CASCADE, null=True, related_name = "reviewer")
    study_period = models.CharField(max_length = 30,default = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().year + 1))
    did_graduate = models.BooleanField(default = False)

    def __str__(self):
        return self.name

class Commission(BasicModel):
    chairman = models.ForeignKey(ManagmentAndReview, on_delete=models.CASCADE, null = True)
    commissioners = models.ManyToManyField(ManagmentAndReview, related_name = "commissioners")
    place = models.CharField(max_length = 30, default = "none")
    time = models.DateTimeField(null = True)
    students = models.ManyToManyField(Student, related_name = "students_in_commission")

    def __str__(self):
        return self.name
