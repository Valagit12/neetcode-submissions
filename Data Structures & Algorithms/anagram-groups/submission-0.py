class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        answer = []
        idx = 0

        for i, s in enumerate(strs):
            # s to set
            # check if set s is in anagrams
            tempSet = tuple(sorted(s))
            if tempSet in anagrams.keys():
                # add to the bucket
                bucketidx = anagrams[tempSet]

                answer[bucketidx] += [s]
                    
            else:
                answer.append([s])
                anagrams[tempSet] = idx
                idx += 1
        
        return answer




        