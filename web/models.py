from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User

from django.utils.text import slugify

import uuid
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# user table--------------------------------------------------------------------
class MyUserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None):
        if not email:
            raise ValueError("email is required")
        if not username:
            raise ValueError("Your user name is required")
        if not first_name:
            raise ValueError("Your First Name is required")
        if not last_name:
            raise ValueError("Your Last Name is required")
        
        

        user=self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, first_name, last_name, password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,

        )
        user.is_admin=True
        user.is_staff=True
        
        user.is_superuser=True
        user.save(using=self._db)
        return user

     

class MyUser(AbstractBaseUser):
    email=models.EmailField(verbose_name="email", max_length=100, unique=True)
    first_name=models.CharField(verbose_name="first name", max_length=100, unique=False)
    username=models.CharField(verbose_name="user name", max_length=100, unique=True)
    
    last_name=models.CharField(verbose_name="last name", max_length=100, unique=False)
    
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    
    last_login=models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)
    


    USERNAME_FIELD="email"
    REQUIRED_FIELDS=['username']
    
    objects=MyUserManager()

    def __str__(self):
        return self.username

    


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

# end user table -------------
# Create your models here.
class Contact(models.Model):
    Full_Name = models.CharField(max_length=100, null=True)
    Subject = models.CharField(max_length=100, null=True)
    Email = models.EmailField(max_length=200, null=True)
    Phone = models.CharField(max_length=100, null=True)
    Message = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


# for the courses to be uploaded
class Website(models.Model):
    courses = (
            ('Frontend', 'Frontend'),
			('Backend', 'Backend'),
			('Fullstack', 'Fullstack'),
			)
    part = (
            ('html and css', 'html and css'),
			('javascript', 'javascript'),
			('React js', 'React js'),
            ('Vue js', 'Vue js'),
			('Bootstrap', 'Bootstrap'),
			('Angular js', 'Angular js'),
            ('Django', 'Django'),
			('Flask', 'Flask'),
			('Php', 'Php'),
            ('Laravel', 'Laravel'),
			('Rub', 'Rub'),
			('Django, html and css', 'Django, html and css'),
            ('Flask, html and css', 'Flask, html and css'),
			('Django and react js', 'Django and react js'),
			('Php, html and css', 'Php, html and css'),
            ('Php and react js', 'Php and react js'),
			('Laravel, html and css', 'Laravel, html and css'),
			)
    Title = models.CharField(max_length=700)
    Course = models.CharField(max_length=200, null=True, choices=courses)
    Part = models.CharField(max_length=200, null=True, choices=part)
    Explanation = models.CharField(max_length=500)
    Image =models.ImageField(upload_to="home/")
    Video = models.FileField(upload_to="home/")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
class Commentwebsite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Website', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.user.first_name
    
class Mobile(models.Model):
    courses = (
            ('Frontend', 'Frontend'),
			('Backend', 'Backend'),
			('Fullstack', 'Fullstack'),
			)
    part = (
            ('React native', 'React native'),
			('Kivy', 'Kivy'),
			('Fluter', 'Fluter'),
            ('React native and firebase', 'React native and firebase'),
            ('React native and django', 'React native and django'),
            ('React native and flask', 'React native and flask'),
			)
    Title = models.CharField(max_length=700)
    Course = models.CharField(max_length=200, null=True, choices=courses)
    Part = models.CharField(max_length=200, null=True, choices=part)
    Explanation = models.CharField(max_length=500)
    Image =models.ImageField(upload_to="home/")
    Video = models.FileField(upload_to="home/")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
class Commentmobile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Mobile', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.user.username


class Desktop(models.Model):
    courses = (
            ('C++', 'C++'),
			('Kivy', 'Kivy'),
			('Pyqt', 'Pyqt'),
			)
    Title = models.CharField(max_length=700)
    Course = models.CharField(max_length=200, null=True, choices=courses)
    Explanation = models.CharField(max_length=500)
    Image =models.ImageField(upload_to="home/")
    Video = models.FileField(upload_to="home/")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
