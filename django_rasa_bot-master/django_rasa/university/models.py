from django.db import models
from django.core.exceptions import ValidationError

from user.models import Lecturer, Student

class University(models.Model):
    name = models.CharField("University Name", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "University"
        verbose_name_plural = "Universities"


class Branche(models.Model):
    name = models.CharField("Branche", max_length=50)
    address = models.CharField("Address", max_length=150)
    university = models.ForeignKey(
        University, verbose_name="university", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Branche"
        verbose_name_plural = "Branches"
        

class Faculty(models.Model):
    name = models.CharField("Faculty Name", max_length=50)
    open_date = models.DateField("Open Date", null=True, blank=True)
    branche = models.ForeignKey(
        Branche, verbose_name="branche", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Faculty"
        verbose_name_plural = "Faculties"


class Course(models.Model):

    title = models.CharField("Course Title", max_length=50, null=False, blank=False)
    num = models.CharField("Course Number", max_length=50, unique=True, null=False, blank=False)
    total_hours = models.IntegerField("Total Course Hours", null=False, blank=False)
    faculties = models.ManyToManyField(Faculty, related_name="faculty")
    # prev_course = models.ForeignKey(
    #     "self",
    #     verbose_name="Previous Course",
    #     related_name="previous_course",
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True,
    # )


    def __str__(self):
        return self.num


    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"


class PreCourse(models.Model):

    course = models.ForeignKey(Course, verbose_name="Course",on_delete=models.SET_NULL, 
        null=True, blank=True,related_name="course"
    )


    prev_course = models.ForeignKey(Course, verbose_name= "Previous Course",
        related_name="previous_course",
        on_delete=models.SET_NULL,
        null=True,
        blank=True 
    )


    def __str__(self):
        return f"Course: {self.course}"
    
    class Meta:
        verbose_name = "Previous Course"
        verbose_name_plural = "Previous Courses"
    


class Class(models.Model):

    MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY = "  Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"
    DAYS_OF_WEEK = (
        (MONDAY, "Monday"), (TUESDAY, "Tuesday"),
        (WEDNESDAY, "Wednesday"),(THURSDAY, "Thursday"),(FRIDAY, "Friday"),
        (SATURDAY, "Saturday"),(SUNDAY, "Sunday")
    )

    claas_day = models.CharField("Class Day", choices=DAYS_OF_WEEK, max_length=10, default=SUNDAY)
    title = models.CharField("Class Title", max_length=50)
    start_time = models.TimeField("Class start time",auto_now=False, auto_now_add=False, null=True, blank=True)
    end_time = models.TimeField("Class end time",auto_now=False, auto_now_add=False, null=True, blank=True)
    branche = models.ForeignKey(
        Branche, verbose_name="branche", on_delete=models.SET_NULL, null=True
    )
    course = models.ForeignKey(
        Course, verbose_name="course", on_delete=models.SET_NULL, null=True
    )
    lecturer = models.ForeignKey(
        Lecturer, verbose_name="lecturer", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"

def validate_degree(value):
    if value < 0 or value > 100:
        raise ValidationError(
           "Degree must be in 0 - 100 range",
        )
        
        
class StudentDegree(models.Model):
    student = models.ForeignKey(Student, verbose_name="Student", on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, verbose_name="Faculty", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name="Course", on_delete=models.CASCADE)
    degree = models.IntegerField("Degree", validators=[validate_degree])
    
    def __str__(self):
        return f"Student: {self.student} - Course: {self.course} - Degree: {self.degree}"
    
    class Meta:
        verbose_name = "Student Degree"
        verbose_name_plural = "Students Degrees"
    