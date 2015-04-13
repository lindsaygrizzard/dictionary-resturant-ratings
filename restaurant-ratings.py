# your code goes here
def ratings(filename):
    filename = open(filename)
    resturant_dic = {}

    # turn file into a dictionary
    for line in filename:
        line = line.rstrip().split(":")
        resturant_dic[line[0]] = int(line[1])

    # turn the keys or resturant_dic into a sorted list
    srt_resturant = sorted(resturant_dic.keys())

    # loop over the srt_resturant list and print out name and rating of each
    # resturant in alphabetical order
    for key in srt_resturant:
        print "%s is rated at %d" %(key, resturant_dic[key])

print(ratings("scores.txt"))