class Commentdesktop(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Desktop', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.user.Full_Name
    
    
class Embeded(models.Model):
    courses = (
            ('C++', 'C++'),
			('Arduino', 'Arduino'),
			('Python', 'Python'),
            ('Micropython', 'Micropython'),
			)
    Title = models.CharField(max_length=700)
    Course = models.CharField(max_length=200, null=True, choices=courses)
    Explanation = models.CharField(max_length=500)
    Image =models.ImageField(upload_to="home/")
    Video = models.FileField(upload_to="home/")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
class Commentembeded(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Embeded', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.user.Full_Name
    
class Graphics(models.Model):
    courses = (
            ('Adobe photoshop', 'Adobe photoshop'),
			('Adobe illustrator', 'Adobe illustrator'),
			)
    Title = models.CharField(max_length=700)
    Course = models.CharField(max_length=200, null=True, choices=courses)
    Explanation = models.CharField(max_length=500)
    Image =models.ImageField(upload_to="home/")
    Video = models.FileField(upload_to="home/")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
class Commentgraphics(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Graphics', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.user.Full_Name
    
    
# models for project

class Project(models.Model):
    type = (
            ('website', 'website'),
			('mobile', 'mobile'),
            ('desktop', 'desktop'),
			('artificial', 'artificial'),
            ('embeded', 'embeded'),
			('iot', 'iot'),
            ('virtual reality', 'virtual reality'),
			('cyber', 'cyber'),
			)
    Title = models.CharField(max_length=700)
    Explanation = models.CharField(max_length=500)
    Type = models.CharField(max_length=200, null=True, choices=type)
    Image =models.ImageField(upload_to="home/")
    Video = models.FileField(upload_to="home/")
    Project = models.FileField(upload_to="home/")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
class Commentproject(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Project', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.user.Full_Name

# MODEL FOR IMAGE
class Image(models.Model):
    Title = models.CharField(max_length=700)
    Image =models.ImageField(upload_to="home/")
    Image_download = models.FileField(upload_to="home/")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
class Commentimage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Image', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.user.Full_Name

# for the template to upload
class Websitetemplate(models.Model):
    template = (
            ('Html and css', 'Html and css'),
			('React js', 'React js'),
			)
    Title = models.CharField(max_length=700)
    Type = models.CharField(max_length=200, null=True, choices=template)
    Explanation = models.CharField(max_length=500)
    Image =models.ImageField(upload_to="home/")
    Template = models.FileField(upload_to="home/")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    template_id = models.CharField(max_length=20, editable=False, unique=True)  # Add unique=True to ensure uniqueness

    def save(self, *args, **kwargs):
        if not self.template_id:
            # Generate a unique template_id based on the Title
            self.template_id = slugify(self.Title)[:20]  # Limit to first 20 characters to fit max_length
        super().save(*args, **kwargs)

class Mobiletemplate(models.Model):
    template = (
			('React native', 'React native'),
			)
    Title = models.CharField(max_length=700)
    Type  = models.CharField(max_length=200, null=True, choices=template)
    Explanation = models.CharField(max_length=500)
    Image =models.ImageField(upload_to="home/")
    Template = models.FileField(upload_to="home/")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    mobiletemplate_id = models.CharField(max_length=20, editable=False, unique=True)  # Add unique=True to ensure uniqueness
    
    def save(self, *args, **kwargs):
        if not self.mobiletemplate_id:
            # Generate a unique mobiletemplate_id based on the Title
            self.mobiletemplate_id = slugify(self.Title)[:20]  # Limit to first 20 characters to fit max_length
        super().save(*args, **kwargs)

class Desktoptemplate(models.Model):
    template = (
            ('Kivy', 'Kivy'),
			('Pyqt', 'Pyqt'),
            ('Tkinter', 'Tkinter'),
			('C++', 'C++'),
			)
    Title = models.CharField(max_length=700)
    Type  = models.CharField(max_length=200, null=True, choices=template)
    Explanation = models.CharField(max_length=500)
    Image =models.ImageField(upload_to="home/")
    Template = models.FileField(upload_to="home/")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    template_id = models.CharField(max_length=20, editable=False, unique=True)  # Add unique=True to ensure uniqueness
    
    def save(self, *args, **kwargs):
        if not self.template_id:
            # Generate a unique template_id based on the Title
            self.template_id = slugify(self.Title)[:20]  # Limit to first 20 characters to fit max_length
        super().save(*args, **kwargs)

class Microsofttemplate(models.Model):
    template = (
            ('word', 'word'),
			('powerpoint', 'powerpoint'),
            ('excell', 'excell'),
			('publisher', 'publisher'),
			)
    Title = models.CharField(max_length=700)
    Type  = models.CharField(max_length=200, null=True, choices=template)
    Explanation = models.CharField(max_length=500)
    Image =models.ImageField(upload_to="home/")
    Template = models.FileField(upload_to="home/")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    template_id = models.CharField(max_length=20, editable=False, unique=True)  # Add unique=True to ensure uniqueness
    
    def save(self, *args, **kwargs):
        if not self.template_id:
            # Generate a unique template_id based on the Title
            self.template_id = slugify(self.Title)[:20]  # Limit to first 20 characters to fit max_length
        super().save(*args, **kwargs)
    
class Adobetemplate(models.Model):
    template = (
            ('photoshop', 'photoshop'),
			('primier', 'primier'),
            ('illustrator', 'illustrator'),
			)
    Title = models.CharField(max_length=700)
    Type  = models.CharField(max_length=200, null=True, choices=template)
    Explanation = models.CharField(max_length=500)
    Image =models.ImageField(upload_to="home/")
    Template = models.FileField(upload_to="home/")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    template_id = models.CharField(max_length=20, editable=False, unique=True)  # Add unique=True to ensure uniqueness
    
    def save(self, *args, **kwargs):
        if not self.template_id:
            # Generate a unique template_id based on the Title
            self.template_id = slugify(self.Title)[:20]  # Limit to first 20 characters to fit max_length
        super().save(*args, **kwargs)
    
    
# FOR TEMPLATE PAYMENT MODELS
class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = (
        ('paid', 'Paid'),
        ('pending', 'Pending'),
        ('failed', 'Failed'),
    )
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    template = models.ForeignKey(Websitetemplate, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='pending')
    payment_date = models.DateTimeField(auto_now_add=True)
    
    unique_code = models.CharField(max_length=100, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.unique_code:
            self.unique_code = str(uuid.uuid4()).replace('-', '')[:12]  # Generate a unique 12-character code
        super().save(*args, **kwargs)
        
class PaymentMobiletemplate(models.Model):
    PAYMENT_STATUS_CHOICES = (
        ('paid', 'Paid'),
        ('pending', 'Pending'),
        ('failed', 'Failed'),
    )
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    mobiletemplate = models.ForeignKey(Mobiletemplate, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='pending')
    payment_date = models.DateTimeField(auto_now_add=True)
    
    unique_code = models.CharField(max_length=100, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.unique_code:
            self.unique_code = str(uuid.uuid4()).replace('-', '')[:12]  # Generate a unique 12-character code
        super().save(*args, **kwargs)
        
class PaymentDesktoptemplate(models.Model):
    PAYMENT_STATUS_CHOICES = (
        ('paid', 'Paid'),
        ('pending', 'Pending'),
        ('failed', 'Failed'),
    )
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    desktoptemplate = models.ForeignKey(Desktoptemplate, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='pending')
    payment_date = models.DateTimeField(auto_now_add=True)
    
    unique_code = models.CharField(max_length=100, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.unique_code:
            self.unique_code = str(uuid.uuid4()).replace('-', '')[:12]  # Generate a unique 12-character code
        super().save(*args, **kwargs)


class PaymentMicrosofttemplate(models.Model):
    PAYMENT_STATUS_CHOICES = (
        ('paid', 'Paid'),
        ('pending', 'Pending'),
        ('failed', 'Failed'),
    )
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    microsofttemplate = models.ForeignKey(Microsofttemplate, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='pending')
    payment_date = models.DateTimeField(auto_now_add=True)
    
    unique_code = models.CharField(max_length=100, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.unique_code:
            self.unique_code = str(uuid.uuid4()).replace('-', '')[:12]  # Generate a unique 12-character code
        super().save(*args, **kwargs)
        
class PaymentAdobetemplate(models.Model):
    PAYMENT_STATUS_CHOICES = (
        ('paid', 'Paid'),
        ('pending', 'Pending'),
        ('failed', 'Failed'),
    )
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    adobetemplate = models.ForeignKey(Adobetemplate, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='pending')
    payment_date = models.DateTimeField(auto_now_add=True)
    
    unique_code = models.CharField(max_length=100, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.unique_code:
            self.unique_code = str(uuid.uuid4()).replace('-', '')[:12]  # Generate a unique 12-character code
        super().save(*args, **kwargs)
        
# FOR COURSES PAYMENT MODELS
class PaymentWebsite(models.Model):
    PAYMENT_STATUS_CHOICES = (
        ('paid', 'Paid'),
        ('pending', 'Pending'),
        ('failed', 'Failed'),
    )
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='pending')
    payment_date = models.DateTimeField(auto_now_add=True)
    
    unique_code = models.CharField(max_length=100, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.unique_code:
            self.unique_code = str(uuid.uuid4()).replace('-', '')[:12]  # Generate a unique 12-character code
        super().save(*args, **kwargs)
        
class PaymentMobile(models.Model):
    PAYMENT_STATUS_CHOICES = (
        ('paid', 'Paid'),
        ('pending', 'Pending'),
        ('failed', 'Failed'),
    )
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    mobile = models.ForeignKey(Mobile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='pending')
    payment_date = models.DateTimeField(auto_now_add=True)
    
    unique_code = models.CharField(max_length=100, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.unique_code:
            self.unique_code = str(uuid.uuid4()).replace('-', '')[:12]  # Generate a unique 12-character code
        super().save(*args, **kwargs)
        
class PaymentDesktop(models.Model):
    PAYMENT_STATUS_CHOICES = (
        ('paid', 'Paid'),
        ('pending', 'Pending'),
        ('failed', 'Failed'),
    )
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    desktop = models.ForeignKey(Desktop, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='pending')
    payment_date = models.DateTimeField(auto_now_add=True)
    
    unique_code = models.CharField(max_length=100, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.unique_code:
            self.unique_code = str(uuid.uuid4()).replace('-', '')[:12]  # Generate a unique 12-character code
        super().save(*args, **kwargs)
        
class PaymentEmbeded(models.Model):
    PAYMENT_STATUS_CHOICES = (
        ('paid', 'Paid'),
        ('pending', 'Pending'),
        ('failed', 'Failed'),
    )
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    embeded = models.ForeignKey(Embeded, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='pending')
    payment_date = models.DateTimeField(auto_now_add=True)
    
    unique_code = models.CharField(max_length=100, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.unique_code:
            self.unique_code = str(uuid.uuid4()).replace('-', '')[:12]  # Generate a unique 12-character code
        super().save(*args, **kwargs)
        
class PaymentGraphics(models.Model):
    PAYMENT_STATUS_CHOICES = (
        ('paid', 'Paid'),
        ('pending', 'Pending'),
        ('failed', 'Failed'),
    )
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    graphics = models.ForeignKey(Graphics, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='pending')
    payment_date = models.DateTimeField(auto_now_add=True)
    
    unique_code = models.CharField(max_length=100, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.unique_code:
            self.unique_code = str(uuid.uuid4()).replace('-', '')[:12]  # Generate a unique 12-character code
        super().save(*args, **kwargs)
        

# PROJECT PAYMENT
class PaymentProject(models.Model):
    PAYMENT_STATUS_CHOICES = (
        ('paid', 'Paid'),
        ('pending', 'Pending'),
        ('failed', 'Failed'),
    )
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='pending')
    payment_date = models.DateTimeField(auto_now_add=True)
    
    unique_code = models.CharField(max_length=100, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.unique_code:
            self.unique_code = str(uuid.uuid4()).replace('-', '')[:12]  # Generate a unique 12-character code
        super().save(*args, **kwargs)


# IMAGE PAYMENT
class PaymentImage(models.Model):
    PAYMENT_STATUS_CHOICES = (
        ('paid', 'Paid'),
        ('pending', 'Pending'),
        ('failed', 'Failed'),
    )
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='pending')
    payment_date = models.DateTimeField(auto_now_add=True)
    
    unique_code = models.CharField(max_length=100, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.unique_code:
            self.unique_code = str(uuid.uuid4()).replace('-', '')[:12]  # Generate a unique 12-character code
        super().save(*args, **kwargs)


