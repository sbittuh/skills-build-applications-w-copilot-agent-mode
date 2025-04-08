from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(_id=ObjectId(), email='thundergod@mhigh.edu', name='Thor'),
            User(_id=ObjectId(), email='metalgeek@mhigh.edu', name='Tony Stark'),
            User(_id=ObjectId(), email='zerocool@mhigh.edu', name='Steve Rogers'),
            User(_id=ObjectId(), email='crashoverride@mhigh.edu', name='Natasha Romanoff'),
            User(_id=ObjectId(), email='sleeptoken@mhigh.edu', name='Bruce Banner'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team = Team.objects.create(name='Avengers')
        team.members.set(users)

        # Create activities
        activities = [
            Activity(_id=ObjectId(), user=users[0], type='Cycling', duration=timedelta(hours=1)),
            Activity(_id=ObjectId(), user=users[1], type='Crossfit', duration=timedelta(hours=2)),
            Activity(_id=ObjectId(), user=users[2], type='Running', duration=timedelta(hours=1, minutes=30)),
            Activity(_id=ObjectId(), user=users[3], type='Strength', duration=timedelta(minutes=30)),
            Activity(_id=ObjectId(), user=users[4], type='Swimming', duration=timedelta(hours=1, minutes=15)),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), team=team, score=500),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), name='Cycling Training', description='Training for a road cycling event'),
            Workout(_id=ObjectId(), name='Crossfit', description='Training for a crossfit competition'),
            Workout(_id=ObjectId(), name='Running Training', description='Training for a marathon'),
            Workout(_id=ObjectId(), name='Strength Training', description='Training for strength'),
            Workout(_id=ObjectId(), name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
