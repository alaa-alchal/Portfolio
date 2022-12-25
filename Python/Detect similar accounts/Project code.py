import csv
import difflib
import itertools
import copy


def extract_from_csv(filename, column_position):
    '''a function that reads csv files and extract specific columns'''

    with open(filename, "r", encoding='latin-1', errors='ignore') as csv_file:
        csv_reader = csv.reader(csv_file)

        list = []
        for line in csv_reader:
            list.append(line[column_position])

    csv_file.close()
    return list


def similarity(string1, string2):
    '''a function that calculates percentage similarity between 2 strings'''
    sequence = difflib.SequenceMatcher(isjunk=None,a=string1.lower(),b=string2.lower())
    difference = round(sequence.ratio()*100,1)
    return difference


def assess(which_list, item_id_list):
    '''a function that assesses similarity of items inside a list with each other
        return: list containing smaller lists in this form [similarity [string1, string2]] where
                string1 and string 2 are sorted in the list inside the list
                        '''

    # 1. compare all elements to each other and return them in the form: [comparison score, [index1, index2]]
    # we're returning the max of similarity becuase apparently similarity(x,y) != similarity(y,x)
    new_list = []
    for x in range(0, len(which_list)):
        for y in range(0, len(which_list)):
            new_list.append([[item_id_list[x], item_id_list[y]],
                             max(similarity(which_list[x], which_list[y]), similarity(which_list[y], which_list[x])),
                             ])

    # 2. sort [index1, index2] in each list
    for x in new_list:
        x[0].sort()

    # 3. remove lists having objects compared to each other
    before_last = list()
    for x in new_list:
        if x[0][0] != x[0][1]:
            before_last.append(x)

            # 3. remove duplicate lists
    last = []
    for x in before_last:
        if x not in last:
            last.append(x)

    return last


def list_merge(list_of_lists):
    '''merges lists which have common elements
       Source: Stack overflow (The only code taken from the web)'''

    LL = set(itertools.chain.from_iterable(list_of_lists))
    # LL is {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'k', 'o', 'p'}
    for each in LL:
        components = [x for x in list_of_lists if each in x]
        for i in components:
            list_of_lists.remove(i)
        list_of_lists += [list(set(itertools.chain.from_iterable(components)))]

    return list_of_lists


def write_to_file(list_to_export):
    '''Exports the list in param to a file.'''

    typo = False
    while typo == False:
        question = input("Would you like to export the duplicates into a csv? y/n\n")
        if question.lower() == "y":
            question2 = str(
                input("What would you like to name your csv file? (do not include .csv at the end)\n")) + ".csv"
            # add titles to csv export
            list_to_export.insert(0, ["Duplicate ID1", "Duplicate ID2", "Duplicate ID3"])

            # export the csv with name: Duplicates_list.csv
            with open(question2, "w", newline="") as AAA:
                writer = csv.writer(AAA)
                writer.writerows(list_to_export)

            typo = True

        # I can remove the next 2 lines but i kept them
        elif question.lower() == "n":
            typo = True

        else:
            print("The input is invalid!")
            print("Please try again: enter y or n \n")


class Data:
    '''creating a class called data to which i will add the objects: series, dba, address, and city'''


def main():
    '''function that will return a final list of which accounts are similar'''
    csv_file_to_clean = input("Enter file name: \n").lower()
    print('\n')

    # 1. create a serial number attribute if you don't have IDs(every account will have an assigned unique number)
    #     series = Data()
    #     series.serial_number = list()
    #     for x in range(0,len(extract_from_csv(csv_file_to_clean, 0))):
    #          series.serial_number.append("s"+str(x))

    # create an id number attribute since we have IDs
    identification = Data()
    identification.mid_list = extract_from_csv(csv_file_to_clean, 3)

    # 2. create a dba object with an attribute called names_list.
    dba = Data()
    dba.name_list = extract_from_csv(csv_file_to_clean, 0)

    # adding another attribute with dba.name_list names compared to each other
    dba.dba_compared = assess(dba.name_list[1:], identification.mid_list[1:])

    print("List of percentages of DBAs compared:\n")
    for x in dba.dba_compared:
        print(x)
    print("\n")

    # 3. create the address object with an attribute called addresses_list.
    address = Data()
    address.addresses_list = extract_from_csv(csv_file_to_clean, 1)

    # adding another attribute with dba.name_list names compared to each other
    address.addresses_compared = assess(address.addresses_list[1:], identification.mid_list[1:])

    print("List of percentages of adresses compared:\n")
    for x in address.addresses_compared:
        print(x)
    print("\n")

    # 4. create the address object with an attribute called addresses_list.
    city = Data()
    city.cities_list = extract_from_csv(csv_file_to_clean, 2)

    # adding another attribute with dba.name_list names compared to each other
    city.cities_compared = assess(city.cities_list[1:], identification.mid_list[1:])

    print("List of percentages of cities compared:\n")
    for x in city.cities_compared:
        print(x)
    print("\n")

    # 5. create one list with all similarity percetages

    all_comparisons = Data()  # create object to add a list to it as an attribute
    all_comparisons.final_list = copy.deepcopy(dba.dba_compared)  # dba percentages to the final list

    for x in all_comparisons.final_list:  # address percentages to the final list
        for y in address.addresses_compared:
            if x[0] == y[0]:
                x.append(y[1])

    for x in all_comparisons.final_list:  # city percentages to the final list
        for y in city.cities_compared:
            if x[0] == y[0]:
                x.append(y[1])

    print("Percentages all combined list:\n")
    for x in all_comparisons.final_list:
        print(x)
    print("\n")

    # 6. Assessment of who are actually duplicates (60+% similarity on everything)
    list_of_duplicates = []
    for x in all_comparisons.final_list:
        if x[1] >= 60 and x[2] >= 60 and x[3] >= 60:
            list_of_duplicates.append(x[0])

    print("List of accounts which had similarities:\n")
    for x in list_of_duplicates:
        print(x)
    print("\n")

    # 7. Consolidate the duplicate accounts in a common list (final step before export)
    list_merge(list_of_duplicates)

    # the next 2 lines are optional (will be removed from the code after)
    for x in list_of_duplicates:
        x.sort()

    print("\nHere's the final list of duplicates:\n")
    for x in list_of_duplicates:
        print(x)

    # 8. Export the duplicates in a csv file:
    write_to_file(list_of_duplicates)


main()
# Enter: test.csv for file name
