from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    def handle(self, *args, **options):
        group1 = Group.objects.get_or_create(name='ticketing')
        group2 = Group.objects.get_or_create(name='Accounts')
        group3 = Group.objects.get_or_create(name='Agent')
        group4 = Group.objects.get_or_create(name='SuperAdmin')
        group5 = Group.objects.get_or_create(name='Admin')
