import os
import json
from django.core.management.base import BaseCommand
from authapp.models.users import UserDRF

JSON_PATH = 'authapp/management/commands/json/'


def load_from_json(json_file_name):
    with open(os.path.join(JSON_PATH, json_file_name + '.json'), 'r', encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):

        print(JSON_PATH)
        users = load_from_json('users')  # Имя файла в скобках
        super_users = load_from_json('super_users')

        UserDRF.objects.all().delete()
        for row in users:
            UserDRF.objects.create_user(**row)

        for row in super_users:
            UserDRF.objects.create_superuser(**row)
