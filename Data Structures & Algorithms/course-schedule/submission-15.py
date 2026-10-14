class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''

        a -> b -> c
               -> d
            e -> 
        h -> f -> g -> h
        '''

        tree = {}

        for i in range(numCourses):
            tree[i] = []

        for pre, post in prerequisites:
            if post not in tree[pre]:
                tree[pre].append(post)
        
        
        if not prerequisites:
            return True
        
        seen = [0] * numCourses
        def dfs(start):
            if seen[start] == 1:
                return False
            
            seen[start] = 1
            for child in tree[start]:
                if not dfs(child):
                    return False
            seen[start] = 0
            tree[start] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True


        
        
