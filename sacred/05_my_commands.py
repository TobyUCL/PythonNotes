from sacred import Experiment

ex = Experiment("my_commands")


@ex.config
def cfg():
    name = "John"


@ex.command
def greet(name):
    """
    Print a nice greet message.
    Uses the name from config.
    """
    print("Hello {}! Nice to greet you!".format(name))


@ex.command
def shout():
    """
    Shout slang question for "what is up?"
    """
    print("WHAZZZUUUUUUUUUUP!!!????")


@ex.automain
def main():
    """
    Can I produce the help documentation from the command line too?
    Yes
    python 05_my_commands.py help main
    """
    print("This is just the main command. Try greet or shout.")