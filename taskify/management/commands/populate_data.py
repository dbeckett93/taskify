import random
from faker import Faker
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from taskify.models import Task, Category, Comment
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the database with fake users and tasks'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create categories
        categories = ['Work', 'Personal', 'Shopping', 'Health', 'Finance']
        category_objects = []
        for category_name in categories:
            category, created = Category.objects.get_or_create(name=category_name)
            category_objects.append(category)

        # Create users
        for _ in range(10):
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password='password123'
            )
            user.save()

        # Create tasks and comments
        for _ in range(10):
            user = random.choice(User.objects.all())
            category = random.choice(category_objects)
            task = Task.objects.create(
                title=fake.sentence(nb_words=6),
                description=fake.paragraph(nb_sentences=3),
                due_date=timezone.now() + timezone.timedelta(days=random.randint(1, 30)),
                completed=fake.boolean(),
                priority=random.choice(['LOW', 'MEDIUM', 'HIGH']),
                user=user,
                category=category
            )
            task.save()

            # Create comments for each task
            for _ in range(random.randint(1, 5)):
                comment = Comment.objects.create(
                    task=task,
                    text=fake.paragraph(nb_sentences=2),
                    created_at=timezone.now()
                )
                comment.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with fake users and tasks.'))