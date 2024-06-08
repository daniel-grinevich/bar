import os
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def remove_migration_files(directory):

    for root, dirs, files in os.walk(directory, topdown=True):
        dirs[:] = [d for d in dirs if d not in [".venv"]]

        for file in files:
            if "migrations" in root and file.endswith(".py") and file != "__init__.py":
                full_path = os.path.join(root, file)
                os.remove(full_path)
                logging.info(f"Removed {file} in {root}")


root_dir = "."
remove_migration_files(root_dir)
