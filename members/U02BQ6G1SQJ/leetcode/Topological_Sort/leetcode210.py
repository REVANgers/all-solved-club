import collections;

def topologySort(adjList : list, indegreeList : list) -> list:
    (courseList, dq) = ([], collections.deque([k for k in range(len(indegreeList)) if (indegreeList[k] == 0)]));
    
    # print(dq);
    
    while (dq):
        curCourse = dq.popleft();
        courseList.append(curCourse);
        
        for nextCourse in adjList[curCourse]:
            indegreeList[nextCourse] -= 1;
            
            if (indegreeList[nextCourse] == 0):
                dq.append(nextCourse);
    
    return (courseList[ : : -1] if (len(courseList) == len(adjList)) else []);

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        (adjList, indegreeList) = ([set() for _ in range(numCourses)], [0 for _ in range(numCourses)]);
        
        for (src, dst) in prerequisites:
            adjList[src].add(dst);
            indegreeList[dst] += 1;
            
        # print(adjList);
        # print(indegreeList);
        
        return topologySort(adjList, indegreeList);
