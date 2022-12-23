# The objective of this project is to demonstrate an understanding of how to:
• Create and modify lists;

• Use list methods (e.g., append());

• Use list operators;

• Use file input in your code;

• Export to files;

• Process strings.

# Challenges:
manipulate lists in functions without using return statements in functions.
The use of local lists only.
multiple loop handling (loops within loops within loops).

#Process Documentation:
The program will start off by asking: Which list would you like to create? [Options: Today, Someday completed]

After choosing the list, I'll ask you if you'd like to add the items to your newly created to-do-list from a file or manually. If you type: from a file, you will be prompted to enter the name of that file while if you type: manually, you will be promted to add items to your list one by one.

Below is a scenario of creating a list from a file. In this example, the test file example.txt contains the list of items that will be added.

<img width="800" alt="image" src="https://user-images.githubusercontent.com/119257994/209270741-f719d2ff-6376-4cc5-924e-ac22885410bf.png">

The program will then ask you what would you like to do. You will have 10 options: [Options: add, completed, create, done, edit, export, prioritize, remove, sort, view].

If you type create, the program will run the previous process again and ask you about which list would you like to create. We will create a someday list now:

<img width="800" alt="image" src="https://user-images.githubusercontent.com/119257994/209271327-943f91a7-b072-41f3-835c-33ab223248d2.png">

Now you have 2 lists. You will get the 10 options of what you want at the end of each process. If you type view, the program will prompt you to enter which list would you like to display. If you type "All", the program will display all lists available:

<img width="800" alt="image" src="https://user-images.githubusercontent.com/119257994/209271566-28f3aead-736e-41fe-9e09-f860a67a4ea7.png">

Now if you type add, the program will ask you which list would you like to add to. We will be adding 2 items to the list Today. The program will then print the new list with all the items after finishing.

<img width="800" alt="image" src="https://user-images.githubusercontent.com/119257994/209271900-d29cf224-9405-49bd-9f57-f76a1b5d1cd5.png">

The remaining functions are a series of actions you can take to manipulate those lists. For instance, if you choose completed, the program will take the items that start with [x]from the first 2 lists (today and someday), and add them to the list of completed items. The  [x] sign will be removed once the items are in the completed items.


When you finish editing, you can type done, and the program will do a final print of all your lists:
(NOTE that we did not type completed before we typed done for this excecise. I only explained what completed does)

<img width="800" alt="image" src="https://user-images.githubusercontent.com/119257994/209272449-f60438e6-2737-45ad-be79-51037821c9e7.png">
