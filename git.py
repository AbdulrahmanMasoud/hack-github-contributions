import os
import random

# Get number of commits from the user
try:
    NUM_COMMITS = int(input("Enter the number of commits to create: "))
except ValueError:
    print("Please enter a valid integer for the number of commits.")
    exit(1)

# Get the year from the user
try:
    year = int(input("Enter the year for the commits (e.g., 2024): "))
except ValueError:
    print("Please enter a valid year.")
    exit(1)

# Create a file for dummy commits
file_path = 'test.txt'
with open(file_path, 'a') as file:
    file.write('Initial commit\n')
os.system('git add test.txt')
os.system('git commit -m "Initial commit"')

for i in range(NUM_COMMITS):
    # Generate random month and day offset
    month = random.randint(1, 12)
    day_offset = i % 28 + 1  # Ensures the day is between 1 and 28 to avoid invalid dates

    # Construct the commit date string
    commit_date_str = f"{year}-{month:02d}-{day_offset:02d} 12:00:00"

    # Write to file to create a change
    with open(file_path, 'a') as file:
        file.write(f'Commit for {commit_date_str}\n')
    
    # Add and commit changes with the specified date
    try:
        os.system('git add test.txt')
        os.system(f'git commit --date="{commit_date_str}" -m "Commit #{i+1}"')
    except Exception as e:
        print(f"Error during commit {i+1}: {e}")

# Push commits to the remote repository
try:
    os.system('git push -u origin main')
except Exception as e:
    print(f"Error pushing to repository: {e}")


#git commit --amend --no-edit --date="Fri Nov 6 20:00:00 2015 -0600" 
#git fetch origin master
#git rebase origin/master
