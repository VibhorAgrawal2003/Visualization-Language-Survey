import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def lend_plot(file):

    lend = file["How likely are you to lend money to a person belonging to a different linguistic group?"]

    very_often = 0
    often = 0
    sometimes = 0
    rarely = 0
    never = 0

    for ln in lend:
        if ln == "Very often":
            very_often += 1
        elif ln == "Often":
            often += 1
        elif ln == "Sometimes":
            sometimes += 1
        elif ln == "Rarely":
            rarely += 1
        elif ln == "Never":
            never += 1 

    lend_array = np.array([very_often, often, sometimes, rarely, never])
    labels = ["Very Often", "Often", "Sometimes", "Rarely", "Never"]

    plt.title("How often one lends money to someone who speaks a different language")
    plt.pie(lend_array, labels = labels, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 8})
    plt.show() 


def borrow_plot(file):

    borrow = file["How likely are you to ask someone from a different linguistic group to borrow money?"]

    very_often = 0
    often = 0
    sometimes = 0
    rarely = 0
    never = 0

    for bor in borrow:
        if bor == "Very often":
            very_often += 1
        elif bor == "Often":
            often += 1
        elif bor == "Sometimes":
            sometimes += 1
        elif bor == "Rarely":
            rarely += 1
        elif bor == "Never":
            never += 1  

    borrow_array = np.array([very_often, often, sometimes, rarely, never])
    labels = ["Very Often", "Often", "Sometimes", "Rarely", "Never"]

    plt.title("How often one borrows money from someone who speaks a different language")
    plt.pie(borrow_array, labels = labels, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 8})
    plt.show()            


def confidence_plot(file):
    data = {
        "medium" : file["Your medium of education for high school"],
        "confidence" : file["How confident are you in your ability to manage your finances?"]
        }

    #confidence levels
    ec = 0
    rc = 0
    oc = 0

    #number of people
    ep = 0
    rp = 0
    op = 0

    for i in range(len(data["confidence"])):
        if data["confidence"][i] == "Extremely confident":
            if "english" in data["medium"][i].lower():
                ec += 5
                ep += 1
            elif "regional" in data["medium"][i].lower():
                rc += 5
                rp += 1
            else:
                oc += 5
                op += 1

        elif data["confidence"][i] == "Quite confident":
            if "english" in data["medium"][i].lower():
                ec += 4
                ep += 1
            elif "regional" in data["medium"][i].lower():
                rc += 4
                rp += 1
            else:
                oc += 4
                op += 1


        if data["confidence"][i] == "Neutral":
            if "english" in data["medium"][i].lower():
                ec += 3
                ep += 1
            elif "regional" in data["medium"][i].lower():
                rc += 3
                rp += 1
            else:
                oc += 3
                op += 1


        if data["confidence"][i] == "Somewhat confident":
            if "english" in data["medium"][i].lower():
                ec += 2
                ep += 1
            elif "regional" in data["medium"][i].lower():
                rc += 2
                rp += 1
            else:
                oc += 2
                op += 1

        if data["confidence"][i] == "Not confident at all":
            if "english" in data["medium"][i].lower():
                ec += 1
                ep += 1
            elif "regional" in data["medium"][i].lower():
                rc += 1
                rp += 1
            else:
                oc += 1
                op += 1

    print("~~Frequency~~")
    print("English: confidence = " + str(ec) + ", people = " + str(ep))
    print("Regional: confidence = " + str(rc) + ", people = " + str(rp))
    print("Other: confidence = " + str(oc) + ", people = " + str(op))

    # percentages
    eper = (ec / (ep*4))*100
    rper = (rc / (rp*4))*100
    oper = (oc / (op*4))*100
    
    labels = ["English Medium", "Regional Language Medium", "Other Medium"]

    xval = [10, 40, 70]
    yval = [eper, rper, oper]
    colors = ['#FF5733', '#33FF57', '#3333FF']

    plt.title('Confidence in financial abilities for groups of different mediums of education')

    plt.bar(xval[0], yval[0], width=15, label = labels[0], color=colors[0])
    plt.bar(xval[1], yval[1], width=15, label = labels[1], color=colors[1])
    plt.bar(xval[2], yval[2], width=15, label = labels[2], color=colors[2])

    plt.xticks(xval, labels)

    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.show()



def english_plot(file):
    english = file["How often do you prefer English to read articles or watch videos related to finance, stock prices and the economy as opposed to other languages?"]

    very_often = 0
    often = 0
    sometimes = 0
    rarely = 0
    never = 0

    for eng in english:
        if eng == "Very often":
            very_often += 1
        elif eng == "Often":
            often += 1
        elif eng == "Sometimes":
            sometimes += 1
        elif eng == "Rarely":
            rarely += 1
        elif eng == "Never":
            never += 1  

    english_array = np.array([very_often, often, sometimes, rarely, never])
    labels = ["Very Often", "Often", "Sometimes", "Rarely", "Never"]

    plt.title("How often one prefers English to learn finance")
    plt.pie(english_array, labels = labels, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 8})
    plt.show()  

def motivation_plot(file):
    motivation = file["Do complex terms and financial jargon confuse you or demotivate you from learning about finance and the economy?"]

    very_often = 0
    often = 0
    sometimes = 0
    rarely = 0
    never = 0

    for motiv in motivation:
        if motiv == "Very often":
            very_often += 1
        elif motiv == "Often":
            often += 1
        elif motiv == "Sometimes":
            sometimes += 1
        elif motiv == "Rarely":
            rarely += 1
        elif motiv == "Never":
            never += 1

    motivation_array = np.array([very_often, often, sometimes, rarely, never])
    labels = ["Very Often", "Often", "Sometimes", "Rarely", "Never"]

    plt.title("How often financial jargon demotivates one from learning")
    plt.pie(motivation_array, labels = labels, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 8})
    plt.show()


