#!/usr/bin/python3
""" Console Module """
import cmd
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models import storage


class HBNBCommand(cmd.Cmd):
    """ HBNB console """
    prompt = '(hbnb) '

    # console classes
    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'City': City,
        'Amenity': Amenity,
        'Review': Review,
        'State': State
    }

    # commands for console
    # create class
    def do_create(self, arg):
        """Creates a new instance """
        # split args at space
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        # class name will be element 0
        class_name = args[0]
        # check if class exists
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        # new instance class name
        new_instance = HBNBCommand.classes[class_name]()
        # iterate through args
        for param in args[1:]:
            # split at equals
            key_value = param.split("=")
            # tuple, if exactly 2, key gets first element
            # value gets 2nd element
            if len(key_value) == 2:
                key, value = key_value
                # replace underscore with space
                if value.startswith('"') and value.endswith('"'):
                    # remove qutes
                    value = value[1:-1].replace('_', ' ').replace('\\"', '"')
                    # check if is in or float
                elif '.' in value:
                    try:
                        value = float(value)
                    except ValueError:
                        continue
                else:
                    try:
                        value = int(value)
                    except ValueError:
                        continue
                    # set attr of instance
                setattr(new_instance, key, value)
                # save and print
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """ Show an instance based on class name and id """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        instance = storage.all().get(key)
        if not instance:
            print("** no instance found **")
            return
        print(instance)

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
           print("** class doesn't exist **")
           return
        # searcg in HBNCommand classes
        instances = storage.all(HBNBCommand.classes[class_name])
        # iterate through instances
        for key, obj in instances.items():
            obj_dict = obj.__dict__.copy()
            # remove sa instance
            if '_sa_instance_state' in obj_dict:
                del obj_dict['_sa_instance_state']
                # print class name, id, and dict
            print(f"[{obj.__class__.__name__}] ({obj.id}) {obj_dict}")

    def do_destroy(self, arg):
        """ Destroy an instance based on class name and id """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        instance = storage.all().get(key)
        if not instance:
            print("** no instance found **")
            return
        storage.delete(instance)
        storage.save()

    def do_update(self, arg):
        """ Update an instance based on class name and id """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        instance = storage.all().get(key)
        if not instance:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3].strip('"').replace('_', ' ')
        setattr(instance, attr_name, attr_value)
        instance.save()

    def do_EOF(self, arg):
        """ Handle EOF to exit the console """
        print()
        return True

    def do_quit(self, arg):
        """ Handle quit to exit the console """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()