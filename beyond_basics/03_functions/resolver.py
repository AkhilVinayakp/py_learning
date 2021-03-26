# creating a resolver class that caches the socket calls
'''
__call__()
is a special method that allows the object to be  callable like regular functions
can be usefull when we need functions that maintains the state b/w calls and required support methods
and attribute to query or chage the state

case study : creating the Resolver class that maintain the host name.

'''
import socket
from typing import Any

class Resolver:
    """ Resolver class  """
    def __init__(self) -> None:
        ''' initialize the cache '''
        self._cache = {}
    def __call__(self, host : str) -> Any:
        ''' implimenting the callable functionality '''
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]
    def clear(self):
        ''' function that clears the cache '''
        self._cache.clear()
    def has_host(self, host):
        ''' checks whether the host already cached '''
        return host in self._cache
    


'''
    Testing >>>>>>>>>>>>>>>>>>
'''
resolver = Resolver()
print(resolver.has_host('www.google.com'))
print(resolver('www.youtube.com'))
