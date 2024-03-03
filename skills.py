import json

ACROBATICS = 'acrobatics'
ANIMAL_HANDLING = 'animal handling'
ARCANA = 'arcana'
ATHLETICS = 'athletics'
DECEPTION = 'deception'
HISTORY = 'history'
INSIGHT = 'insight'
INTIMIDATION = 'intimidation'
INVESTIGATION = 'investigation'
MEDICINE = 'medicine'
NATURE = 'nature'
PERCEPTION = 'perception'
PERFORMANCE = 'performance'
PERSUASION = 'persuasion'
RELIGION = 'religion'
SLEIGHT_OF_HAND = 'sleight of hand'
STEALTH = 'stealth'
SURVIVAL = 'survival'

STR = 'strength'
DEX = 'dexterity'
CON = 'constitution'
INT = 'intelligence'
WIS = 'wisdom'
CHA = 'charisma'

def main():
    skills = []
    skills.append(ACROBATICS)
    skills.append(ANIMAL_HANDLING)
    skills.append(ARCANA)
    skills.append(ATHLETICS)
    skills.append(DECEPTION)
    skills.append(HISTORY)
    skills.append(INSIGHT)
    skills.append(INTIMIDATION)
    skills.append(INVESTIGATION)
    skills.append(MEDICINE)
    skills.append(NATURE)
    skills.append(PERCEPTION)
    skills.append(PERFORMANCE)
    skills.append(PERSUASION)
    skills.append(RELIGION)
    skills.append(SLEIGHT_OF_HAND)
    skills.append(STEALTH)
    skills.append(SURVIVAL)


    final = []
    for skill in skills:
        s = dict()
        print(skill, end=": ")
        proficient = input ("Proficient >> ")

        if skill in [ATHLETICS]: attribute = STR
        elif skill in [ACROBATICS, SLEIGHT_OF_HAND, STEALTH]: attribute = DEX
        elif skill in [ARCANA, HISTORY, INVESTIGATION, NATURE, RELIGION]: attribute = INT
        elif attribute in [ANIMAL_HANDLING, INSIGHT, MEDICINE, PERCEPTION, SURVIVAL]: attribute = WIS
        elif attribute in [DECEPTION, INTIMIDATION, PERFORMANCE, PERSUASION]: attribute = CHA

        if proficient == 't': proficient = True
        else: proficient = False

        final.append({"name": skill, "attribute": attribute, "proficient": proficient })
    print(json.dumps(final))



main()