def medium_of_education_plot(file):
    medium_of_education = file["Your medium of education for high school"]

    english = 0
    regional = 0
    other = 0

    for medium in medium_of_education:
        if medium == "English medium":
            english += 1
        elif medium == "Regional language":
            regional += 1
        elif medium == "Other":
            other += 1

    medium_of_education_array = np.array([english, regional, other])
    labels = ["English Medium", "Regional Language", "Other"]

    plt.title("Medium of Education for High School")
    plt.pie(medium_of_education_array, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 8})
    plt.legend(labels, loc = "best")
    plt.show()    


def languages_plot(file):
    languages = file["Primary language (for everyday communication)"]

    hindi = 0
    english = 0
    telugu = 0
    tamil = 0
    bhojpuri = 0
    haryanvi = 0

    for lang in languages:
        if "hindi" in lang.lower() and "english" in lang.lower():
            hindi += 1
            english += 1
        elif "hindi" in lang.lower():
            hindi += 1
        elif "english" in lang.lower():
            english += 1
        elif "telugu" in lang.lower():
            telugu += 1     
        elif "tamil" in lang.lower():
            tamil += 1                
        elif "bhojpuri" in lang.lower():
            bhojpuri += 1
        elif "haryanvi" in lang.lower():
            haryanvi += 1

    
    languages_array = np.array([hindi, english, telugu, tamil, bhojpuri, haryanvi])
    labels = ["Hindi", "English", "Telugu", "Tamil", "Bhojpuri", "Haryanvi"]

    plt.title("Primary languages for everyday communication")
    plt.pie(languages_array, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 8})
    plt.legend(labels, loc = "best")
    plt.show()


def academic_years_plot(file):
    academic_years = file["Academic Year"]

    first_year = 0
    second_year = 0
    third_year = 0
    fourth_year = 0
    fifth_year = 0

    for year in academic_years:
        if year == "First year student":
            first_year += 1
        elif year == "Second year student":
            second_year += 1
        elif year == "Third year student":
            third_year += 1
        elif year == "Fourth year student":
            fourth_year += 1
        elif year == "Fifth year student":
            fifth_year += 1

    academic_years_array = np.array([first_year, second_year, third_year, fourth_year, first_year])
    labels = ["First Year", "Second Year", "Third Year", "Fourth Year", "Fifth Year"]

    plt.title("Academic Years")
    plt.pie(academic_years_array, labels = labels, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 8})
    plt.show()



def age_plot(file):
    age = file["Age"]

    g18_20 = 0
    g21_23 = 0
    g24_26 = 0
    g27_above = 0

    for a in age:
        if a == "18 to 20":
            g18_20 += 1
        elif a == "21 to 23":
            g21_23 += 1
        elif a == "24 to 26":
            g24_26 += 1
        elif a == "27 and above":
            g27_above += 1

    age_array = np.array([g18_20, g21_23, g24_26, g27_above])
    labels = ["18 to 20", "21 to 23", "24 to 26", "27 and above"]

    plt.title("Age")
    plt.pie(age_array, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 8})
    plt.legend(labels, loc = "best")
    plt.show() 


def gender_plot(file):
    gender = file["Gender"]

    male = 0
    female = 0
    other = 0
    prefer_not_to_say = 0

    for gen in gender:
        if gen == "Male":
            male += 1
        elif gen == "Female":
            female += 1
        elif gen == "Other":
            other += 1
        elif gen == "Prefer Not To Say":
            prefer_not_to_say += 1

    gender_array = np.array([male, female, other, prefer_not_to_say])
    labels = ["Male", "Female", "Other", "Prefer Not To Say"]

    plt.title("Gender")
    plt.pie(gender_array, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 8})
    plt.legend(labels, loc = "best")
    plt.show() 



if __name__ == "__main__":
    file = pd.read_excel("responses.xlsx")

    while(True):
        print("~~~~~ Plot Menu ~~~~~")
        print("\nDemographic details:")
        print("Enter 1 for Gender")
        print("Enter 2 for Age")
        print("Enter 3 for Academic Years")
        print("Enter 4 for Primary Spoken Language")
        print("Enter 5 for Medium of Education")

        print("\nEmpirical Pie Charts")
        print("Enter 6 for Motivation levels")
        print("Enter 7 for English Preference")
        print("Enter 8 for Financial Self-Confidence")
        print("Enter 9 for Borrowing")
        print("Enter 10 for Lending")

        print("\nEnter 0 to exit")

        ch = int(input())

        plt.figure(figsize=(8, 6))

        if ch == 0:
            break

        elif ch == 1:
            gender_plot(file)
    
        elif ch == 2:
            age_plot(file)

        elif ch == 3:
            academic_years_plot(file)

        elif ch == 4:
            languages_plot(file)

        elif ch == 5:
            medium_of_education_plot(file)

        elif ch == 6:
            motivation_plot(file)

        elif ch == 7:
            english_plot(file)

        elif ch == 8:
            confidence_plot(file)

        elif ch == 9:
            borrow_plot(file)

        elif ch == 10:
            lend_plot(file)

        else:
            print("Try again!\n")