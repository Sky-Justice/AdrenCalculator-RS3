def CalculateAdren(identified_rotation):
    # Calculates Finishing Adrenaline (Primitive method)
    adren = min(max(float(input("Starting adren? ")),0),100)
    for ability_class in identified_rotation:
        if ability_class == 'Basic':
            adren = min(adren + 8, 100)
        elif ability_class =='Threshold':
            adren = max(min(adren - 15, 100),0)
        elif ability_class =='Ultimate':
            adren = max(min(adren - 80, 100), 0)
        elif ability_class == 'Igneous_overpower':
            adren = max(min(adren - 60, 100), 0)
        elif ability_class == '2h auto':
            adren = min(adren + 3, 100)
        elif ability_class == 'Dw auto':
            adren = min(adren + 2, 100)
        elif ability_class == "Oh auto":
            adren = min(adren + 1, 100)
        elif ability_class == "Adrenaline_Renewal":
            adren = min(adren + 40, 100)
    print("Remaining Adren: " + str(adren))
    return adren
    
    #advanced adren calc method
    # We take a textfile from YarB and check for Jaws?
        # Textfile [one list of all the toggles]
        # [second list of rotation presumably]
            # Trim out ~, -,
    # Adren Save (vigour): Conditionals?
    # Adren generators: FoTs, Natty, Jaws, Divert, Energizing, Inspiration
def TextReader():
    # Opens up textfile of abilities,
    textfile = open("Ability_class_melee.txt")
    ability_class_melee_text = textfile.read()
    ability_list = ability_class_melee_text.split('\n\n')
    ability_list_dict = {"Basic": ability_list[0], "Threshold": ability_list[1], "Ultimate": ability_list[2], "Igneous": ability_list[3], "Auto_Attack": ability_list[4], "Adrenaline_Renewal": ability_list[5]}

    # Converts into workable lists, creates dictionary?
    basic_list = ability_list_dict['Basic'].strip('][').split(', ')
    Threshold_list = ability_list_dict['Threshold'].strip('][').split(', ')
    Ultimate_list = ability_list_dict['Ultimate'].strip('][').split(', ')
    Igneous_list = ability_list_dict['Igneous'].strip('][').split(', ')
    Auto_Attack_list = ability_list_dict['Auto_Attack'].strip('][').split(', ')
    Potion_list = ability_list_dict['Adrenaline_Renewal'].strip('][').split(', ')
    Ability_Class_Dict = {'Basic': basic_list, "Threshold": Threshold_list, "Ultimate": Ultimate_list, "Igneous": Igneous_list, "Auto_Attack": Auto_Attack_list, "Adrenaline_Renewal": Potion_list}
    return(Ability_Class_Dict)

def ClassifyRotation(Ability_rotation):
    Ability_Class_Scanner = [ ]
    print("Your Rotation: " + str(Ability_rotation))
    for ability in Ability_rotation:
        for key, value in TextReader().items():
            for ability_1 in value:
                if ability_1.lower() == ability.lower():
                    Ability_Class_Scanner.append(key)
    return(Ability_Class_Scanner)
def AcquireRotation():
    # Reads a rotation, saves it as a text
    check = True
    rotationText = []
    print("Enter in your rotation, make sure to spell things correctly.")
    counter = 0
    while check:
        ability_entry = input("Enter Ability " + str(counter) + ": ")
        if ability_entry == "Done" or ability_entry == 'done':
            check = False
        rotationText.append(ability_entry.replace('"', ''))
        counter += 1
    y = open('C:\\Users\\jjsun\\PycharmProjects\\Runescape\\Rotation.txt', 'w')
    y.write(str(rotationText))
    y.close()

    # Opens rotation, inputs it.
    text = open('Rotation.txt')
    Ability_rotation_1 = text.read()
    Ability_rotation = Ability_rotation_1.strip('][').split(', ')
    text.close()
    for i in range(len(Ability_rotation)):
        Ability_rotation[i] = Ability_rotation[i].replace("'", "")
    return Ability_rotation
def main():

    CalculateAdren(ClassifyRotation(AcquireRotation()))

main()