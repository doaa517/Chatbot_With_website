from django.db import models
from django.contrib.auth.models import AbstractUser

# from university.models import Faculty

class User(AbstractUser):
    MALE, FEMALE = "m", "f"
    GENDER_OPTIONS = (
        (MALE, "Male"),
        (FEMALE, "Female"),
    )

    father_name = models.CharField("Father Name", max_length=50, null=True, blank=True)
    phone = models.CharField("Phone Number", max_length=15, null=True)
    gender = models.CharField(
        "Gender", choices=GENDER_OPTIONS, max_length=10, default=MALE
    )
    email = models.EmailField ("Email", null=False, blank=False)
    address = models.CharField("Address", max_length=100, null=True, blank=True)
    nationality = models.CharField("Nationality", max_length=100, null=True, blank=True)
    birth_date = models.DateField("Birth Date", null=True, blank=True)

    bank_name = models.CharField("Bank Name", null=True, blank=True, max_length=50)
    bank_card_num = models.CharField(
        "bank Card Number", null=True, blank=True, max_length=50
    )
    profile_image = models.ImageField(
        "Profile Image", upload_to="profile_images", null=True, blank=True,
    )

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Student(models.Model):
    id = models.IntegerField("Student ID", primary_key=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, related_name="student_user"
    )
    # faculty = models.ForeignKey(Faculty, verbose_name="Faculty", null=True, blank=False, on_delete=models.SET_NULL)
    
    def __str__(self) -> str:
        if self.user.first_name and self.user.last_name:
            return self.user.first_name + " " + self.user.last_name
        else:
            return str(self.user)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"


class Lecturer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, related_name="lecturer_user"
    )

    certificate = models.CharField("Certificate", max_length=50, null=True, blank=True)
    certificate_date = models.DateField("Certificate Date", null=True, blank=True)
    
    def __str__(self) -> str:
        if self.user.first_name and self.user.last_name:
            return self.user.first_name + " " + self.user.last_name
        else:
            return str(self.user)

    class Meta:
        verbose_name = "Lecturer"
        verbose_name_plural = "Lecturers"
