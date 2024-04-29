import os

# Define the root directory of your Django project here
root_dir = "."


def remove_migration_files(directory):
    for root, dirs, files in os.walk(directory, topdown=True):
        # Skip certain directories by modifying the 'dirs' list in-place
        dirs[:] = [d for d in dirs if d not in [".venv"]]

        for file in files:
            if "migrations" in root and file.endswith(".py") and file != "__init__.py":
                os.remove(os.path.join(root, file))
                print(f"Removed {file} in {root}")


# Call the function and pass the root dichrectory of your Django project
remove_migration_files(root_dir)
