import os


class ProjectManager:
    @staticmethod
    def create_project(project_name: str, project_dir: str | None = None):
        """Creates project folder in `project_dir` if `proj_dir` is not None,
        otherwise creates project folder in current directory.

        Raises `FileExistsError` if project with given name is already
        exists. Raises `FileNotFoundError` if given `project_dir` does not
        exist.
        """
        if project_dir is None:
            project_dir = os.getcwd()

        project_path = os.path.join(project_dir, project_name)
        try:
            os.mkdir(project_path)
        except FileExistsError as err:
            raise FileExistsError(
                'Project with given name already exists',
            )
        except FileNotFoundError as err:
            raise FileNotFoundError(
                'directory does not exist',
            )
