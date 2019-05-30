# iterate through the list of asteroids
# keep track of the latest values that we have seen
# we can use a stack
# negative asteroids move to the left
# positive asteroids move to the right
# we iterate to the right
# if the stack is empty, then we push asteroid into stack
# if the asteroid is positive

def asteroidCollision(asteroids):
    res = []
    for asteroid in asteroids:
        if len(res) == 0 or asteroid > 0:
            res.append(asteroid)
        elif asteroid < 0:
            # While top of the stack is positive.
            while len(res) and res[-1] > 0:
                # Both asteroids are equal, destroy both.
                if res[-1] == -asteroid:
                    res.pop()
                    break
                # Stack top is smaller, remove the +ve asteroid
                # from the stack and continue the comparison.
                elif res[-1] < -asteroid:
                    res.pop()
                    continue
                # Stack top is larger, -ve asteroid is destroyed.
                elif res[-1] > -asteroid:
                    break
            else:
                # -ve asteroid made it all the way to the
                # bottom of the stack and destroyed all asteroids.
                res.append(asteroid)
    return res



def asteroid_col(asteroids):
    results = []

    for asteroid in asteroids:
        if len(results) == 0:
            results.append(asteroid)
