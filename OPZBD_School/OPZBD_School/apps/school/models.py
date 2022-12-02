from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    surname = models.CharField(max_length=255, verbose_name="Фамилия")
    lastname = models.CharField(max_length=255, verbose_name="Отчество")

    def __str__(self):
        return f"{self.name} {self.surname} {self.lastname}"

class Student(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    surname = models.CharField(max_length=255, verbose_name="Фамилия")
    lastname = models.CharField(max_length=255, verbose_name="Отчество")

    def __str__(self):
        return f"{self.name} {self.surname} {self.lastname}"


class ClassName(models.Model):
    name = models.CharField(max_length=3, verbose_name="Названия учебного класса", unique=True)


    def __str__(self):
        return self.name


class ClassRoom(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ManyToManyField(Student, related_name="prev", blank=True)
    classname = models.ForeignKey(ClassName, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.teacher} {self.student} {self.classname}"
