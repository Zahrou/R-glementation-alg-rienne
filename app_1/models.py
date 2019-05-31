from django.db import models

# Create your models here.

class jarida(models.Model):
    num = models.CharField(max_length=4)
    date = models.DateField(unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return "%s du %s" % (self.num, self.date)


class loi(models.Model):
    num = models.CharField(max_length=10)
    date = models.DateField()
    objet = models.TextField(max_length=2000)
    journal = models.ForeignKey(jarida, on_delete=models.CASCADE)

    def __str__(self):
        return "%s du %s" % (self.num, self.date)

class ordonnance(models.Model):
    num = models.CharField(max_length=10)
    date = models.DateField()
    objet = models.TextField(max_length=2000)
    journal = models.ForeignKey(jarida, on_delete=models.CASCADE)

    def __str__(self):
        return "%s du %s" % (self.num, self.date)

class decret_executif(models.Model):
    num = models.CharField(max_length=10)
    date = models.DateField()
    objet = models.TextField(max_length=2000)
    journal = models.ForeignKey(jarida, on_delete=models.CASCADE)
    #loi = models.ForeignKey(loi, on_delete=models.CASCADE, default="")

    def __str__(self):
        return "%s du %s" % (self.num, self.date)

class decret_presidentiel(models.Model):
    num = models.CharField(max_length=10)
    date = models.DateField()
    objet = models.TextField(max_length=2000)
    journal = models.ForeignKey(jarida, on_delete=models.CASCADE)
    #loi = models.ForeignKey(loi, on_delete=models.CASCADE, default="")

    def __str__(self):
        return "%s du %s" % (self.num, self.date)

class arrete(models.Model):
    num = models.CharField(max_length=10)
    date = models.DateField()
    objet = models.TextField(max_length=2000)
    journal = models.ForeignKey(jarida, on_delete=models.CASCADE)
    #loi = models.ForeignKey(loi, on_delete=models.CASCADE, default="")

    def __str__(self):
        return "%s du %s" % (self.num, self.date)


class arrete_interministeriel(models.Model):
    num = models.CharField(max_length=10)
    date = models.DateField()
    objet = models.TextField(max_length=2000)
    journal = models.ForeignKey(jarida, on_delete=models.CASCADE)
    #loi = models.ForeignKey(loi, on_delete=models.CASCADE, default="")

    def __str__(self):
        return "%s du %s" % (self.num, self.date)

class decision(models.Model):
    num = models.CharField(max_length=10)
    date = models.DateField()
    objet = models.TextField(max_length=2000)
    journal = models.ForeignKey(jarida, on_delete=models.CASCADE)
    #loi = models.ForeignKey(loi, on_delete=models.CASCADE, default="")

    def __str__(self):
        return "%s du %s" % (self.num, self.date)
