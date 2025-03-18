from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Track

@receiver(pre_save, sender=Track)
def streamable_file_creation(sender, instance, **kwargs):
    try:
        track = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        pass
    else:
        if not track.master_recording == instance.master_recording:
            print("New master!")