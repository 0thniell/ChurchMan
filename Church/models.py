from django.db import models

# Create your models here.
class Members(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)
    sex = models.CharField(max_length=64)
    dob = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    office_address = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    marital_status = models.CharField(max_length=64)
    spouse_name = models.CharField(max_length=64)
    number_of_children = models.CharField(max_length=64)
    occupation = models.CharField(max_length=64)
    date_joined_church = models.CharField(max_length=64)
    membership_status = models.CharField(max_length=64)
    date_of_conversion = models.CharField(max_length=64)
    baptism_date = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'

class Church_Service(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    date = models.CharField(max_length=64)
    opening_time = models.CharField(max_length=64)
    nature_of_service = models.CharField(max_length=64)
    topic_of_sermon = models.CharField(max_length=64)
    scripture_reading = models.CharField(max_length=64)
    preacher = models.CharField(max_length=64)
    closing_time = models.CharField(max_length=64)
    men_attendance = models.CharField(max_length=64)
    women_attendance = models.CharField(max_length=64)
    tithes = models.CharField(max_length=64)
    offering = models.CharField(max_length=64)
    seed_offering = models.CharField(max_length=64)
    building_offering = models.CharField(max_length=64)
    welfare_offering = models.CharField(max_length=64)
    thanksgiving_offering = models.CharField(max_length=64)
    other_offerings = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'

class Church_Event_Register(models.Model):
    id = models.AutoField(primary_key=True)
    event_title = models.CharField(max_length=64)
    event_description = models.CharField(max_length=64)
    event_date = models.CharField(max_length=64)
    event_time = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    targeted_group = models.CharField(max_length=64)
    pastor_in_charge = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=64)
    is_the_event_approved = models.CharField(max_length=64)
    approved_by = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.event_title}'

class First_Timer(models.Model):
    id = models.AutoField(primary_key=True)
    visitors_name = models.CharField(max_length=64)
    who_invited_you = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=64)
    email_address = models.CharField(max_length=64)
    purpose_of_coming = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    sex = models.CharField(max_length=64)
    marital_status = models.CharField(max_length=64)
    would_you_like_to_be_our_member = models.CharField(max_length=64)
    your_experience_in_the_service = models.CharField(max_length=64)
    have_you_given_your_life_to_christ = models.CharField(max_length=64)
    if_yes_date_converted = models.CharField(max_length=64)
    your_prayer_request = models.CharField(max_length=64)
    will_you_like_to_fellowship_with_us_again = models.CharField(max_length=64)
    record_officer = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.visitors_name}'

class Order_Of_Service(models.Model):
    id = models.AutoField(primary_key=True)
    nature_of_service = models.CharField(max_length=64)
    activities = models.CharField(max_length=64)
    duration = models.CharField(max_length=64)
    activities_moderator = models.CharField(max_length=64)
    service_time = models.CharField(max_length=64)
    service_cordinator = models.CharField(max_length=64)
    service_date = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.nature_of_service}'

class Facility_Management(models.Model):
    id = models.AutoField(primary_key=True)
    facility_name = models.CharField(max_length=64)
    facility_type = models.CharField(max_length=64)
    facility_location = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    maintenance_log = models.CharField(max_length=64)
    last_date_maintained = models.CharField(max_length=64)
    next_due_date = models.CharField(max_length=64)
    maintenance_expense = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.facility_name}'

class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    quantity = models.CharField(max_length=64)
    status = models.CharField(max_length=64)
    other_info = models.CharField(max_length=64)
    record_officer = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.description}'

class Income(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return f'{self.description}'

class Expense(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return f'{self.description}'


class Department(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True, null=True)
    members = models.ManyToManyField(Members)
    
    def __str__(self):
        return self.name


class Churcharm(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True, null=True)
    members = models.ManyToManyField(Members)
    
    def __str__(self):
        return self.name


class Payroll(models.Model):
    id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Members, on_delete=models.CASCADE)
    date = models.DateField()
    gross = models.FloatField(blank=True, null=True)
    tax = models.FloatField(blank=True, null=True)
    net = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.gross:
            self.tax = self.gross * 0.075
            self.net = self.gross - self.tax
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.member.name} - {self.date}"