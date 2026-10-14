class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # '''
        #  /1-4-5 -6                 indegrees = {0: 0, 3: 0, 1: 1/0, 2: 2/1/0, 4: 2, 5: 1, 6: 2}
        # 0. /.    |                  queue: 1, 2, 4
        #  \2-------                  ans = [0, 3, 1]
        #  /                          
        # 3                           

        # 8 <- 7                          
        # \. /                        
        #  9                      
        # '''
        # [[6, 2], [6, 5], [2, 3], [2, 0], [5, 4], [4, 1], [4, 2], [1, 0]] -> [0, 3, 1, 2, 4, 5, 6]
        # [[0, 1], [0, 2], [3, 2], [1, 4], [2, 4], [4, 5], [2, 6], [5, 6], [8, 9], [9, 7], [7, 8]] -> []
        # [[0, 1], [2, 1]] -> [0, 2, 1]
        # [], 3 -> [0, 1, 2]

        tree = {i: [] for i in range(numCourses)}
        indegree = {i: 0 for i in range(numCourses)}
        for post, pre in prerequisites:
            tree[pre].append(post)
            indegree[post] += 1
        
        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        
        ans = []
        while queue:
            currCourse = queue.popleft()
            
            ans.append(currCourse)
            for postCourse in tree[currCourse]:
                indegree[postCourse] -= 1

                if indegree[postCourse] == 0:
                    queue.append(postCourse)

        if len(ans) < numCourses: return []
        return ans
            

        
        




