# RANDOM
# Pseudo random, i.e. DO NOT use for Hasing, or passwords, as the output may be
# predictable.


def main() -> None:
    """Function used to run the main code."""
    import random
    
    random.seed(0) # Take way the randomness.
    # Every time the random is called, the seed changes, but when we explicitly
    # call random.seed(n), it will return the same sequence of random.
    
    r_range = random.randrange(0, 10, 2) # Just like the range [a, b), step
    print(r_range)

    r_int = random.randint(0, 5) # [a, b]
    print(r_int)
    
    names = ['lucas', 'joão', 'maria', 'carlos']
    random_name = random.choice(names)
    print(random_name)

    sample_list = random.sample(names, k=3)
    print(sample_list)



if __name__ == '__main__':
    main()