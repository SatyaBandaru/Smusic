from django.db import models

# Album model
class Album(models.Model):
    class Meta():
        verbose_name_plural="Album"
    Album_name=models.CharField(max_length=30, unique=True, primary_key=True)
    Album_pic=models.ImageField(upload_to='media')

    def __str__(self):
        return (self.Album_name)

#Song Model
class Songs(models.Model):
    class Meta():
        verbose_name_plural="Songs"
    Album_name=models.ForeignKey(Album,on_delete=models.CASCADE)
    Song_id=models.IntegerField()
    Song_name=models.CharField(max_length=20)
    Singer=models.CharField(max_length=30)
    Song_file=models.FileField(upload_to='media')

    def __str__(self):
        return (str(self.id)+self.Song_name)
