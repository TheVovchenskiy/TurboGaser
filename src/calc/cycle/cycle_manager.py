import os
import re

from src.calc.config_manager import ConfigManager


PROJECT_CYCLE_DIR = 'cycle'
CALC_PREFIX = 'calc_'
CYCLE_CONFIG_FILE = './src/calc/cycle/config/input.py'
CYCLE_CONFIG_PATH = os.path.normpath(
    os.path.join(os.getcwd(), CYCLE_CONFIG_FILE)
)


class CycleManager:
    """Main entry point of calculating cycle of GTE"""
    @staticmethod
    def _is_calc_dir(dir_name: str) -> bool:
        """Returns true if given `dir_name` is calc with id"""
        match = re.fullmatch(rf'{CALC_PREFIX}[\d]+', dir_name)
        return match is not None

    @staticmethod
    def create_calc(project_path: str) -> int:
        """Create new calculation of a cycle, returns id of new calc"""
        cycle_path = os.path.join(project_path, PROJECT_CYCLE_DIR)
        if not os.path.exists(cycle_path):
            os.mkdir(cycle_path)
        # list all directories in cycle folder
        directories = list(os.walk(cycle_path))[0][1]

        # calc_dirs: list[str] = []
        max_id = 0
        for directory in directories:
            if CycleManager._is_calc_dir(directory):
                calc_id = int(directory.removeprefix(CALC_PREFIX))
                max_id = max(calc_id, max_id)

        new_calc_dir = os.path.join(cycle_path, f'{CALC_PREFIX}{max_id+1}')
        os.mkdir(new_calc_dir)

        ConfigManager.create_config(CYCLE_CONFIG_PATH, new_calc_dir)
        return max_id + 1
