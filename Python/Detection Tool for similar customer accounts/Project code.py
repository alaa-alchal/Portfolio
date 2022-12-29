import csv

def extract_from_csv(filename, column_position):
    '''a function that reads csv files and extract specific columns'''
    
    with open(filename, "r", encoding='latin-1', errors='ignore') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        list = []
        for line in csv_reader:
            list.append(line[column_position])
            
    csv_file.close()
    return list

# names = extract_from_csv("test_copy.csv", 1)
# names





import difflib

def similarity(string1, string2):
    '''a function that calculates percentage similarity between 2 strings'''
    sequence = difflib.SequenceMatcher(isjunk=None, a=string1.lower(), b=string2.lower())
    difference = round(sequence.ratio() * 100, 1)
    if difference > 60:
        return difference
    return 0





def dict_with_similarities(dictionary):
    ''' 0 : (('12345', '23456'), 90.9, 69.4, 88.9)

        We have dictionries with elements like this:
            0 is the comparison number
            ('12345', '23456') are the 2 items being compared
            each of 12345 and 23456 have 3 elements being compares;
                1st is name to which there is 90.9% similarity
                2nd is address to which there is 69.4% similarity
                3rd is city to which there is 88.9& similarity 
                                                                    '''
    new_dict = dict()
    
    for x, y in dictionary.items():
        if y[1] >= 60 and y[2] >= 60 and y[3] >= 60:
            new_dict[x] = y
            

    return new_dict

# sss = {    
#             0 : (['item1', 'item2'], 50, 70, 70), 
#             1 : (['item3', 'item4'], 60, 100, 70),
#             2 : (['item2', 'item5'], 90, 90, 90)
#         }

# dict_with_similarities(sss)







import itertools


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


# L = [['a','b','c'],['b','d','e'],['k'],['o','p'],['e','f'],['p','a'],['d','g']]
# print(list_merge(L))












import csv

def write_to_file(list_to_export):
    '''Exports the list in param to a file.'''
    
    
    #Getting the number of columns needed for titles to add titles for as long as the longest amount of 
    #duplicates in one row
    def get_longest_list(lst):
        return max(lst, key=len)
    longest_list = get_longest_list(list_to_export)
    number_of_columns = len(longest_list)
    
    
    #Now creating the row that is supposed to represent the column titles in the csv
    titles_list = []
    for x in range(1, number_of_columns+1):
        titles_list.append(f'Duplicate ID{x}')
    
    
    #Now to the actual writing to file
    typo = False
    while typo == False:
        question = input("Would you like to export the duplicates into a csv? y/n\n")
        if question.lower() == "y":
            question2 = str(input("What would you like to name your csv file? (do not include .csv at the end)\n")) + ".csv"
            #add titles to csv export
            list_to_export.insert(0, titles_list)
    
            #export the csv with name: Duplicates_list.csv
            with open(question2, "w", newline="") as AAA:
                writer = csv.writer(AAA)
                writer.writerows(list_to_export)
                
            typo = True
            
        #I can remove the next 2 lines but i kept them
        elif question.lower() == "n": 
            typo = True
            
        else:
            print("The input is invalid!")
            print("Please try again: [Enter y or n] \n")

            
            
            
            
            
            
            
            
            
            
            
            
           
        
        
        
import copy


def main():
    '''function that will return a final list of which accounts are similar'''
    csv_file_to_clean = input("Enter file name:\n")
    

# 1. create a dictionary with Id as key and a tuple containing Name, address, and city as value.
   
    
    data_dict = dict()
    
    for x in range(1, len(extract_from_csv(csv_file_to_clean, 0))):
        data_dict[extract_from_csv(csv_file_to_clean, 0)[x]] = (extract_from_csv(csv_file_to_clean, 1)[x], 
                                                                extract_from_csv(csv_file_to_clean, 2)[x], 
                                                                extract_from_csv(csv_file_to_clean, 3)[x]
                                                                   )
#     for x in data_dict.items():
#         print(f'{x[0]} : {x[1]}\n')
        

    
# 2. Create a list containing tuples of the elements in the dictionary that you want to compare
    

    important_note = '''
            for x in data_dict.items():
                for y in data_dict.items():
                    print(f'{x[0]} : {y[0]}')

            Notice here that we are comparing 12345 to 23456 then again we are comparing 23456 to 12345.
            We are also comparing 12345 to 12345.
            The number of comparisons in this double loop is 7^2 = 49 while only 21 are required.
               We need go find a way to optimize the code by not performing the same comparisons twice
               or comparing the same items.
    
    The steps below remove repetitions and same-item comparisons:                   
                                                                    '''
                                                
    keys_list = list(data_dict.keys())

    who_to_compare_to = list()
        
    for x, y in enumerate(keys_list):
        for z in keys_list[x:]:
            if y == z:
                continue
            else:
                who_to_compare_to.append((y, z))

#     for x in who_to_compare_to:
#         print(x)
        
    
# 3. compare dictionary elemenets together and store comparisons in another dictionary

    comparison = 0 #assigning serial numbers to comparisons because we can't store the 2 items being compared
                   # in a list as Key to the dictionary
    
    comparisons_dict = dict()
    
    for x in who_to_compare_to:
        comparisons_dict[comparison] = (
                                            [x[0], x[1]],
                                            similarity(data_dict[x[0]][0],data_dict[x[1]][0]),
                                            similarity(data_dict[x[0]][1],data_dict[x[1]][1]),
                                            similarity(data_dict[x[0]][2],data_dict[x[1]][2])
                                        )
        comparison += 1
    
    
#     for x, y in comparisons_dict.items():
#         print(f'{x} : {y}\n')
    
    
# 5. Creating a new dictionary with only items that have similarities included

    similar_items = dict_with_similarities(comparisons_dict)
    
#     for x, y in similar_items.items():
#          print(f'{x} : {y}\n')
        
# 5. Storing the elements that are similar in a list of lists   
    
    list_of_duplicates = []
    
    for x, y in similar_items.items():
        list_of_duplicates.append(y[0])
    
#     print(list_of_duplicates)
    
#     for x in list_of_duplicates:
#         print(x)
    

    # 6. Consolidate the duplicate accounts in a common list (final step before export)

    list_merge(list_of_duplicates)
    
    print('\n\n')
    print("Here's a list of your duplicates:")
    print('\n')
    for x in list_of_duplicates:
        print(x)
    print('\n')


# 7. Export the duplicates in a csv file:
    write_to_file(list_of_duplicates)        
        
        
main()
