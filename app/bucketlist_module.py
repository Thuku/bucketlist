class BucketLists(object):
    bucketlists = []

    def __init__(self):
        pass

    def create_bucket_list(self, bucketlist_name, activity, status):
        bucketlist = {"name": bucketlist_name,
                      "activity": activity, "status": status}
        self.bucketlists.append(bucketlist)
        print(self.bucketlists)
        return bucketlist["name"]

    def check_bucketlist_status(self):
        incomplete = []
        complete = []
        bucketlists = BucketLists.bucketlists
        print(bucketlists)
        for i in bucketlists:
            if i['status'] == 'incomplete':
                incomplete.append(i)
            elif i['status'] == 'incomplete':
                complete.append(i)
            print(i)
        return incomplete
