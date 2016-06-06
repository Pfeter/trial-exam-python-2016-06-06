# Create a function that takes a list as a parameter,
# and returns a new list with all it's element value doubled.
# It should raise an error if the parameter is not a list
def doubled(input_list):
    if type(input_list) is list:
        output = []
        for i in input_list:
            output.append(i * 2)
        return output
    else:
        raise
