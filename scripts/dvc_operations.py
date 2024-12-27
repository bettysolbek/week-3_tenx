import subprocess

def run_command(command):
    """
    Helper function to execute shell commands.
    Args:
        command (list): Command to execute as a list.
    """
    try:
        subprocess.run(command, check=True)
        print(f"Command {' '.join(command)} executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def initialize_dvc():
    """Initialize DVC in the project."""
    run_command(['dvc', 'init'])

def setup_remote(remote_name, remote_path):
    """Set up a DVC remote."""
    run_command(['dvc', 'remote', 'add', '-d', remote_name, remote_path])

def add_dataset(dataset_path):
    """Add a dataset to DVC tracking."""
    run_command(['dvc', 'add', dataset_path])

def push_to_remote():
    """Push data to the configured DVC remote."""
    run_command(['dvc', 'push'])

def commit_changes(message):
    """Commit changes to Git."""
    run_command(['git', 'add', '.'])
    run_command(['git', 'commit', '-m', message])
