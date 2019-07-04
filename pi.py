import sys
import random

def checkCircle(x_, y_):
    '''This function checks if the point (x, y)
    lies in the circle centred at (0.5, 0.5) and with radius 0.5'''
    if (x_-0.5)**2 + (y_-0.5)**2 <= 0.5**2:
        return True
    else:
        return False

def simulate():
    '''Imagine a square with corners at (0, 0), (0, 1), (1, 1), (1, 0) and 
    a circle with centre at (0.5, 0.5) with radius 0.5. Satisfy yourself that
    theoretically if we select a point randomly from the square, the probability
    it will be in the circle is pi/4. So if we do this N times, then N*pi/4 of 
    our points will be in the circle. Conversely, if we pick N points randomly from square
    and take a ratio of those inside circle to the total and multiply this ratio by 4
    we should be near pi. This function uses random numbers to perform a simulation/experiment 
    of the Pi approximation. It randomly picks a point in the square and finally,
    it returns 1 if the point is within the circle, and 0 if outside'''

    # Generate a random fraction for the x coordinate and y coordinate
    # Not that (x, y) will always lie in the square formed by 
    # the corner points (0, 0), (0, 1), (1, 1), (1, 0)
    x = random.random()
    y = random.random()
    if checkCircle(x, y):
        return 1
    else:
        return 0

def main(N):
    inside_circle = 0
    for i in range(N):
        inside_circle += simulate()
    print N, ' simulations of Pi approximation were run...'
    print 'Fraction of points inside circle: ', 1.0*inside_circle/N
    # The ratio should be [ pi*(0.5)^2 ]/[ 1 ] = pi/4
    # So four times the above ratio should be close to pi
    print 'The Monte Carlo method gives pi = ', 4.0*inside_circle/N

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("Wrong number of arguments! Enter number of simulations to run as argument.\n"
               "Example Usage: python pi.py 1000 to run 1000 simulations\n")
    try:
        numsims = int(sys.argv[1])
    except:
        print 'Expected input type integer, obtained: ', sys.argv[1]
        sys.exit()
    main(numsims)
