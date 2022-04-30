# Program name: Strange_Spencer_FinalProject.py
# Author: Spencer Strange
# Date: 
# Summary: Calculate a variety of useful information regarding candle making. How much wax and fragrance oil for a project, based on potency of fragrance desited
# Variables: 
#   wax: dictionary for holding name, weight, gravity, of user specified wax
#   waxName: User defined name of wax (string)
#   waxWeight: User specified weight of wax being used (float)
#   gravityInq: Determining if there is a density that needs to be specified by the user (string)
#   gravity: Specific gravity of wax, used to calcuate how much wax is needed for specific project
   
# https://armatagecandlecompany.com/blog/wax-per-candle/ 
# https://armatagecandlecompany.com/blog/fragrance-oil-calculations/ 
# https://armatagecandlecompany.com/blog/specific-gravity/ 
# Desktop > candle-math.pdf

# Defining if ounces or grams
def main():

    weightType = str(input("Will you be using grams or ounces for your measurements? (Reminder to not use fluid ounces): "))
    while weightType.upper() != "GRAMS" and weightType.upper() != "OUNCES":
        weightType = str(input("ERROR... You have input an inproper weight type. Please enter a proper weight type: "))
    if weightType.upper() == "GRAMS":
        print("You have chosen grams.")
    if weightType.upper() == "OUNCES":
        print("You have chose ounces. Reminder to not use fluid ounces, as your measurments will not be accurate.")

# Defining wax dictionary and calculating specific gravity
    wax = {}
    waxName = str(input("Enter the name of the wax you will be calculating, or DONE when finished: "))
    while waxName.upper() != "DONE":
        specificGravityInq = str(input("Do you know the specific gravity of the wax you will be using? "))
        while specificGravityInq.upper() != "YES" and specificGravityInq.upper() != "NO":
            specificGravityInq = str(input("ERROR... You have input an inproper response. Please enter '"'Yes'"' or '"'No'"': "))
        if specificGravityInq.upper() == "YES":
            specificGravity = float(input("Great. Please enter the specific gravity within 2 signifigant digits: "))
        if specificGravityInq.upper() == "NO":
            print("No worries, we can calculate this for your specific wax, or we can assume the default. Calculating this specific information will make for the best products from your specific wax.")
            calculateInq = str(input("Would you like to calculate the specific gravity for your wax? "))
            while calculateInq.upper() != "YES" and calculateInq.upper() != "NO":
                calculateInq = str(input("ERROR... You have input an inproper response. Please enter '"'Yes'"' or '"'No'"': "))
            if calculateInq.upper() == "NO":
                print("Sounds good. We will set the specific gravity to the average.")
                specificGravity = float(0.86)
            if calculateInq.upper() == "YES":
                print("Sounds good. We will help you calculate this for your wax. You will need to be able to melt wax, measure volume, and measure weight.")
                print("For volume calculations, you will need to measure in mL or cups.")
                measurementInq = str(input("Will you be using cups or mL? "))
                while measurementInq.upper() != "CUPS" and measurementInq.upper() != "ML":
                    measurementInq = str(input("ERROR... You have input an inproper response. Please enter '"'cups'"' or '"'mL'"': "))
                if measurementInq.upper() == "CUPS":
                    volumeCups = float(input("Please enter the volume in cups: "))
                if measurementInq.upper() == "ML":
                    volumeML = float(input("Please enter the volume in mL: "))
                if weightType.upper() == "GRAMS":
                    meltWaxWeightG = float(input("Enter the weight of melted wax (not including weight of measuring container) in grams: "))
                else:
                    meltWaxWeightOz = float(input("Enter the weight of melted wax (not including weight of measuring container) in ounces: "))
                if weightType.upper() == "GRAMS" and measurementInq.upper() == "ML":
                    densityGramsMl = meltWaxWeightG / volumeML
                    specificGravity = densityGramsMl / 0.997
                    format_specificGravity = "{:.2f}".format(specificGravity)
                    print("The calculated specific gravity for your wax is", format_specificGravity )
                if weightType.upper() == "GRAMS" and measurementInq.upper() == "CUPS":
                    densityGramsCups = meltWaxWeightG / volumeCups
                    specificGravity = densityGramsCups / 235.88
                    format_specificGravity = "{:.2f}".format(specificGravity)
                    print("The calculated specific gravity for your wax is", format_specificGravity )
                if weightType.upper() == "OUNCES" and measurementInq.upper() == "ML":
                    densityOzML = meltWaxWeightOz / volumeML
                    specificGravity = densityOzML / 0.03517
                    format_specificGravity = "{:.2f}".format(specificGravity)
                    print("The calculated specific gravity for your wax is", format_specificGravity )
                if weightType.upper() == "OUNCES" and measurementInq.upper() == "CUPS":
                    densityOzCups = meltWaxWeightOz / volumeCups
                    specificGravity = densityOzCups / 8.32
                    format_specificGravity = "{:.2f}".format(specificGravity)
                    print("The calculated specific gravity for your wax is", format_specificGravity )
        wax[waxName] = specificGravity
        waxName = str(input("Enter the name of the next wax, or DONE when you are finished: "))

# Defining candle/melt container dictionary
    container = {}
    containerName = str(input("Enter the name of the container you'd like to define, or DONE when you're finished: "))
    while containerName.upper() != "DONE":
        meltOrCandle = str(input("Is this a wax melt or candle container? "))
        while meltOrCandle.upper() != "MELT" and meltOrCandle.upper() != "CANDLE":
            meltOrCandle = str(input("ERROR... You have entered an inproper response. Please respond with either '"'Melt'"' or '"'Candle'"': "))
        if meltOrCandle.upper() == "MELT" or meltOrCandle.upper() == "CANDLE":
            fragranceLoad = int(input("As a whole number between 3 and 12, please enter how strong you would like the product you are making to smell. "))
            while fragranceLoad > 12 or fragranceLoad < 3:
                fragranceLoad = int(input("ERROR... You have input an invalid number. Please enter a number between 3 and 12. "))
        print("Your previously defined measurement unit is", weightType)
        containerWeight = float(input("Measure the container while it is empty, and provide the weight in your previously defined unit: "))
        waterAndContWeight = float(input("Fill your container to the height you wish to fill it with wax. Include the container weight in your measurement. Provide this weight in your previously defined unit: "))
        waterWeight = waterAndContWeight - containerWeight
        totalWeight = waterWeight * specificGravity
        fragranceLoadPercent = fragranceLoad / 100
        waxWeight = totalWeight / (1 + fragranceLoadPercent)
        fragranceOil = totalWeight - waxWeight
        container[containerName] = meltOrCandle, totalWeight, waxWeight, fragranceOil 
        containterName = str(input("Enter the name of the next container you'd like to define, or DONE when you are finished: "))

        

# totalWeight = waterWeightOz/Gr * specificGravity

# waxWeight = totalWeight / (1 + fragranceLoad converted to percentage bewteen 3 and 12)

# totalWaxWeight = waxWeight * numberOfContainers
main()