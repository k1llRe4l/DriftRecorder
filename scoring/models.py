from django.db import models

class Driver (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Score (models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    total_score = models.IntegerField()

    def __str__(self):
        return f"{self.driver.name} - {self.total_score}"