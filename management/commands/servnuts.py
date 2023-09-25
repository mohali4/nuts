from django.core.management.base import BaseCommand, CommandParser, CommandError

class Command(BaseCommand):
    help="start serving your bots"

    #def add_arguments(self, parser: CommandParser) -> None:
    #    parser.add_argument('')

    def handle (self, *args, **wargs): 
        pass