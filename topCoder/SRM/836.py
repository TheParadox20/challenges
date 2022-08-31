class ThreeDarts:
    possiblePoints = []
    for i in range(1,4):
        for j in range(1,21):
            if (possiblePoints.count(i*j)>0):
                continue
            possiblePoints.append(i*j)
    possiblePoints.append(25)
    possiblePoints.append(50)
    possiblePoints.sort()
    def throwDarts(self, N):
        omegaTuple = ()

        #
        if (self.possiblePoints.count(N)>0):
            omegaTuple+=(N,)
            return omegaTuple
        n=[]
        while N>1:
            while(N>self.possiblePoint[42]):
                if len(n)>3:
                    return omegaTuple
                n.append(N%2)
                N-=(N%2)
            n.append(N)
            if len(n)>0:
                n.append(N-(N%2))
        return omegaTuple