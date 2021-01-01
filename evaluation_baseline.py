import csv
import triangle_closing as tc
import collections as coll

import webbrowser


listingfile = open('seattle_listings_14_07_2019.csv', newline='')
listing_reader = csv.reader(listingfile)

listing_header = next(listing_reader)
listing_records = list(listing_reader)

print(listing_header)
# print(len(listing_records))

# index of review_scores_rating
print(listing_header.index('review_scores_rating'))

ratings = [(row[0], row[86]) for row in listing_records]
print(ratings)

sorted_ratings = sorted(ratings, key=lambda x: x[1], reverse=False)
print(sorted_ratings)
print(len(sorted_ratings))

rating_filter = [(tup[0], float(tup[1])) for tup in sorted_ratings if tup[1] != '']
print(rating_filter)
print(len(rating_filter))

popularity = sorted(rating_filter, key=lambda x: x[1], reverse=True)
print(popularity[:5])

baseline = popularity[:10]

review_counts = coll.Counter(row[3] for row in tc.records)
print(review_counts.most_common(10))

test_user = review_counts.most_common(10)[5][0]
print(test_user)

user_listing = tc.find_listings(tc.records, test_user)
print(user_listing)

user_fellows = tc.find_travellers(tc.records, user_listing)
print(user_fellows)

counts = tc.count_triangles(tc.records, user_fellows)
print(counts)

recom_users = tc.recommend_listings(counts, user_listing)
print(recom_users)

airbnb_url = "http://airbnb.com/rooms/"

print(recom_users[0][0])
#for rec in recom_users:
#    webbrowser.open(airbnb_url + rec[0][0])

