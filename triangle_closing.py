import csv, sys, webbrowser
import collections as coll


def find_listings(records_list, user_id1):
    listings1 = set()
    # Find listing of user
    for rows in records_list:
        if rows[3] == user_id1:
            listings1.add(rows[0])

    return listings1


def find_travellers(records_list, listings2):
    # Find fellow travellers
    fellow_travellers = set()

    for rows in records_list:
        if rows[0] in listings2:
            fellow_travellers.add(rows[3])

    return fellow_travellers


def count_triangles(records_list, fellow_travellers):
    # Find triangle user is a part of
    triangles = []
    for row in records_list:
        if row[3] in fellow_travellers:
            triangles.append(row[0])

    return coll.Counter(triangles)


def recommend_listings(counts1, user_listings, num=10):
    for listing in user_listings:
        if listing in counts1:
            counts1.pop(listing)

    return counts1.most_common(num)


if __name__ == '__main__':
    print(sys.argv)
    filename, user_id = sys.argv[1:]

    # Open and parse CSV file
    # csvFile = open('seattle_reviews_14_07_2019.csv', newline='')
    csvFile = open(filename, newline='')
    reader = csv.reader(csvFile)
    header = next(reader)
    records = list(reader)
    # user_id = '2451'

    user_listing = find_listings(records, user_id)
    user_fellows = find_travellers(records, user_listing)
    counts = count_triangles(records, user_fellows)
    recom_users = recommend_listings(counts, user_listing)

    # present the result
    for rec in recom_users:
        webbrowser.open('http://airbnb.com/rooms/' + rec[0])

    print(recom_users)
