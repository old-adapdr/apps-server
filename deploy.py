#!/usr/bin/env python3
"""
File contains deployment script for deploying github.com/alexpdr/hs
"""
from argparse import ArgumentParser
from os import getenv
from subprocess import run
from pathlib import Path
from shutil import copyfile

# Variables
argument_parser = ArgumentParser()
root_path = getenv("ROOT_PATH")
prefix_core = "/core"
prefix_services = "/services"
prefix_stacks = "/stacks"
prefix_ssl = "/ssl"


def deploy(root_path: str, prefix: str, setup_only: bool = True):
    """
    Copies, pulls and restarts docker-compose files & services

    Arguments:
    - root_path: str, root_path of the repository/deployment target
    - prefix: str, prefix for any service subdirectories
    - setup_only: bool, toggle for setup OR setup + deploy via dc

    Returns:
    - None

    Examples:
    - deploy(root_path="/home/{USER}/{REPOSITORY}", root_path="services")
    """

    target_dir = f"{root_path}{prefix}"
    update_type = prefix.replace("/", "")

    for folder in Path(target_dir).absolute().iterdir():
        for file in Path(folder).absolute().iterdir():
            if (
                file.name.endswith(".env")
                or Path(file).is_dir()
            ):
                continue
            elif file.name.startswith("dist"):
                print(f"Updating {update_type}='{str(folder).split('/')[-1]}'")
                print("-" * 40)
                print("Copying over docker-compose file...")

                copyfile(
                    src=file.name,
                    dst=str(file.name).strip("dist.")
                )
                if setup_only:
                    print("Running dry-run, only copying over files!")
                else:
                    run(["docker-compose", "pull"], cwd=folder)
                    run(["docker-compose", "up", "-d"], cwd=folder)

                print("-" * 40)
            else:
                print("Could not find any 'dist' files, is root_path set?")


# Add arguements to parser
argument_parser.add_argument("--core", "Set true to deploy core only")
argument_parser.add_argument("--services", "Set true to deploy services only")
argument_parser.add_argument("--stacks", "Set true to deploy stacks only")
argument_parser.add_argument("--deploy", "Set true to deploy all available")

# Parse arguements
args = argument_parser.parse_args()

# Deploy new updates for services and stacks
if args.core:  # Deploy core
    deploy(root_path=root_path, prefix=prefix_core, setup_only=False)
elif args.services:  # Deploy services
    deploy(root_path=root_path, prefix=prefix_services, setup_only=False)
elif args.stacks:  # Deploy stacks
    deploy(root_path=root_path, prefix=prefix_stacks, setup_only=False)
elif args.deploy:  # Deploy all
    deploy(root_path=root_path, prefix=prefix_core, setup_only=False)
    deploy(root_path=root_path, prefix=prefix_services, setup_only=False)
    deploy(root_path=root_path, prefix=prefix_stacks, setup_only=False)
else:  # Setup only
    deploy(root_path=root_path, prefix=prefix_core)
    deploy(root_path=root_path, prefix=prefix_services)
    deploy(root_path=root_path, prefix=prefix_stacks)
