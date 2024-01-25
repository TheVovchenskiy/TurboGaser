import json
import os
import shutil
import uuid

from src.config_manager import ConfigManager


METADATA_FILE = 'meta_data.json'
PROJECT_NAME_KEY = 'project_name'
PROJECT_ID_KEY = 'project_id'


class ProjectManager:
    @staticmethod
    def is_project(project_path: str):
        """Check if given path contains project data"""
        project_metadata = ProjectManager._get_project_metadata(project_path)
        if project_metadata is not None:
            if PROJECT_NAME_KEY in project_metadata and \
                    PROJECT_ID_KEY in project_metadata:
                return True

        return False

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

        if not os.path.isabs(project_dir):
            project_dir = os.path.join(os.getcwd(), project_dir)

        project_path = os.path.join(project_dir, project_name)
        try:
            os.mkdir(project_path)
        except FileExistsError as err:
            raise FileExistsError(
                'Project with given name already exists',
            )
        except FileNotFoundError as err:
            raise FileNotFoundError(
                'Directory does not exist',
            )

        project_meta_data = {
            PROJECT_NAME_KEY: project_name,
            PROJECT_ID_KEY: str(uuid.uuid4()),
        }
        with open(os.path.join(project_path, METADATA_FILE), 'w') as file:
            json.dump(project_meta_data, file)

        ConfigManager.save_current_project(project_path)

    @staticmethod
    def _get_project_metadata(project_path: str) -> dict:
        """Get given project's metadata"""
        project_metadata_path = os.path.join(project_path, METADATA_FILE)

        if os.path.exists(project_metadata_path):
            with open(project_metadata_path) as file:
                return json.load(file)

        return None

    @staticmethod
    def _get_project_name(project_path) -> str | None:
        if ProjectManager.is_project(project_path):
            project_metadata = ProjectManager._get_project_metadata(
                project_path)
            return project_metadata.get(PROJECT_NAME_KEY)
        return None

    @staticmethod
    def delete_project(project_name: str):
        """Delete project with given name"""
        projects_list = ConfigManager.get_projects_list()
        for project_path in projects_list:
            if ProjectManager._get_project_name(project_path) == project_name:
                ConfigManager.delete_project_path_from_list(project_path)
                shutil.rmtree(project_path)
                break

    @staticmethod
    def list_projects() -> list[str]:
        """Returns list with all the valid project names"""
        res = []
        projects_list = ConfigManager.get_projects_list()
        for project_path in projects_list:
            if ProjectManager.is_project(project_path):
                res.append(ProjectManager._get_project_name(project_path))
            else:
                ConfigManager.delete_project_path_from_list(project_path)

        return res
