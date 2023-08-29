from django.db import transaction
from django.core.management.base import BaseCommand

from loans_for_good.models import UserFormConfiguration

import time

class Command(BaseCommand):
    help = 'Command to set previous data from UseFormConfiguration'

    @transaction.atomic
    def cmd(self):
        UserFormConfiguration.objects.create(
            name="Dados completos",
            field_settings=["email", "marital_status", "birth_date", "nationality", "phone_number", "monthly_income"]
        )

    def handle(self, *args, **options):
        script_start = time.time()
        self.cmd()
        self.stdout.write('Done with {}s'.format(time.time() - script_start))
