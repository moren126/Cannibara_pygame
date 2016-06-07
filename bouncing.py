import math 

class Bouncing:

    def getBounceAmount(currentBounce, bounceRate, bounceHeight):

        return int(math.sin( (math.pi / float(bounceRate)) * currentBounce ) * bounceHeight)