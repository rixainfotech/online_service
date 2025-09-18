from django.core.management.base import BaseCommand
from courses.models import Course

class Command(BaseCommand):
    help = 'Add or update initial catalog of 9 courses to the database'

    def handle(self, *args, **options):
        catalog = [
            {
                'title': 'Artificial Intelligence',
                'slug': 'artificial-intelligence',
                'short_desc': 'Learn AI foundations, ML algorithms, and neural networks',
                'duration_weeks': 12,
            },
            {
                'title': 'Machine Learning',
                'slug': 'machine-learning',
                'short_desc': 'Supervised/unsupervised learning, preprocessing, model evaluation',
                'duration_weeks': 10,
            },
            {
                'title': 'Python with Django',
                'slug': 'python-with-django',
                'short_desc': 'Build robust backends and full-stack apps with Django & REST',
                'duration_weeks': 12,
            },
            {
                'title': 'SQL',
                'slug': 'sql',
                'short_desc': 'Queries, joins, optimization, and data modeling for real apps',
                'duration_weeks': 6,
            },
            {
                'title': 'Testing',
                'slug': 'testing',
                'short_desc': 'Unit, integration, E2E testing with pytest, Selenium, and CI',
                'duration_weeks': 8,
            },
            {
                'title': 'DevOps',
                'slug': 'devops',
                'short_desc': 'CI/CD, Docker, Kubernetes, monitoring, and cloud basics',
                'duration_weeks': 10,
            },
            {
                'title': 'Linux',
                'slug': 'linux',
                'short_desc': 'Command line, shell scripting, services, and security essentials',
                'duration_weeks': 5,
            },
            {
                'title': 'MERN Stack (JS)',
                'slug': 'mern-stack',
                'short_desc': 'MongoDB, Express, React, Node.js to build modern web apps',
                'duration_weeks': 12,
            },
            {
                'title': 'Full Stack Web3',
                'slug': 'full-stack-web3',
                'short_desc': 'Solidity, smart contracts, dApps, wallets, decentralized stacks',
                'duration_weeks': 10,
            },
        ]

        for c in catalog:
            course, created = Course.objects.get_or_create(
                title=c['title'],
                defaults={
                    'slug': c['slug'],
                    'short_desc': c['short_desc'],
                    'duration_weeks': c['duration_weeks'],
                }
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f"Created: {course.title}"))
            else:
                # Update existing record
                course.slug = c['slug']
                course.short_desc = c['short_desc']
                course.duration_weeks = c['duration_weeks']
                course.save()
                self.stdout.write(self.style.WARNING(f"Updated: {course.title}"))
