import requests
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from taskify.models import Task, Category, Comment
from django.utils import timezone
import random

class Command(BaseCommand):
    help = 'Populate the database with fake users and tasks using DummyJSON API'

    def handle(self, *args, **kwargs):
        # Fetch fake users
        user_response = requests.get('https://dummyjson.com/users?limit=10')
        users = user_response.json()['users']

        # Create users
        for user_data in users:
            user = User.objects.create_user(
                username=user_data['username'],
                email=user_data['email'],
                password='password123'
            )
            user.save()

        # Fetch fake tasks
        task_response = requests.get('https://dummyjson.com/todos?limit=10')
        tasks = task_response.json()['todos']

        # Create categories
        categories = ['Work', 'Personal', 'Shopping', 'Health', 'Finance']
        category_objects = []
        for category_name in categories:
            category = Category(name=category_name)
            category.save()
            category_objects.append(category)

        # Create tasks and comments
        for task_data in tasks:
            user = random.choice(User.objects.all())
            category = random.choice(category_objects)
            task = Task.objects.create(
                title=task_data['todo'],
                description='This is a randomly generated task.',
                due_date=timezone.now() + timezone.timedelta(days=random.randint(1, 30)),
                completed=task_data['completed'],
                priority=random.choice(['LOW', 'MEDIUM', 'HIGH']),
                user=user,
                category=category
            )
            task.save()

            # Create comments for each task
            for _ in range(random.randint(1, 5)):
                comment = Comment.objects.create(
                    task=task,
                    text='This is a randomly generated comment.',
                    created_at=timezone.now()
                )
                comment.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with fake users and tasks.'))