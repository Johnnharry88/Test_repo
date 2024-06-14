#!/usr/bin/python3
"""Equi-Console Module"""
import cmd
import sys
from equi_model.base_model import BaseModel
from equi_model.__init__ import storage
from equi_model.user import User
from equi_model.state import State
from equi_model.city import City
from equi_model.order import Order
from equi_model.product import Product


class EquiCommand(cmd.Cmd):
    #display a banner as soon as console is opened
    intro = "====================== Welcome to Equi-Med Console ======================"
    """hold functionalty for App console"""
    prompt = 'Equi-Med>  '
    
    classes = {
                'BaseModel': BaseModel, 'User': User
                }
    store_comd = {'all', 'count', 'create'}

    def precmd(self, line):
        """Changes imput command line to desired format
        format: <class name>. <command>
        """
        #setting variable holders for line param
        comd = clx = id_ = _args = ''

        if not (',' in line and '(' in line and ')' in line):
            return line

        try:
            #parse line from left to right
            p_line = line[:]
            #pick up the class name
            clx = p_line[:p_line.find('.')]
            #picking up command
            comd = p_line[p_line.find('.') + 1:p_line.find('(')]
            #checks if comd is in EquiCommand.store_comd
            if comd not in EquiCommand.store_comd:
                raise Exception
            #checks out for arguments like id in parenthesis
            p_line = p_line[p_line.find('(') + 1:p_line.find(')')]
            if p_line:
                #split args
                p_line = p_line.partition(', ')
                #pick out id
                id_ = p_line[0].replace('\"', '')
                # if args exists beyind id_
                p_line = p_line[2].strip()
                if p_line:
                    if pline[0] == '{' and p_line[-1] == '}'\
                            and type(eval(p_line)) is dict:
                        _args = p_line
                    else:
                        _args = p_line.replace(',', '')
            line = ' '.join([comd, clx, id_, _args])
        except Exception as line_eror:
            pass
        finally:
            return line
    def help_quit(self):
        """Prints help documentation for quit"""
        print("Exits the console program\n")

    def do_quit(self, arg):
        """Method that exits the consol program"""
        return True
    
    def help_create(self):
        """Displays help information for the method create"""
        print('Creates a class of listed type')
        print()
        classes = 'BaseModel User'
        print(classes)
        print()
        print('Usage: create <clasname>\n')

    #implementing the create function
    def do_create(self, args):
        """Cretes Object of any class"""
        try:
            if not args:
                raise SyntaxError()
            arg = args.split(" ")
            dic = {}
            for a in arg[1:]:
                arg_split = a.split("=")
                arg_split[1] = eval(arg_split[1])
                if type(arg_split[1]) is str:
                    arg_split[1] = arg_split[1].replace("_", " ").replace('"', '"')
                dic[arg_split[0]] = arg_split[1]
        except SyntaxError:
            print("*** Class name not found ***")
        except NameError:
            print("***class name does not exist""")
        class_obj = EquiCommand.classes[arg[0]](**dic)
        class_obj.save()
        print(class_obj.id)

    def help_display(self):
        """Help information for the display command"""
        print("Displays individual instance of a class")
        print()
        print("Usage: display ,classname> <objectid>\n")

    #implementing the display function
    def do_display(self, args):
        """Method that displays individual object"""
        x = args.partition(" ")
        x_name = x[0]
        x_id = x[2]
        # Removes extra arguments from id
        if x_id and ' ' in x_id:
            x_id = x_id.partition(' ')[0]
        if not x_name:
            print("-----class name required-----")
            return
        if x_name not in EquiCommand().classes:
            print("--------class does not exist---------")
            return
        if not x_id:
            if x_name in EquiCommand().classes:
                obj = storage.all()
                for y in obj.keys():
                    if x_name in y:
                        a = obj[y]
                        print(a)
            return
        key = x_name + "." + x_id
        try:
            print(storage.equi_obj[key])
        except KeyError:
            print("----------no item mathces your input value----------")

    def help_del(seif):
        """Displays Help information on del"""
        print("Deletes a specific instancs if id")
        print()
        print("else deletes the entire class\n")

    #implementing the del function
    def do_del(self, args):
        """Deletes a specific object ont entire class if not specified with id """
        x = args.partition(" ")
        x_name = x[0]
        x_id = x[2]
        #ensuring that it only id that is used
        if x_id and ' ' in x_id:
            x_id = x_id.partiton(' ')[0]
        if not x_name:
            print('------------class name missing, invalid entry -------------')
            return
        if x_name not in EquiCommand.classes:
            print('------------- class does not exist------------')
            return
        if not x_id:
            if x_name in EquiCommand().classes:
                obj = storage.all()
                for y in obj.keys():
                    if x_name in y:
                        del(storage.all()[y])
                        storage.save()
                        print('Successfully Deleted {}'.format(x_name))
                        return
        key = x_name + '.' + x_id
        try:
            del(storage.all()[key])
            storage.save()
        except KeyError:
            print('no instance matching request')

    def help_count(self):
        """Help documentation for count"""
        print("Counts the object belonging to a class")
        print()
        print('Usage: command <classname>i\n')

    #implementing the count funciton
    def do_count(self, args):
        """Counts the number of obj in a class instance"""
        if args not in EquiCommand().classes:
            print("Object not found")
        else:
            rec = 0
            obj = storage.all()
            for y in obj.keys():
                if args in y:
                    rec += 1
            print(rec)

    def help_all(self):
        """Help infromation for the all command"""
        print('Displays all the classes created and stored')
        print()
        print('Usage: command')

    #implementing the all function
    def do_all(self, args):
        """Displays all classes in the App"""
        obj = storage.all()
        for x in obj.keys():
            a = obj[x]
            print(a)

    def help_update(self):
        """Helps show the information on display"""
        print('Changes values in clase bjects')
        print()
        print('Usage: command <classname> <id> <attval>\n')

    #implementing the update function
    def do_update(self, args):
        """Updates a certain object with new info"""
        x_name = x_id = att_name = att_val = kwargs = ''
        # Isolates the class from other args
        args = args.partition(" ")
        if args[0] and args[0] in EquiCommand().classes:
            x_name = args[0]
        else:
            print(' Class name not found')
            return
        # isolating id from other argumnents
        args = args[2].partition(" ")
        if args[0]:
            x_id = args[0]
        else:
            print('Id of object required')
            return
        # Creating key ffrom arguments passed
        key = x_name + '.' + x_id
        # Checks out if key is valid
        if key not in storage.all():
            print('Invalid key')
            return
        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
            args = []
            args.append(k)
            args.append(v)
        else:
            # if not kwargs
            args = args[2]
            if args and args[0] == '"': # checking out quotes in args
                next_quote = args.find('"', 1)
                att_name = args[1:next_quote]
                args = args[next_quote + 1:]

            args = args.partition(' ')
            # if no att_name found as a result of no quotes in args
            if not att_name and args[0] != ' ':
                att_name = args[0]

            # checks for quoted values in args
            if args[2] and args[2][0] == '"':
                att_val = args[2].partition(' ')[0]
            args = [att_name, att_val]
        # get dictionary corresponding to args
        temp_dict = storage.all()[key]
        # Checking through the args created
        for x, att_name in enumerate(args):
            # Defines only att_name during iteration
            if (x % 2 == 0):
                att_val = args[x + 1] 
                if not att_name:
                    print('Attribute nof found, check comand')
                    return
                if not att_val:
                    print(' value not found')
                temp_dict.__dict__.update({att_name: att_val})
        # Saves changes to the file
        temp_dict.save()


if __name__ == "__main__":
    EquiCommand().cmdloop()
