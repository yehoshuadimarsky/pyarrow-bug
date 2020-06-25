import platform
from pprint import pprint

config = {
    i: getattr(platform.uname(), i)
    for i in ["system", "release", "version", "machine", "processor"]
}
config['compiler'] = platform.python_compiler()

print('The hardware config is:')
pprint(config)
