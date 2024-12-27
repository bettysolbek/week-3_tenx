from scripts.dvc_operations import (
    initialize_dvc, setup_remote, add_dataset, push_to_remote, commit_changes
)

# Define paths
data_path = 'data/data.csv'
remote_name = 'localstorage'
remote_path = '/path/to/your/local/storage'

# Task 2 Workflow
if __name__ == "__main__":
    # Step 1: Initialize DVC
    print("Initializing DVC...")
    initialize_dvc()

    # Step 2: Set up remote storage
    print("Setting up remote storage...")
    setup_remote(remote_name, remote_path)

    # Step 3: Add dataset to DVC
    print("Adding dataset to DVC...")
    add_dataset(data_path)

    # Step 4: Commit changes
    print("Committing changes to Git...")
    commit_changes("Added dataset and configured DVC")

    # Step 5: Push data to remote storage
    print("Pushing data to remote storage...")
    push_to_remote()
