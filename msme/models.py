from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator


class Msme(models.Model):

    class Meta:
        verbose_name_plural = 'Msme'


    # Choices
    SUBSIDY_APPROVAL_STATUS = (
        ("YES", "Yes"),
        ("NO", "No"),
    )
    BANK_NAME = (
        ("STATE BANK OF INDIA", "State Bank of India"),
        ("HDFC BANK", "HDFC"),
        ("INDIAN BANK", "Indian Bank"),
    )

    # Fields
    serial_num = models.AutoField(primary_key=True)
    udyog_aadhar_number = models.CharField(max_length=12, unique=True, validators=[RegexValidator(r'^\d{12}$')], null=False)
    entrepreneur_name = models.CharField(max_length=50, null=False)
    enterprise_name = models.CharField(max_length=100, null=False)
    pan_number = models.CharField(max_length=10, null=False)
    bank_account_number = models.CharField(max_length=16, validators=[RegexValidator(r'^\d{10,16}$')], null=False)
    bank_name = models.CharField(max_length=50, null=False, choices=BANK_NAME)
    branch_ifsc_code = models.CharField(max_length=50, null=False)
    partnership_members_amount = models.CharField(max_length=12, validators=[RegexValidator(r'^\d{0,10}$')])
    civil_investment = models.CharField(max_length=12, validators=[RegexValidator(r'^\d{0,11}$')])
    #subsidy_provided = models.ForeignKey(SubsidyApplication, from_fields={})
    subsidy_provided = models.CharField(max_length=8, null=False, choices=SUBSIDY_APPROVAL_STATUS)
    sector = models.CharField(max_length=14, null=False)

    def __str__(self):
        return "Udyog Aadhaar: " + str(self.udyog_aadhar_number)


"""
class SubsidyApplication(models.Model):
    subsidy_application_number = models.AutoField(primary_key=True)
    udyog_aadhar_number = models.ForeignKey(Msme, on_delete=models.CASCADE, null=False)
    sector = models.CharField(max_length=14, null=False)
    entrepreneur_name = models.CharField(max_length=50, null=False)
    bank_account_number = models.CharField(max_length=16, validators=[RegexValidator(r'^\d{10,16}$')], null=False)
    amount_of_interest = models.CharField(max_length=10, null=False)
    term_loan = models.CharField(max_length=4, null=False)
    pan_number = models.CharField(max_length=9, validators=[RegexValidator(r'^\d{9}$')], null=False)
    loan_amount = models.CharField(max_length=12, validators=[RegexValidator(r'^\d{0,11}$')], null=False)
    subsidy_amount = models.CharField(max_length=12, default=0.00)
    subsidy_claimed = models.CharField(max_length=4, null=False)
    application_date = models.DateTimeField(blank=True, null=True)
    approval_date = models.DateTimeField()



    user = models.ForeignKey('auth.user')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    notice_period = models.CharField(max_length=10)
    applied_date = models.DateTimeField(blank=True, null=True)
    upload_resume = models.FileField()

    def apply(self):
        self.applied_date = timezone.now()
        self.save()

    def __str__(self):
        return "You have successfully applied for the job - " + str(self.title)
"""
