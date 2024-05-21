#!/usr/bin/python3
''' Script console for command intrepreter'''
import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_help(self, arg):
        """Help command"""
        if arg:
            try:
                func = getattr(self, 'help_' + arg)
                func()
            except AttributeError:
                print(f"No help on {arg}")
        else:
            super().do_help(arg)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
