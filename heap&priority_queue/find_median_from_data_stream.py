import heapq
class MedianFinder:

    def __init__(self):
        self.arr = []
        self.length = 0

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.length += 1

        # sort afterwards
        for i in range(self.length - 1, 0, -1):
            if self.arr[i] < self.arr[i-1]:
                self.arr[i], self.arr[i-1] = self.arr[i-1], self.arr[i]
            else:
                break

    def findMedian(self) -> float:
        i = self.length // 2
        if self.length % 2 == 0:
            return (self.arr[i] + self.arr[i - 1]) / 2
        return float(self.arr[i])


class MedianFinderHeap:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        # make sure both lengths are roughly the same
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2
