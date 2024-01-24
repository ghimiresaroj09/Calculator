from django.db import models

class CalculationResult(models.Model):
    num1 = models.FloatField()
    num2 = models.FloatField()
    opt = models.CharField(max_length=1)
    answer = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.answer)