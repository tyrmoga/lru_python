def simple_lru_cache(maxsize=3):
    cache = {}
    order = []

    def decorator(func):
        def wrapper(*args):
            if args in cache:
                # Move the accessed item to the end of the order list
                order.remove(args)
                order.insert(0, args)
                return cache[args]
            result = func(*args)
            cache[args] = result
            order.insert(0, args)
            if len(cache) > maxsize:
                # Remove the least recently used item
                args = order.pop()
                del cache[args]
                return result
        return wrapper
    return decorator