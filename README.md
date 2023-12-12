# 0x00. AirBnB clone - The console

The Airbnb Project is a property management system that allows users to list, search, and book accommodations. It provides a command-line interface for managing property listings.

## Command Interpreter (console.py)

The `console.py` module serves as the command-line interface for interacting with the Airbnb Project. It allows users to perform various actions related to property management.

### How to Start the Command Interpreter

To start the command interpreter, follow these steps:

1. Clone the project repository:

    ```bash
    git clone https://github.com/sameduTM/AirBnB_clone.git
    ```

2. Navigate to the project directory:

    ```bash
    cd AirBnB_clone
    ```

3. Run the command interpreter:

    ```bash
    python console.py
    ```

### How to Use the Command Interpreter

Once the command interpreter is running, you can use the following commands:

## Available Commands

### `create`

Creates a new instance of `BaseModel`, saves it to the JSON file, and prints the ID.

Usage:
```bash
> create BaseModel

### `show`
Prints the string representation of an instance based on the class name and ID.

Usage:
> show BaseModel 123

destroy
Deletes an instance based on the class name and ID, saving the change to the JSON file.

Usage:
> destroy BaseModel 123

all
Prints all string representations of instances.

Usage:
> all

update
Updates an instance based on the class name, ID, attribute name, and attribute value.

Usage:
> update BaseModel 123 name "New Name"

quit or EOF
Exit the program.

Usage:
> quit
> EOF

### Contributing
If you'd like to contribute to the project, please follow the guidelines in the CONTRIBUTING.md file.

### License
This project is licensed under the MIT License.



