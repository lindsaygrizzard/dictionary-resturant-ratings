import random
def ratings_guide(filename):
    filename = open(filename)
    resturant_dic = {}

    for line in filename:
        line = line.rstrip().split(":")
        resturant_dic[line[0]] = int(line[1])

    quit_program = False

    name = raw_input("Hello! What is your name?")

    while not quit_program:
        choice = raw_input("""do you want to change the rating, add a new rating, 
            or quit, %s (add, edit, or quit) """ %(name))

        if choice.lower() == "add":
            add_ratings(filename, resturant_dic)
        elif choice.lower() == "edit":
            change_rating(filename, resturant_dic)
        elif choice.lower() == "quit":
            quit_program = True
            print "Bye bye, %s" % (name)


def add_ratings(filename, full_dic):

    quit = False

    while not quit:
        new_rst = raw_input("Enter a resturant: ").title()
        new_rting = int(raw_input("Please enter a rating: "))

        full_dic[new_rst] = new_rting

        # turn the keys or resturant_dic into a sorted list
        print_ratings(full_dic)

        go_on = raw_input("Do you want to enter another resturant? (yes or no) ")

        if go_on.lower() == "no":
            quit = True

def change_rating(filename, full_dic):
    quit_edit = False
    while not quit_edit:
        dic_length = len(full_dic)
        dic_key_arr = [i for i in full_dic]
        random_num = random.randint(0, dic_length)
        random_resturant = dic_key_arr[random_num]

        # remove this key
        full_dic.pop(random_resturant)
        
        changed_rting = int(raw_input("What is your new rating for %s: " %random_resturant))

        full_dic[random_resturant] = changed_rting  

        print_ratings(full_dic)

        go_on = raw_input("Do you want to change another resturant? (yes or no): ")

        if go_on.lower() == "no":
            quit_edit = True


def print_ratings(full_dic):
    srt_resturant = sorted(full_dic.keys())
    # loop over the srt_resturant list and print out name and rating of each
    # resturant in alphabetical order
    for key in srt_resturant:
        print "%s is rated at %d" %(key, full_dic[key])


ratings_guide("scores.txt")