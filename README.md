# Saves and Save System

This repository provides a simple Python implementation for managing save files in a game or an application. The system supports creating, updating, retrieving, and deleting save files, while maintaining an index of save files in a directory. It uses JSON format for storing data and allows you to easily manage multiple saves for your application.

Characteristics (I think so):
 - Separate the JSON content from the index table to avoid loading everything and affecting the operation
 - Call the add/delete archive method to automatically update the index table
     - This means that additional renaming functions (by calling these methods) do not need to explicitly require updating the index table.
 - Save can manage multiple archives, and the archive name can be placed in the content of the archive. The file name will be archived using time, which will avoid files with illegal characters in the name as file names, which is quite good

## Overview

### `Saves` Class
- Handles multiple save files in a specified directory.
- Maintains an index file (list.json) that keeps track of all save names and filenames.
- Provides functions to:
  - Get a list of all save names.
  - Create a new save (if the name does not already exist, automatically update index table).
  - Delete a specific save(automatically update index table).
  - Update an existing save.

### `Save` Class
- Represents an individual save file.
- Provides functions to:
  - Create a new save file.
  - Delete a save file.
  - Retrieve the contents of a save file.
  - Update the contents of a save file.

## Requirements

- Python 3.x
- `os` and `json` modules (built-in Python libraries)

## Usage

### 1. Initialization
To create a new save system, you can instantiate the Saves class, passing the directory path where you want to store the save files. Optionally, you can provide a custom file suffix (default is "json"，and it is essentially JSON).
This will generate the corresponding directory and list. json in the current execution path

```python
import Saves

saves = Saves("game_log")
```

### 2. Saving Data
To create a new save, use the sett() method. This will create a new save file with a unique filename and store the provided parameters.

```python
saves.sett(save_name="Save1", parameter={"score": 100, "level": 5})
```

### 3. Deleting a Save
To delete a specific save, use the dele() method. This will remove the save file and update the save list automatically.

```python
saves.dele(save_name="Save1")
```

### 4. Retrieving a Save
To get the contents of a specific save, use the get() method. This will load the data from the save file.

```python
save_data = saves.get(save_name="Save1")
print(save_data)
```

### 5. Updating a Save
To update an existing save file, use the update() method.

```python
saves.update(save_name="Save1", parameter={"score": 150, "level": 6})
```

### 6. Listing All Saves
To get a list of all save names, use the get_lists() method.

```python
save_names = saves.get_lists()
print(save_names)
```

## Class Details

### `Saves`
- **Methods:**
  - `__init__(self, folder_path, json_suffix="json")`: Initializes the save system, checking if the directory exists and loading the save list.
  - `get_filename(self, save_name)`: Returns the filename associated with a save name.
  - `get_lists(self)`: Returns a list of all save names.
  - `update_lists(self)`: Updates the save list stored in the index file.
  - `sett(self, save_name, parameter)`: Creates a new save.
  - `dele(self, save_name)`: Deletes a save.
  - `get(self, save_name)`: Retrieves the contents of a save.
  - `update(self, save_name, parameter)`: Updates the contents of a save.

### `Save`
- **Methods:**
  - `__init__(self, file_path)`: Initializes a single save file object.
  - `sett(self, parameter)`: Creates a new save file.
  - `dele(self)`: Deletes the save file.
  - `get(self)`: Retrieves the contents of the save file.
  - `update(self, parameter)`: Updates the contents of the save file.

## Example

```python
# Initialize the save system with a specified folder path
saves = Saves(folder_path="path_to_save_directory")

# Create a new save
saves.sett(save_name="Save1", parameter={"score": 100, "level": 1})

# Retrieve a save
save_data = saves.get(save_name="Save1")
print(save_data)  # Output: {"score": 100, "level": 1}

# Update a save
saves.update(save_name="Save1", parameter={"score": 150, "level": 2})

# Delete a save
saves.dele(save_name="Save1")

# List all save names
save_names = saves.get_lists()
print(save_names)  # Output: []
```

## Error Handling

- **FileNotFoundError**: Raised when trying to access or modify a save file that does not exist.
- **FileExistsError**: Raised when trying to create a save file that already exists.
- **JSONDecodeError**: Raised when the save list is not a valid JSON file.
  
Make sure to handle these exceptions as necessary in your application.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



---

For any issues or feature requests, feel free to open an issue in the GitHub repository.

