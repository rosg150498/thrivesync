from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    interests = models.TextField(null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
    contact_information = models.TextField(null=True, blank=True)

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_and_time = models.DateTimeField()
    duration = models.DurationField()
    location = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='event_covers/', null=True, blank=True)
    category = models.CharField(max_length=255)
    organiser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organised_events')
    capacity = models.PositiveIntegerField()
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)

class Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='sessions')
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_and_time = models.DateTimeField()
    duration = models.DurationField()
    speaker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sessions_speaker')
    capacity = models.PositiveIntegerField()
    virtual_link = models.URLField(null=True, blank=True)

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_bookings')
    booking_date_and_time = models.DateTimeField()
    ticket_type = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedbacks')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_feedbacks')
    rating = models.PositiveIntegerField()
    comments = models.TextField()