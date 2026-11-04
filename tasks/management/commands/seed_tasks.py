from django.core.management.base import BaseCommand
from tasks.models import Task


class Command(BaseCommand):
    help = 'Seeds the database with funny and interesting sample tasks.'

    def handle(self, *args, **kwargs):
        Task.objects.all().delete()

        funny_tasks = [
            {
                'title': 'Bribe the cat for affection',
                'description': 'Offer premium tuna treats and negotiate a tentative 3-second petting agreement.',
                'completed': False,
            },
            {
                'title': 'Teach rubber duck advanced quantum computing',
                'description': 'Duck listened attentively for 3 hours and raised zero objections. Best peer review ever.',
                'completed': True,
            },
            {
                'title': 'Practice saying "It worked on my machine" in the mirror',
                'description': 'Tone must strike the perfect balance between baffled innocence and absolute conviction.',
                'completed': False,
            },
            {
                'title': 'Apologize to the houseplants for emotional neglect',
                'description': 'Water them gently and promise to never leave for the weekend without notice again.',
                'completed': True,
            },
            {
                'title': 'Search for the portal where missing socks disappear',
                'description': 'Check behind the dryer; bring snacks in case it leads to Narnia.',
                'completed': False,
            },
            {
                'title': 'Pretend to understand CSS flexbox on the first try',
                'description': 'Just keep adding justify-content and align-items until things finally center.',
                'completed': True,
            },
            {
                'title': 'Negotiate peace treaty with my alarm clock',
                'description': 'Snooze button is currently holding all the diplomatic leverage.',
                'completed': False,
            },
        ]

        for item in funny_tasks:
            Task.objects.create(**item)

        self.stdout.write(self.style.SUCCESS(f'Successfully populated {len(funny_tasks)} hilarious tasks!'))

