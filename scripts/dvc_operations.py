import subprocess

def run_command(command):
    """
    Helper function to run shell commands.
    Args:
        command (list): List of command arguments.
    """
    try:
        subprocess.run(command, check=True)
        print(f"Command {' '.join(command)} executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

def initialize_dvc():
    """
    Initialize DVC in the project directory.
    """
    run_command(['dvc', 'init'])

def setup_dvc_remote(remote_name, remote_path):
    """
    Set up a DVC remote storage.
    Args:
        remote_name (str): Name of the remote storage.
        remote_path (str): Path to the remote storage.
    """
    run_command(['dvc', 'remote', 'add', '-d', remote_name, remote_path])

def add_data_to_dvc(data_path):
    """
    Add a dataset to DVC tracking.
    Args:
        data_path (str): Path to the data file or directory.
    """
    run_command(['dvc', 'add', data_path])

def push_dvc_data():
    """
    Push tracked data to remote storage.
    """
    run_command(['dvc', 'push'])

def commit_changes_to_git(commit_message):
    """
    Commit changes to Git.
    Args:
        commit_message (str): Commit message for Git.
    """
    run_command(['git', 'add', '.'])
    run_command(['git', 'commit', '-m', commit_message])
