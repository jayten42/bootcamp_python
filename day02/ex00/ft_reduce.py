def ft_reduce(function_to_apply, list_of_inputs):
    value = list_of_inputs.pop(0)
    for elm in list_of_inputs:
        value = function_to_apply(value, elm)
    return value
