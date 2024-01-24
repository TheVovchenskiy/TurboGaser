import argparse

from src.project_manager import ProjectManager
from src.utils.errors import print_error


class ArgsParser:
    def __init__(self, program_name: str) -> None:
        self.parser = argparse.ArgumentParser(
            prog=program_name,
        )
        self.subparsers = self.parser.add_subparsers(
            title='valid subcommands',
            dest='command',
        )

        self._setup_project_commands()

        # self._add_subparsers()
        # self._add_arguments()

    def _setup_project_commands(self):
        # subparser for 'project' command
        self.project_parser = self.subparsers.add_parser(
            'project',
            help='Manage projects',
        )
        self.project_subparsers = self.project_parser.add_subparsers(
            dest='project_command',
            help='Project actions',
        )

        # subcommand 'new' for 'project' command
        self.new_project_parser = self.project_subparsers.add_parser(
            'new',
            help='Create a new project',
        )
        self.new_project_parser.add_argument(
            'project_name',
            type=str,
            help='Name of the new project',
        )
        self.new_project_parser.add_argument(
            '-p',
            '--project_dir',
            type=str,
            default=None,
            help='Directory of the new project',
        )

    def _handle_project_command(self, args: argparse.Namespace):
        if args.project_command == 'new':
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

        else:
            self.project_parser.print_help()

    def run(self):
        try:
            args = self.parser.parse_args()

            if args.command == 'project':
                self._handle_project_command(args)
            else:
                self.parser.print_help()

        except Exception as e:
            print_error(f'an unexpected error occured: {e}')
