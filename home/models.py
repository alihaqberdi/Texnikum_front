from django.db import models
from user.models import User

class Clinic(models.Model):
    name = models.CharField(verbose_name="Poliklinika nomi", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Klinika"
        verbose_name_plural = "Klinikalar"
        ordering = ("id",)

class VideoCategorie(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Video(models.Model):
    categorie = models.ForeignKey(VideoCategorie, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    front_img = models.ImageField(upload_to='video_front_images')
    link = models.URLField()
    descriptions = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class LeaderDoctor(models.Model):
    full_name = models.CharField(max_length=255, null=True)
    user = models.OneToOneField('user.User', verbose_name='Bosh shifokorni tanlang', on_delete=models.CASCADE,
                                null=True)
    clinica = models.ForeignKey('home.Clinic', max_length=255, verbose_name='Qaysi klinika bosh shifokori',
                                on_delete=models.PROTECT)
    discription = models.TextField(verbose_name="Bosh shifokor ma'lumotlari")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Bosh shifokor"
        verbose_name_plural = "Bosh shifokorlar"
        ordering = ("id",)


class Doctor(models.Model):
    full_name = models.CharField(max_length=255, null=True)
    user = models.OneToOneField('user.User', verbose_name="Doctorni tanlang", on_delete=models.CASCADE, null=True)
    clinica = models.ForeignKey('home.Clinic', verbose_name="Qaysi kilnika shifokori", on_delete=models.PROTECT)
    leader_doctor = models.ForeignKey('home.LeaderDoctor', verbose_name="Bosh vrach", on_delete=models.SET_NULL,
                                      null=True)
    discription = models.TextField(verbose_name="Bosh shifokor ma'lumotlari")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Shifokor"
        verbose_name_plural = "Shifokorlar"
        ordering = ("id",)


class Nurse(models.Model):
    full_name = models.CharField(max_length=255, null=True)
    user = models.OneToOneField('user.User', verbose_name="Hamshirani tanlang", on_delete=models.CASCADE, null=True)
    clinica = models.ForeignKey('home.Clinic', verbose_name="Qaysi kilnika shifokori", on_delete=models.PROTECT)
    doctor = models.ForeignKey('home.LeaderDoctor', verbose_name="Vrach", on_delete=models.SET_NULL, null=True)
    discription = models.TextField(verbose_name="Hamshira ma'lumotlari")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Hamshira"
        verbose_name_plural = "Hamshiralar"
        ordering = ("id",)

