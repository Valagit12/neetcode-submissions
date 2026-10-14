class Twitter:

    def __init__(self):
        self.count = 0
        self.usertofollowing = defaultdict(set)
        self.tweets = defaultdict(list)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        '''
        tweets = {tweet1 : user1, tweet2 : user2, tweet 3: user1}
        '''
        # if followers empty
        heap = []
        ans = []


        followers = self.usertofollowing[userId].copy()
        followers.add(userId)
        if not followers:
            return []

        for followerId in followers:
            if self.tweets[followerId]:
                index = len(self.tweets[followerId]) - 1
                #check index is in
                count, tweetId = self.tweets[followerId][index]
                heapq.heappush(heap, [count, tweetId, index-1, followerId])
        
        heapq.heapify(heap)
        while heap and len(ans) < 10:
            count, tweetId, index, followerId = heapq.heappop(heap)
            ans.append(tweetId)

            if index >= 0:
                count, tweetId = self.tweets[followerId][index]
                heapq.heappush(heap, [count, tweetId, index-1, followerId])
        return ans
   

    def follow(self, followerId: int, followeeId: int) -> None:
        self.usertofollowing[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.usertofollowing[followerId].discard(followeeId)
    