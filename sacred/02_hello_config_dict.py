"""
This shows how config files may be used to change the experiment from the command line.

If the experiment is simply run from the command line
> python 02_hello_config_dict.py        ### "Hello world!'

No we may change this config file on the command line by going 
> python 02_hello_config_dict.py with recipient=galaxy      ### 'Hello galaxy!'

Preset alternatives to the config are shown below (Variant1, Variant2). We may select these by:
> python 02_hello_config_dict.py with variant1      ### 'Howdidlydoodily!'
> python 02_hello_config_dict.py with variant2      ### 'Hello Mr Man.!'
This shows that the config variants behave like changing the original config from the command line.

"""


from sacred import Experiment

ex = Experiment('hello_config')

@ex.config
def my_config():
    recipient = "world"
    message = "Hello %s!" % recipient

@ex.named_config
def variant1():
    message = "Howdidlydoodily!"

@ex.named_config
def variant2():
    recipient = "Mr Man."

@ex.named_config
def variant3():
    # recipient is not availible for some reason
    recipient = "earth"
    message = "Goodbye %s!" % recipient

#custom commands
@ex.command
def scream():
    """
    Command which screams.
    """
    print("AAAAAaaaaaaaaaahhh...")


@ex.automain
def my_main(message):
    print(message)
