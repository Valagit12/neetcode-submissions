class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    

        '''

        - - - - - - - - - T
        a.  n  

        position = speed*time + start
        position_a = 3*time + 1
        position_b = 2*time + 4

        speeda*time + starta = speedb*time + startb
        time(speeda - speedb) = startb - starta
        time = (startb - starta)/(speeda - speedb)

        '''

        cars = [(pos, spd) for pos,spd in zip(position, speed)]
        stack = []

        cars.sort()

        print(cars)
        
        for car in cars[::-1]:
            
            pos, spd = car

            timetotarget = (target - pos) / spd

            if stack and timetotarget <= stack[-1]:
                continue
            else:
                stack.append(timetotarget)

        return len(stack)

        # (0 1) (1 2)

        # - - - - - - - - - - -

        
            
            
            


            
        return len(stack)