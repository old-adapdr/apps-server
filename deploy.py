#!/usr/bin/env python3
"""
File contains deployment script for deploying github.com/alexpdr/hs
"""
from os import getenv
from subprocess import run
from pathlib import Path
from shutil import copyfile

root_path = getenv("ROOT_PATH")
prefix_apps = "/apps"
prefix_stacks = "/stacks"


def deploy(root_path: str, prefix: str, update_type: str):
    """
    Copies, pulls and restarts docker-compose files & services

    Arguments:
    - root_path: str, root_path of the repository/deployment target
    - prefix: str, prefix for any service subdirectories
    - update_type: str, semantic name for the type of update

    Returns:
    - None

    Examples:
    - deploy("/home/USER/REPOSITORY", "SERVICES", "SERVICES")
    """
    print("-" * 40, "\nUpdating core services", "-" * 40)
    run(["docker-compose", "pull"], cwd=Path(root_path))
    run(["docker-compose", "up", "-d"], cwd=Path(root_path))

    target_dir = f"{root_path}{prefix}"
    for folder in Path(target_dir).absolute().iterdir():
        for file in Path(folder).absolute().iterdir():
            if (
                file.name.endswith(".env")
                or Path(file).is_dir()
                or str(Path(file)).find("drone")
            ):
                continue
            elif file.name.startswith("dist"):
                print("-" * 40)

                print(f"Updating {update_type}='{str(folder).split('/')[-1]}'")
                print("Copying over docker-compose file...")
                copyfile(
                    src=file.name,
                    dst=str(file.name).strip("dist.")
                )
                run(["docker-compose", "pull"], cwd=folder)
                run(["docker-compose", "up", "-d"], cwd=folder)

                print("-" * 40)


# Deploy apps
deploy(root_path=root_path, prefix=prefix_apps, update_type="app")
deploy(root_path=root_path, prefix=prefix_stacks, update_type="stack")
