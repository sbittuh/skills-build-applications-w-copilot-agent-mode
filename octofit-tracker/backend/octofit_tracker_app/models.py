from djongo import models

class User(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=255)
    members = models.ArrayField(model_container=User)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    duration = models.IntegerField()  # in minutes
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} by {self.user.email}"

class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.team.name}: {self.score}"

class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
