from sacred import Experiment
ex = Experiment('my_experiment')

"""
I have adapted this to show that only the variables in the config file may be edited from the command line.
If you try to edit the values for ayy, the console is not happy
"""

@ex.config
def my_config():
    foo = 42
    bar = 'baz'

@ex.capture
def some_function(a, foo, bar=10):
    ayy = 20
    print(a, foo, bar, ayy)

@ex.automain
def my_main():
    some_function(1, 2, 3)     #  1  2   3
    some_function(1)           #  1  42  'baz'
    some_function(1, bar=12)   #  1  42  12
    some_function()            #  TypeError: missing value for 'a'
    