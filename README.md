# 0x00. AirBnB clone - The console
![65f4a1dd9c51265f49d0 copy](https://github.com/Zed-bard/AirBnB_clone/assets/132649828/21d45145-1108-4f54-9d3f-d09f8ecf0272)

The command interpreter described in the provided code is a tool for interacting with a system via a command-line interface. Below is a breakdown of how to start it, how to use it, and some examples:

### Starting the Command Interpreter:

1. **Navigate to the Directory**: Open a terminal or command prompt and navigate to the directory where the script `hbnb_command.py` is located.

2. **Execute the Script**: Run the script using the Python interpreter. You can start it by typing:
   ```
   python3 hbnb_command.py
   ```
   or if it's executable:
   ```
   ./hbnb_command.py
   ```

3. **Prompt**: After executing the script, you should see a prompt `(hbnb)` indicating that the command interpreter is ready to accept commands.

### Using the Command Interpreter:

The command interpreter understands various commands and syntaxes to interact with the system. Here are some of the commands it supports:

- **Creating an Instance**:
  ```
  create <classname>
  ```
  Example: `create BaseModel`

- **Showing Instance Details**:
  ```
  show <classname> <instance_id>
  ```
  Example: `show BaseModel 1234-5678`

- **Destroying an Instance**:
  ```
  destroy <classname> <instance_id>
  ```
  Example: `destroy BaseModel 1234-5678`

- **Listing All Instances**:
  ```
  all
  ```
  Example: `all`

- **Counting Instances of a Class**:
  ```
  count <classname>
  ```
  Example: `count BaseModel`

- **Updating an Instance**:
  ```
  update <classname> <instance_id> <attribute> "<value>"
  ```
  Example: `update BaseModel 1234-5678 name "New Name"`

- **Quitting the Interpreter**:
  ```
  quit
  ```
  or press `Ctrl + D` to send an EOF (End Of File) character.

### Examples:

1. **Creating an Instance**:
   ```
   (hbnb) create BaseModel
   ```

2. **Showing Instance Details**:
   ```
   (hbnb) show BaseModel 1234-5678
   ```

3. **Destroying an Instance**:
   ```
   (hbnb) destroy BaseModel 1234-5678
   ```

4. **Listing All Instances**:
   ```
   (hbnb) all
   ```

5. **Counting Instances of a Class**:
   ```
   (hbnb) count BaseModel
   ```

6. **Updating an Instance**:
   ```
   (hbnb) update BaseModel 1234-5678 name "New Name"
   ```

7. **Quitting the Interpreter**:
   ```
   (hbnb) quit
   ```
