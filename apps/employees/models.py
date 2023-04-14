from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
import hrm_app.settings as sett

from apps.corecode.models import PermitDocCategory, Citizenship


class Employee(models.Model):
    STATUS_CHOICES = [("active", "is working(active)"), ("inactive", "fired(inactive)")]

    GENDER_CHOICES = [("male", "Male"), ("female", "Female")]

    #STAFF_CHOICES = [("WhiteCollar", "Белый воротник"), ("BlueCollar", "Синий воротник")]

    current_status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="active"
    )
    personnel_number = models.CharField(max_length=200, unique=True, )
    surname = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    other_name = models.CharField(max_length=200, blank=True )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="male",)
    date_of_birth = models.DateField(default=timezone.now, )
    position = models.CharField(max_length=200)
    """ current_class = models.ForeignKey(
        StudentClass, on_delete=models.SET_NULL, blank=True, null=True
    ) """
    citizenship = models.ForeignKey(
        Citizenship, on_delete=models.SET_NULL, blank=True, null=True, 
    )

    current_doc_category = models.ForeignKey(
        PermitDocCategory, on_delete=models.SET_NULL, blank=True, null=True, 
    )
    date_of_employment = models.DateField(default=timezone.now, )

    date_of_dismissal = models.DateField()

    tin_number = models.CharField(max_length=200, blank=True)

    snils_number = models.CharField(max_length=200, blank=True)

    mobile_num_regex = RegexValidator(
        regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!"
    )
    mobile_number = models.CharField(
        validators=[mobile_num_regex], max_length=13, blank=True
    )

    address = models.TextField(blank=True, )
    others = models.TextField(blank=True, )
    photo = models.ImageField(blank=True, upload_to="employees/photos/", )

    class Meta:
        ordering = ["personnel_number", "surname", "firstname", "other_name"]

    def __str__(self):
        #return f"{self.surname} {self.firstname} {self.other_name} ({self.registration_number})"
        return "{} {} {} ({})".format(self.surname, self.firstname, self.other_name, self.personnel_number)

    def get_absolute_url(self):
        return reverse("employee-detail", kwargs={"pk": self.pk})


class EmployeeBulkUpload(models.Model):
    date_uploaded = models.DateTimeField(auto_now=True)
    csv_file = models.FileField(upload_to="employees/bulkupload/")
