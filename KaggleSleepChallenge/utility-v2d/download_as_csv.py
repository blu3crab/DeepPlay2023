import os

def download_local_csv_file(file_name, kaggle_working_dir):
  """Downloads a local CSV file to the Kaggle/working directory.

  Args:
    file_name: The name of the local CSV file.
    kaggle_working_dir: The path to the Kaggle/working directory.
  """

  # Copy the local CSV file to the Kaggle/working directory.
  os.system(f"cp {file_name} {kaggle_working_dir}")

# Get the path to the Kaggle/working directory.
kaggle_working_dir = os.getcwd()

# Download the local CSV file to the Kaggle/working directory.
download_local_csv_file('series_label.csv', kaggle_working_dir)

# Print a message confirming that the file was downloaded.
print(f'File data.csv downloaded successfully to {kaggle_working_dir}.')

# Python
# from kaggle.api.kaggle_api_extended import KaggleApi

# # Create a Kaggle API object.
# api = KaggleApi()

# # Get the path to the Kaggle/working directory.
# kaggle_working_dir = api.get_working_directory()

# # Upload the local CSV file to the Kaggle/working directory.
# api.upload_file(file_name, kaggle_working_dir)

# # Print a message confirming that the file was uploaded.
# print(f'File {file_name} uploaded successfully to {kaggle_working_dir}.')