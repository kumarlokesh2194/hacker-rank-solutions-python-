class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
    def computeDifference(self):
        b = []
        for i in range(len(a)):
            for j in a:
                diff = abs(a[i]-j)
                b.append(diff)
        self.maximumDifference = (max(b))
	# Add your code here

# End of Difference class
