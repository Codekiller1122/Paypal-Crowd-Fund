from django.core.management.base import BaseCommand
from crowd.models import Campaign
class Command(BaseCommand):
    help = 'Seed sample campaigns'
    def handle(self, *args, **options):
        Campaign.objects.update_or_create(slug='save-the-park', defaults={'title':'Save The Community Park','description':'Help us restore the park playground','goal_cents':500000,'owner_email':'owner@example.com'})
        Campaign.objects.update_or_create(slug='school-supplies', defaults={'title':'School Supplies for Kids','description':'Provide supplies to students in need','goal_cents':200000,'owner_email':'owner2@example.com'})
        self.stdout.write(self.style.SUCCESS('Seeded campaigns.'))
