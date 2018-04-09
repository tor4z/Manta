import os, pkgutil

def run_dir(func_name=""):
    """
        This function *MUST* in the __init__.py
    """
    for loader, mod_name, is_pkg in pkgutil.iter_modules([os.path.dirname(__file__)]):
        try:
            mod = loader.find_module(mod_name).load_module(mod_name)
            for item in dir(mod):
                func = getattr(mod, item)
                if callable(func):
                    if not func_name or func.__name__ is func_name:
                        func()
        except AttributeError:
            pass