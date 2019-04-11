"""
simulating printing models and adding them to a completed list
"""

def printing_models(unprinted_models, printed_models):
    """ function is simulating the printing process
    and moving the printed models into a different list """
    while unprinted_models:
        unprinted_model = unprinted_models.pop()
        print("Printing model: " + unprinted_model)
        printed_models.append(unprinted_model)

def show_printed_models(printed_models):
    """ show printed models """
    print("The following models have been printed: \n")
    for printed_model in printed_models:
        print(printed_model.title())

UNFINISHED_MODELS = ['superstar', 'deathstar', 'moviestar']
FINISHED_MODELS = []

printing_models(UNFINISHED_MODELS, FINISHED_MODELS)
show_printed_models(FINISHED_MODELS)

#for lists its possible to make a copy of it and use instead of original one
#to make a copy simply use
#function_name(list_name[:])
#this should prevent the original list from being eptied by the program
