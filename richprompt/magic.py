from .prompts import RichPrompts
from IPython import get_ipython

OLD_PROMPTS = None
IPYTHON = get_ipython()


def load_ipython_extension(ipython):
    OLD_PROMPTS, IPYTHON.prompts = IPYTHON.prompts, RichPrompts(IPYTHON)


def unload_ipython_extension(ipython):
    OLD_PROMPTS, IPYTHON.prompts = RichPrompts(IPYTHON), IPYTHON.prompts
