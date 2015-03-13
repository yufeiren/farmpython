def __init__(self, hash_func=settings.DEFAULT_HASH,
            replicas=settings.DEFAULT_REPLICAS):

    self._hash = hash_func # Contains the hashing function
    self._replicas = replicas # Contains the number of replicas per node
    self._keys = [] # A sorted list of hash keys (the ring with the node positions)
    self._hash_map = {} # our ring data (hash/value where value will be the node destination)
    # Yeah we could use a sorted dict but using a list is faster for sorting

