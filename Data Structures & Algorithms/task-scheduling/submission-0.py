class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        queue = deque()
        freq = {}

        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        
        for _, frequency in freq.items():
            heapq.heappush(heap, frequency * -1)
        
        time = 1
        while heap or queue:
            print(time, heap, queue)
            if heap:
                print('in heap')
                consumed_action = heapq.heappop(heap)

                if consumed_action < -1:
                    queue.append((consumed_action + 1, time + n + 1))

            time +=1

            if queue:
                print('in queeu')
                next_time = queue[0][1]

                if next_time == time:
                    heapq.heappush(heap, queue.popleft()[0])
        
        return time - 1

        '''
        time = 4
        heap = []
        queue = [(1, 4), (1, 5)]
        '''




        




        

        


        
        

        return 2
         
            

           