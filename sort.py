import os
from datetime import datetime

# Specify the directory where the files are located
directory = "/Users/kaungmyatkyaw/Desktop/downloaded"

# Get the list of files in the directory
files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

# Sort the files based on their creation time
files.sort(key=lambda x: os.path.getctime(x))


