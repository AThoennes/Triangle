class Triangle:

    # main method
    def main():

        # if the number enter isn't 0 then the least amount of
        # levels you can have are 1
        num = 1

        # prompt for a number of levels
        levels = int(input("How many levels? "))

        # do all this is the number of levels is greater than 0
        if levels > 0:

            # variable to keep track of the spaces
            # for each level
            spaces = levels

            # counter used in for loop
            i = 0
            for i in range(i,levels):

                # print the spaces then the stars then the spaces
                print (" "*spaces + "*" * (num+num) + " "*spaces)

                # next level will have 1 more star on each side
                num = num + 1

                # and one less space on each side
                spaces = spaces - 1
