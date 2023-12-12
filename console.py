#!/usr/bin/env python3
import cmd
from models.base_model import BaseModel
from models import storage
"""This is the cmd module that contains,
        the entry point for the command interpreter.
"""


class HBNBCommand(cmd.Cmd):
    """class provides a simple command-line interface using Python cmd module
    """

    prompt = '(hbnb) '
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    }

    storage_dict = storage.all()

    def do_create(self, line):
        """ Creates a new instance of BaseModel,
            saves it (to the JSON file) and prints the id.
            Usage: create <class name>
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            cls_name = args[0]
            new_inst = globals()[cls_name]()
            print(new_inst.id)
            storage.save()

    def do_show(self, line):
        """Prints the string representation of an instance
                based on the class name and id

        Args:
            line (str): splits to two arguments class name and id
        """

        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in self.storage_dict:
            print("** no instance found **")
        else:
            print(self.storage_dict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, line):
        """Deletes an instance based on the class name,
                and id (save the change into the JSON file).

        Args:
            line (str): split into two args, classname and id
        """
        args = line.split()

        if len(args) == 0:
            print("** class name is missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in self.storage_dict():
            print("** no instance found **")
        else:
            del self.storage_dict["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances

        Args:
            line (str): takes a string of commands
        """
        args = line.split()
        dict_list = []

        if len(args) > 0:
            if args[0] not in self.__classes:
                print("** class doesn't exist **")
            else:
                for obj in storage.all().values():
                    dict_list.append(obj.__str__())
                print(dict_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id or updating
            attribute
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args[0], args[1]) not in self.storage_dict:
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            try:
                type(eval(args)) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(args) == 4:
            obj = self.storage_dict["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                typ_val = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = typ_val(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            obj = self.storage_dict["{}.{}".format(args[0], args[1])]
            for key, value in eval(args[2]).items():
                if (key in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[key])
                        in {str, int, float}):
                    typ_val = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = typ_val(value)
                else:
                    obj.__dict__[key] = value
        storage.save()

    def do_EOF(self, line):
        """EOF command to exit the program

        Args:
            line (bool): returns true and exits
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
