# Complexity
- Time complexity:
    $O(n+m)$

- Space complexity:
    $O(n+m)$

# Code
```python3 []
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        required = [0 for _ in range(numCourses)]
        graph = defaultdict(list)
        for second, first in prerequisites:
            required[second] += 1
            graph[first].append(second)
        
        queue = deque([i for i, v in enumerate(required) if v == 0])
        orders = []
        while queue:
            curr = queue.popleft()
            orders.append(curr)
            for next_ in graph[curr]:
                required[next_] -= 1
                if required[next_] == 0:
                    queue.append(next_)
        
        return orders if sum(required) == 0 else []
```