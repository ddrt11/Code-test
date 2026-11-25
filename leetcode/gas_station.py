class Solution:
    def canCompleteCircuit(self, gas, cost):
        total = 0
        cur = 0
        start = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            cur += diff
            if cur < 0:
                start = i + 1
                cur = 0
        return start if total >= 0 else -1

if __name__ == "__main__":
    s = Solution()
    print(s.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))
    print(s.canCompleteCircuit([2,3,4],[3,4,3]))
