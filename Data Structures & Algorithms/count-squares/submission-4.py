class CountSquares:
    
    # where points are stored as (x, y) -> freq
    points: {(int, int), int}

    def __init__(self):
        # dictionary to hold x y pairs -> x maps to an array (assuming dups count as more squares)
        # of y's
        # when it comes time to count given a point, look at dict of point's x
        # since 3 other points are needed to make a square (one has to have same x): 
        # I can check for a matching x. Now that I have a pair of x's I check their values for pairs of y's 
        
        self.points = {}

    # 3, 2   2, 3
    def add(self, point: List[int]) -> None:
        xy = (point[0], point[1])
        if not self.points.get(xy):
            self.points[xy] = 1
        else: 
            self.points[xy] += 1

    def count(self, point: List[int]) -> int:
        count = 0
        x = point[0]
        y = point[1]

        # algo looks for rectangles as well
        for (qx, qy) in self.points:
            # look for each diagonal, once there is, look for both point's neighbors
            if 0 != abs(qx - x) == abs(qy - y):
                if (qx, y) in self.points and (x, qy) in self.points: 
                    count += self.points[qx, qy] * self.points[qx, y] * self.points[x, qy]
        
        return count

        
