import json
import os


CONFIG_NAME = '.turbo_gaser_config'
CONFIG_FILE = os.path.join(os.path.expanduser('~'), CONFIG_NAME)
CURRENT_PROJECT_KEY = 'current_project'
PROJECTS_LIST_KEY = 'projects_list'


class ConfigManager:
    @staticmethod
    def _save_config(current_project_path: str | None, projects_list: list[str]):
        """Save config with new data"""
        with open(CONFIG_FILE, 'w') as file:
            json.dump(
                {
                    CURRENT_PROJECT_KEY: os.path.normpath(current_project_path) if current_project_path is not None else None,
                    PROJECTS_LIST_KEY: projects_list,
                },
                file,
            )

    @staticmethod
    def _read_config() -> dict | None:
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as file:
                config = json.load(file)
                return config

        return None

    @staticmethod
    def save_current_project(project_path: str):
        """Save project as a current project to the config file"""
        config = ConfigManager._read_config()
        projects_list = []
        if config is not None:
            projects_list = config.get(PROJECTS_LIST_KEY, [])

        if project_path not in projects_list:
            projects_list.append(os.path.normpath(project_path))

        ConfigManager._save_config(project_path, projects_list)

    @staticmethod
    def get_current_project() -> str | None:
        """Returns current project's absolute path.
        If there were none projects created returns `None`"""
        config = ConfigManager._read_config()
        if config is not None:
            return config.get(CURRENT_PROJECT_KEY)
        return None

    @staticmethod
    def get_projects_list() -> list[str] | None:
        config = ConfigManager._read_config()
        if config is not None:
            return config.get(PROJECTS_LIST_KEY, None)

        return None

    @staticmethod
    def delete_project_path_from_list(project_path_to_delete: str):
        """Delete project from projects list"""
        config = ConfigManager._read_config()
        if config is not None:
            projects_list: list = config.get(PROJECTS_LIST_KEY, [])
            current_project = config.get(CURRENT_PROJECT_KEY, None)
            try:
                projects_list.remove(project_path_to_delete)
            except ValueError:
                pass
            if project_path_to_delete == current_project:
                current_project = None
            ConfigManager._save_config(current_project, projects_list)

    @staticmethod
    def set_current_project(project_path: str):
        """Set existing project as current"""
        pass
        # config = ConfigManager._read_config()
        
        # project_path = find_project_path(proj_name)
        # if project_path and os.path.exists(project_path):
        #     save_current_project_path(project_path)
        #     print(f"Current project set to: {proj_name}")
        # else:
        #     print(f"Project '{proj_name}' not found.")

    @staticmethod
    def find_project_path(proj_name):
        """Finds project by it's name"""
        pass
