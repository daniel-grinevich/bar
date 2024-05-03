import os

root_dir = "."


def remove_migration_files(directory):
    for root, dirs, files in os.walk(directory, topdown=True):
        dirs[:] = [d for d in dirs if d not in [".venv"]]

        for file in files:
            if "migrations" in root and file.endswith(".py") and file != "__init__.py":
                os.remove(os.path.join(root, file))
                print(f"Removed {file} in {root}")


remove_migration_files(root_dir)
