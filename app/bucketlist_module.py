class BucketLists(object):
    bucketlists = []

    def __init__(self):
        pass

    def create_bucket_list(self, bucketlist_name, activity):
        bucketlist = {"name": bucketlist_name, "activity": activity}
        self.bucketlists.append(bucketlist)
        print(self.bucketlists)
        return bucketlist["name"]
