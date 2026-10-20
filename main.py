from pyscript import document,display

def submit(e):
    document.getElementById("output").innerHTML = "" #clears the previous output when a new one is inputted

    Grade_7 = {'Adrian Christian Hernandez', 'Daniel Harwell', 'Robert Rodriguez', 'Claudine Amington', 'John Doe'}
    Grade_8 = {'Carlos Borromeo', 'Joaquin Castor', 'Philip Ponce', 'Gerthy Bausa', 'Danielle Sandoval'}
    Grade_9 = {'Princess Schwab', 'Nathan Ladion', 'Jericho Magsalin', 'Eran Diaz', 'Jacob Sherburn'}
    Grade_10 = {'Therese Reyes', 'Cheree Mendoza', 'Zoey Ledres', 'Samantha Lacuesta', 'Francis Fernandez'} #sets including the students in their respective grade level

    fname = (document.getElementById('firstname').value) #grabs the firstname textbox's input
    sname = (document.getElementById('surname').value) #grabs the surname textbotx's input
    result = fname + " " + sname #combines both value above and adds a space between to create the full name

    master_set = Grade_7 | Grade_8 | Grade_9 | Grade_10 #unionizes each set to become the master_set's value
    master_set.add(result) #adds inputted results into the master_set's values
    master_set = ", ".join(sorted(master_set)) #sorts the master_set's values in alaphabetical order

    full_list = master_set.split(",")

    display(f"Student list: {master_set} | " f"Total number of students:{len(full_list)}", target="output") #displays the text "student list:" and follows up with master set values, then displays the total number of values in the variable