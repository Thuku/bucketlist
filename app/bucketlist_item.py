from app.bucketlist_acc import BucketLists


class BucketListItems(object):
    def add_activity(self, bucketlist_name, item):
        print(bucketlist_name, item)
        print(BucketLists.bucketlists)
        # d=(item for item in BucketLists.bucketlists if item['name']==bucketlist_name)
        for i in BucketLists.bucketlists:
            print(i)
            if i['name'] == bucketlist_name:
                print("here")
                print(i)
                l = i["activity"]
                l.append(item)
                print(l)

            # print(values)
            # print(all_buckets)
