import abc
import argparse
from typing import Type

from src.project_manager import ProjectManager
from src.utils.errors import print_error

COMMAND_DEST = 'command'

PROJECT_SUBCOMMAND_DEST = 'project_command'
PROJECT_COMMAND = 'project'
PROJECT_NEW_SUBCOMMAND = 'new'
PROJECT_DELETE_SUBCOMMAND = 'delete'
PROJECT_LIST_SUBCOMMAND = 'list'


class Command(abc.ABC):
    """Abstract class for every command"""
    @abc.abstractmethod
    def add_arguments(self, parser: argparse.ArgumentParser):
        pass

    @abc.abstractmethod
    def execute(self, args: argparse.Namespace):
        pass


class ProjectCommand(Command):
    """Manage projects"""

    def __init__(self) -> None:
        self.subcommands: dict[str, Command] = {}

    def add_subcommand(self, name: str, subcommand: Command):
        self.subcommands[name] = subcommand

    def add_arguments(self, parser: argparse.ArgumentParser):
        project_subparsers = parser.add_subparsers(
            dest=PROJECT_SUBCOMMAND_DEST,
            help='Project actions',
        )

        for name, subcommand in self.subcommands.items():
            subparser = project_subparsers.add_parser(
                name,
                help=subcommand.__doc__,
            )
            subcommand.add_arguments(subparser)

    def execute(self, args: argparse.Namespace):
        if args.project_command in self.subcommands:
            self.subcommands[args.project_command].execute(args)
        else:
            print_error("Unknown project command")


class NewProjectCommand(Command):
    """Create a new project"""

    def add_arguments(self, subparser: argparse.ArgumentParser):
        subparser.add_argument(
            'project_name',
            type=str,
            help='Name of the new project',
        )
        subparser.add_argument(
            '-p',
            '--project_dir',
            type=str,
            default=None,
            help='Directory of the new project',
        )

    def execute(self, args: argparse.Namespace):
        try:
            ProjectManager.create_project(
                args.project_name,
                args.project_dir,
            )
            print(f"Project '{args.project_name}' successfully created")
        except FileExistsError:
            print_error(
                f"project '{args.project_name}' already exists"
            )
        except FileNotFoundError:
            print_error(
                f"the directory '{args.project_dir}' does not exist"
            )
        except Exception as e:
            print_error(
                "an unexpected error occured "
                f"while creating the project: {e}"
            )


class DeleteProjectCommand(Command):
    """Delete a project"""

    def add_arguments(self, subparser: argparse.ArgumentParser):
        subparser.add_argument(
            'project_name',
            type=str,
            help='Name of the new project',
        )

    def execute(self, args: argparse.Namespace):
        try:
            ProjectManager.delete_project(
                args.project_name,
            )
            print(f"Project '{args.project_name}' successfully deleted")
        except Exception as e:
            print_error(
                "an unexpected error occured "
                f"while deleting the project: {e}"
            )


class ListProjectsCommand(Command):
    """List all available projects"""

    def add_arguments(self, subparser: argparse.ArgumentParser):
        pass

    def execute(self, args: argparse.Namespace):
        try:
            list = ProjectManager.list_projects()
            if len(list) == 0:
                print('No active projects available')
            else:
                print('Available projects:', end='\n\t')
                print(*list, sep='\n\t')
        except Exception as e:
            print_error(
                "an unexpected error occured "
                f"while listing projects: {e}"
            )


class CommandFactory:
    """Factory for creating commands"""

    commands: dict[str, Type[Command]] = {}

    @classmethod
    def add_command(cls, command_name: str, command_type: Type[Command]):
        cls.commands[command_name] = command_type

    @classmethod
    def get_command(cls, command_name: str):
        if command_name in cls.commands:
            command_type = cls.commands.get(command_name)
            if command_type:
                return command_type()

        return None


class ArgsParser:
    def __init__(self, program_name: str) -> None:
        self.parser = argparse.ArgumentParser(
            prog=program_name,
        )
        self.subparsers = self.parser.add_subparsers(
            title='valid subcommands',
            dest=COMMAND_DEST,
        )

        self._setup_project_commands()

    def _setup_project_commands(self):
        for command_name, command_type in CommandFactory.commands.items():
            command = command_type()
            subparser = self.subparsers.add_parser(
                command_name,
                help=command.__doc__,
            )
            command.add_arguments(subparser)

    def run(self):
        try:
            args = self.parser.parse_args()

            if args.command:
                command = CommandFactory.get_command(args.command)
                if command:
                    command.execute(args)
                else:
                    print_error(f"command '{args.command}' not recognized")
            else:
                self.parser.print_help()

        except Exception as e:
            print_error(f'an unexpected error occured: {e}')


# Commands/subcommands registering
project_command = ProjectCommand()
project_command.add_subcommand(PROJECT_NEW_SUBCOMMAND, NewProjectCommand())
project_command.add_subcommand(
    PROJECT_DELETE_SUBCOMMAND, DeleteProjectCommand()
)
project_command.add_subcommand(PROJECT_LIST_SUBCOMMAND, ListProjectsCommand())

CommandFactory.add_command(PROJECT_COMMAND, lambda: project_command)
