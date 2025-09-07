from django.db import models


class Vacs(models.Model):
    id = models.AutoField(primary_key=True, db_column="Id")
    published = models.DateTimeField(null=True, blank=True, db_column='Published')
    company = models.CharField(max_length=50, db_column='Company')
    description = models.TextField(db_column='Description')
    title = models.CharField(max_length=50, db_column='Title')

    def __str__(self):
        return ' | '.join([self.title, self.company])

    class Meta:
        db_table = 'Vacs'
