from django.core.management.base import BaseCommand
from courses.models import Course


class Command(BaseCommand):
    help = 'Add AI and Machine Learning courses to the database'

    def handle(self, *args, **options):
        # Create AI course
        ai_course, created = Course.objects.get_or_create(
            title='Artificial Intelligence',
            defaults={
                'slug': 'artificial-intelligence',
                'short_desc': 'Learn the fundamentals of AI, machine learning algorithms, and neural networks',
                'duration_weeks': 12
            }
        )
        
        if created:
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created course: {ai_course.title}')
            )
        else:
            self.stdout.write(
                self.style.WARNING(f'Course already exists: {ai_course.title}')
            )

        # Create Machine Learning course
        ml_course, created = Course.objects.get_or_create(
            title='Machine Learning',
            defaults={
                'slug': 'machine-learning',
                'short_desc': 'Master supervised and unsupervised learning, data preprocessing, and model evaluation',
                'duration_weeks': 10
            }
        )
        
        if created:
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created course: {ml_course.title}')
            )
        else:
            self.stdout.write(
                self.style.WARNING(f'Course already exists: {ml_course.title}')
            )
