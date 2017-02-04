from django.db import models

class ManagmentAndReview(models.Model):
    personal_id = models.AutoField(primary_key=True)
    personal_name = models.CharField(max_length=200)
    titles = models.CharField(max_length=200)
    place_of_work = models.CharField(max_length=200)
    category = models.CharField(max_length=60)

    def __str__(self):
        return self.personal_name

class Thesis(models.Model):
    thesis_id = models.AutoField(primary_key=True)
    thesis_description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=60)
    def __str__(self):
        return self.thesis_description

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=200)
    student_class = models.CharField(max_length=1)
    student_number = models.IntegerField()
    class_type = models.CharField(max_length=200)
    handed_document_over = models.BooleanField(default=False)
    handed_assignment_over = models.BooleanField(default=False)
    has_commission = models.BooleanField(default=False)
    has_reviewer = models.BooleanField(default=False)
    assigned_teacher = models.ForeignKey(ManagmentAndReview, on_delete=models.CASCADE, null=True)
    assigned_thesis = models.ForeignKey(Thesis, on_delete=models.CASCADE, null=True)
    assigned_reviewer = models.ForeignKey(ManagmentAndReview, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.student_name
