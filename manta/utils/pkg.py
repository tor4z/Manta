import os, pkgutil

def run_dir(path, func_name=""):
    """
        This function *MUST* in the __init__.py
    """
    if not isinstance(path, list):
        path = [path]

    for loader, mod_name, is_pkg in pkgutil.iter_modules(path):
        try:
            mod = loader.find_module(mod_name).load_module(mod_name)
            for item in dir(mod):
                func = getattr(mod, item)
                if callable(func):
                    if not func_name or func.__name__ is func_name:
                        func()
        except AttributeError:
            pass