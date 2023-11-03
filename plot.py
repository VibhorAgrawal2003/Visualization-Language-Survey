import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def confidence(file):
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
                ec += 4
                ep += 1
            elif "regional" in data["medium"][i].lower():
                rc += 4
                rp += 1
            else:
                oc += 4
                op += 1

        elif data["confidence"][i] == "Quite confident":
            if "english" in data["medium"][i].lower():
                ec += 3
                ep += 1
            elif "regional" in data["medium"][i].lower():
                rc += 3
                rp += 1
            else:
                oc += 3
                op += 1


        if data["confidence"][i] == "Neutral":
            if "english" in data["medium"][i].lower():
                ec += 2
                ep += 1
            elif "regional" in data["medium"][i].lower():
                rc += 2
                rp += 1
            else:
                oc += 2
                op += 1


        if data["confidence"][i] == "Somewhat confident":
            if "english" in data["medium"][i].lower():
                ec += 1
                ep += 1
            elif "regional" in data["medium"][i].lower():
                rc += 1
                rp += 1
            else:
                oc += 1
                op += 1

        if data["confidence"][i] == "Not confident at all":
            if "english" in data["medium"][i].lower():
                ec += 0
                ep += 1
            elif "regional" in data["medium"][i].lower():
                rc += 0
                rp += 1
            else:
                oc += 0
                op += 1

    print("~~Frequency~~")
    print("English: confidence = " + str(ec) + ", people = " + str(ep))
    print("Regional: confidence = " + str(rc) + ", people = " + str(rp))
    print("Other: confidence = " + str(oc) + ", people = " + str(op))

    # percentages
    eper = (ec / (ep*4))*100
    rper = (rc / (rp*4))*100
    oper = (oc / (op*4))*100
    
    xval = ["English Medium", "Regional Language", "Other"]
    yval = [eper, rper, oper]
    colors = ['#FF5733', '#33FF57', '#3333FF']

    plt.title('Confidence in financial abilities of different language speakers')

    plt.bar(10, yval[0], width=20, label = xval[0], color=colors[0])
    plt.bar(40, yval[1], width=20, label = xval[1], color=colors[1])
    plt.bar(70, yval[2], width=20, label = xval[2], color=colors[2])
    # plt.bar(xval, yval)
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

def languages_plot(file):
    languages = file["Primary language (for everyday communication)"]

    hindi = 0
    english = 0
    telugu = 0
    tamil = 0
    bhojpuri = 0
    haryanvi = 0

    for lang in languages:
        if "hindi" in lang.lower():
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
    plt.legend(labels, title = "Languages", loc = "upper right")
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


if __name__ == "__main__":
    file = pd.read_excel("responses.xlsx")

    while(True):
        print("Plot Menu")
        print("Enter 1 for academic years")
        print("Enter 2 for primary languages")
        print("Enter 3 for demotivation by jargon")
        print("Enter 4 for english preference")
        print("Enter 5 for financial self-confidence")
        print("Enter 7 for exit")

        ch = int(input())

        if ch == 1:
            academic_years_plot(file)
    
        elif ch == 2:
            languages_plot(file)

        elif ch == 3:
            motivation_plot(file)

        elif ch == 4:
            english_plot(file)

        elif ch == 5:
            confidence(file)

        elif ch == 7:
            break

        else:
            print("Try again!\n")