def interleave(*args):
    iters = [iter(arg) for arg in args]
    while True:
        try:
            for it in iters:
                #get's everytime the next element of the iter
                #but because of the for loop it takes from every iter one, and then moves on to the next iter
                # and in the second round, it takes from every iter the second element. because next saves the place
                #where it was holding
                yield next(it)
        except StopIteration:
            return

print(list(interleave('abc', [1, 2, 3], ('!', '@', '#'))))
