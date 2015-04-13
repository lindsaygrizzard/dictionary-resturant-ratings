# your code goes here
def add_ratings(filename):
    filename = open(filename)
    resturant_dic = {}
    quit = False

    while not quit:
        # turn file into a dictionary
        for line in filename:
            line = line.rstrip().split(":")
            resturant_dic[line[0]] = int(line[1])

        new_rst = raw_input("Enter a resturant: ").title()
        new_rting = int(raw_input("Please enter a rating: "))

        resturant_dic[new_rst] = new_rting

        # turn the keys or resturant_dic into a sorted list
        srt_resturant = sorted(resturant_dic.keys())

        print_ratings(srt_resturant, resturant_dic)

        go_on = raw_input("Do you want to enter another resturant? (yes or no) ")

        if go_on.lower() == "no":
            quit = True

def print_ratings(user_list, full_dic):
    # loop over the srt_resturant list and print out name and rating of each
    # resturant in alphabetical order
    for key in user_list:
        print "%s is rated at %d" %(key, full_dic[key])


add_ratings("scores.txt")