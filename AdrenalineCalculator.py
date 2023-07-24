import csv

def CalculateAdren(ability_class_scanner):
    adren = ability_class_scanner[-2]
    max_adren = ability_class_scanner[-1]
    classified_rotation = ability_class_scanner[:-2]

    for ability_class in classified_rotation[0]:
        print(ability_class)
        if ability_class.__contains__('Basic'):
            adren = min(adren + 8, max_adren)
            for modifier in ability_class:
                if modifier.__contains__('Energising'):
                    adren = min(adren + 2.4, max_adren)
                if modifier.__contains__('Jaws'):
                    jawsbleed = int(modifier.strip('Jaws'))
                    adren = min(adren + 2*jawsbleed, max_adren)
        elif ability_class.__contains__ ('Threshold'):
            adren = max(min(adren - 15, max_adren),0)
        elif ability_class.__contains__('Ultimate'):
            if ability_class.__contains__('V2'):
                adren = max(min(adren - 60, max_adren), 0)
            else:
                adren = max(min(adren - 80, max_adren), 0)
        elif ability_class.__contains__('Igneous'):
            if ability_class.__contains__('V2'):
                adren = max(min(adren - 20, max_adren), 0)
            else:
                adren = max(min(adren - 40, max_adren), 0)
        elif ability_class.__contains__('2h_Auto'):
            adren = min(adren + 3, max_adren)
        elif ability_class.__contains__('Mh_Auto'):
            adren = min(adren + 2, max_adren)
        elif ability_class.__contains__('Oh_Auto'):
            adren = min(adren + 1, max_adren)
        elif ability_class.__contains__('Adrenaline_Renewal'):
            adren = min(adren + 40, max_adren)
    print("Remaining Adren: " + str(adren))
    return adren

def TextReader():
    # Opens up text of abilities
    textfile = open("Ability_class.txt")
    ability_class_melee_text = textfile.read()
    ability_list = ability_class_melee_text.split('\n\n')
    ability_list_dict = {"Basic": ability_list[0], "Threshold": ability_list[1], "Ultimate": ability_list[2], "Igneous": ability_list[3], "2h_Auto": ability_list[4], "Mh_Auto": ability_list[5],
                         "Oh_Auto": ability_list[6],"Adrenaline_Renewal": ability_list[7], "Energising": ability_list[8], "Jaws1":ability_list[9],"Jaws2":ability_list[10],"Jaws3":ability_list[11],
                         "Jaws4":ability_list[12], "Jaws5":ability_list[13], "V2":ability_list[14]}

    # Format Uncleaned Dictionary.
    basic_list = ability_list_dict['Basic'].strip('][').split(', ')
    Threshold_list = ability_list_dict['Threshold'].strip('][').split(', ')
    Ultimate_list = ability_list_dict['Ultimate'].strip('][').split(', ')
    Igneous_list = ability_list_dict['Igneous'].strip('][').split(', ')
    Twohanded_Auto = ability_list_dict['2h_Auto'].strip('][').split(', ')
    Mh_Auto = ability_list_dict['Mh_Auto'].strip('][').split(', ')
    Oh_Auto = ability_list_dict['Oh_Auto'].strip('][').split(', ')
    Adrenaline_Renewal = ability_list_dict['Adrenaline_Renewal'].strip('][').split(', ')
    Energising = ability_list_dict['Energising'].strip('][').split(', ')
    Jaws1 = ability_list_dict['Jaws1'].strip('][').split(', ')
    Jaws2 = ability_list_dict['Jaws2'].strip('][').split(', ')
    Jaws3 = ability_list_dict['Jaws3'].strip('][').split(', ')
    Jaws4 = ability_list_dict['Jaws4'].strip('][').split(', ')
    Jaws5 = ability_list_dict['Jaws5'].strip('][').split(', ')
    V2 = ability_list_dict['V2'].strip('][').split(', ')

    # Final, Clean Dictionary
    Ability_Class_Dict = {'Basic': basic_list, "Threshold": Threshold_list, "Ultimate": Ultimate_list, "Igneous": Igneous_list, "2h_Auto": Twohanded_Auto,
                          "Mh_Auto:": Mh_Auto, "Oh_Auto":Oh_Auto, "Adrenaline_Renewal": Adrenaline_Renewal, "Energising": Energising,
                          "Jaws1": Jaws1,"Jaws2": Jaws2,"Jaws3": Jaws3, "Jaws4": Jaws4,"Jaws5": Jaws5, "V2":V2}


    return(Ability_Class_Dict)
def ClassifyRotation(input_rotation):
    Ability_Class_Scanner = [ ]
    Ability_Classifiers = [ ]
    for ability in input_rotation[0]:
        for key, value in TextReader().items():
            for ability_1 in value:
                if ability.lower().__contains__(ability_1.lower()):
                    Ability_Classifiers.append(key)
        Ability_Class_Scanner.append(Ability_Classifiers.copy())
        Ability_Classifiers.clear()
    Ability_Class_Scanner.pop(-1)
    return [Ability_Class_Scanner , input_rotation[1], input_rotation[2]]

def AcquireRotation():
    # Reads a rotation, saves it as a text
    check = True
    rotationText = []
    print("Enter in your rotation, make sure to spell things correctly. Refer to Ability_Class.txt, Type Done or done when you're finished")
    print("Adren rules: Basics 8%, Thresholds -15%, Ultimates -80%, 2h auto 3%, mh 2%, oh 1%, Energising is Rank 4")
    print("See Ability_Class.txt. Format for Jaws: Jaws#_Ability, Format for Energising: Energising_Ability. V2 for Vestments2. Order should not matter.")
    adren = min(max(float(input("Starting adren? ")),0),130)
    max_adren = float(input("Total Adren? "))
    while max_adren < 100 or max_adren > 130 or max_adren < adren:
        max_adren = float(input("Re-enter Total Adren; cannot be under 100, greater than 130, or less than your starting adren: "))
    counter = 0
    while check:
        ability_entry = input("Enter Ability " + str(counter) + ": ").strip()
        ability_entry.lower()
        if ability_entry == "Done" or ability_entry == 'done':
            check = False
        rotationText.append(ability_entry.replace('"', ''))
        counter += 1
    y = open('C:\\Users\\jjsun\\OneDrive\\Documents\\PycharmProjects\\Runescape\\Rotation.txt', 'w')
    y.write(str(rotationText))
    print(rotationText)
    y.close()

    # Opens rotation, inputs it.
    text = open('Rotation.txt')
    Ability_rotation_1 = text.read()
    Ability_rotation = Ability_rotation_1.strip('][').split(', ')
    text.close()
    for i in range(len(Ability_rotation)):
        Ability_rotation[i] = Ability_rotation[i].replace("'", "")
    print("Your Rotation: " + str(Ability_rotation))
    WritetoCSV(Ability_rotation)
    return [Ability_rotation, adren, max_adren]

def WritetoCSV(Ability_rotation):
    # Appends current CSV with rotation
    # Prompts user to write CSV or ignore
    write_to_csv = input("Write to CSV? Y or N: ")
    if write_to_csv == "Y" or "y":
        row_names = []
        for i in range(len(Ability_rotation)):
            row_names.append("Ability: "+str(i))
        with open('Rotation_CSV.csv', 'a') as f:
            write = csv.writer(f)
            write.writerow(row_names)
            write.writerow(Ability_rotation)
            f.close()

def main():
   CalculateAdren(ClassifyRotation(AcquireRotation()))
main()
