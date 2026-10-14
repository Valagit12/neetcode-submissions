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
        followers = self.usertofollowing[userId]
        followers.add(userId)
        # if followers empty
        heap = []
        ans = []

        for followerId in followers:
            followertweets = self.tweets[followerId]
            for tweet in followertweets:
                heap.append(tweet)
        
        heapq.heapify(heap)
        
        i = 0
        while heap and i < 10:
            ans.append(heapq.heappop(heap)[1])
            i+=1
        
        return ans




        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.usertofollowing[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.usertofollowing[followerId].discard(followeeId)
    