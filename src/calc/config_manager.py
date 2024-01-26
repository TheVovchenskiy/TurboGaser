import shutil


class ConfigManager:
    @staticmethod
    def create_config(config_instance_src: str, dst: str):
        """Creates copy of a config instance in the given path"""
        shutil.copy2(config_instance_src, dst)

