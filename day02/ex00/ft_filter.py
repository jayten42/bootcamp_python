def ft_filter(function_to_apply, list_of_inputs):
    if function_to_apply in None:
        return (elm for elm in list_of_inputs if elm)
    return (elm for elm in list_of_inputs if function_to_apply(elm))
