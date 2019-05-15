from IPython import get_ipython
from richprompt import RichPrompts

ip = get_ipython()
ip.prompts = RichPrompts(ip)
