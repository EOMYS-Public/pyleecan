def create_quantity(self, symbol, physic, component=None):
    """Create the quantity associate to the given symbol and physic

    Parameters
    ----------
    symbol : str
        symbol of the wanted quantity
    component : str
        component wanted of the given quantity

    Returns
    -------
    Quantity
        The wanted quantity
    """

    cleaned_symbol = _clean_symbol(symbol)

    try:
        func = _get_function_pointer(cleaned_symbol, physic)
    except:
        raise ValueError(
            f'The symbol "{symbol}" from the physic "{physic}" is unknown.'
        )

    return func()


def _clean_symbol(symbol):
    """Function for clean a symbol.
    Symbol can have some special caractere like '.', '/'.
    This function aims to replace those caracteres by interpretable ones.

    Parameters
    ----------
    symbol : str
        The symbol to clean

    Returns
    -------
    str
        The symbol that has been clean
    """
    cleaned_symbol = symbol.replace(".", "_times_")
    cleaned_symbol = cleaned_symbol.replace("/", "_per_")
    return cleaned_symbol


def _get_function_pointer(symbol, physic):
    """From the quantity symbol and physic, return a pointer to the function that create the Quantity

    Parameters
    ----------
    symbol : str
        the symbol of the quantity
    physic : str
        the physic of the quantity

    Returns
    -------
    function
        function that create the Quantity
    """
    func_file_name = f"{physic}_quantity_maker"
    func_name = f"{symbol}__quantity_maker"
    imported_module = __import__(
        f"pyleecan.Functions.Quantity.{func_file_name}",
        fromlist=[func_file_name],
    )
    return getattr(imported_module, func_name)
