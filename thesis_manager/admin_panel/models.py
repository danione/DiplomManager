from django.db import models

class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    teacher_name = models.CharField(max_length=200)
    titles = models.CharField(max_length=200)
    place_of_work = models.CharField(max_length=200)
    system_programming = models.BooleanField(default=False)

    def __str__(self):
        return self.teacher_name

class Thesis(models.Model):
    id = models.AutoField(primary_key=True)
    thesis_description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    software = models.BooleanField(default=True)
    hardware = models.BooleanField(default=False)
    
    def __str__(self):
        return self.thesis_description

class Reviewer(models.Model):
    id = models.AutoField(primary_key=True)
    reviewer_name = models.CharField(max_length=200)
    reviewer_titles = models.CharField(max_length=200)
    place_of_work = models.CharField(max_length=200)


    def __str__(self):
        return self.reviewer_name

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=200)
    student_class = models.CharField(max_length=1)
    student_number = models.IntegerField()
    system_programming = models.BooleanField(default=True)
    has_document = models.BooleanField(default=False)
    has_assignment = models.BooleanField(default=False)
    has_commission = models.BooleanField(default=False)
    has_reviewer = models.BooleanField(default=False)
    assigned_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    assigned_thesis = models.ForeignKey(Thesis, on_delete=models.CASCADE, null=True)
    assigned_reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.student_name
