class IntervalMerger:
    def __init__(self, intervals):
        self.intervals = intervals

    def merge_intervals(self):
        self.intervals.sort(key=self.sort_by_start)
        merged = []
        
        for interval in self.intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged

    def sort_by_start(self, interval):
        return interval[0]

    def display(self):
        print(self.merge_intervals())

intervals = [
    [1, 3],
    [2, 6],
    [8, 10],
    [15, 18]
]

merger = IntervalMerger(intervals)
merger.display()
