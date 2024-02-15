#-----------------------impotr librarys-------------------------------
import numpy as np
import matplotlib.pyplot as plt
import os , platform
from colorama import Fore
# -------------------------------BAnner --------------------------------------
plat = platform.uname()[0]
if plat == "Linux":
     os.system("clear")
else:
      os.system("cls")

def banner():
    font =f"""{Fore.CYAN} 

███████╗██╗  ██╗██████╗ ███████╗ ██████╗████████╗███████╗██████╗     ██╗   ██╗ █████╗ ██╗     ██╗   ██╗███████╗    
██╔════╝╚██╗██╔╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗    ██║   ██║██╔══██╗██║     ██║   ██║██╔════╝    
█████╗   ╚███╔╝ ██████╔╝█████╗  ██║        ██║   █████╗  ██║  ██║    ██║   ██║███████║██║     ██║   ██║█████╗      
██╔══╝   ██╔██╗ ██╔═══╝ ██╔══╝  ██║        ██║   ██╔══╝  ██║  ██║    ╚██╗ ██╔╝██╔══██║██║     ██║   ██║██╔══╝      
███████╗██╔╝ ██╗██║     ███████╗╚██████╗   ██║   ███████╗██████╔╝     ╚████╔╝ ██║  ██║███████╗╚██████╔╝███████╗    
╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝   ╚═╝   ╚══════╝╚═════╝       ╚═══╝  ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚══════╝

                                                craeted by Abolfazl ilka                                                                       
                                                                                                                                                                                                                                                                                                                                                             
"""
    print(font)

banner()
# -------------- input data by user Of the three methods -----------------------
show_data = input(Fore.LIGHTGREEN_EX + '[~]' + Fore.RED + 'Hello, do you enter the data manually or use the txt file or the default data? [ 1-manually , 2-txt file 3-default ] '+Fore.LIGHTGREEN_EX )

x = np.array([75,75,73,71,71,70,67,75,79,78,78,78,78,77,75,80,87,86,86,83,82,82,81,91])
data_user= []

# ----------------- check user input to add data -----------------
try:
    if show_data == "1":
        while True:
            value = input("Enter your data one by one and when finished type 'End'")
            if value == "End":
                break
            data_user.append(float(value))
        print(data_user)
    elif show_data == "2":
        with open('data.txt', 'r') as file:
            data_user = [float(line) for line in file]
    elif show_data == "3":
        data_user = x
    else:
        raise ValueError("Invalid input! Please enter 1, 2 or 3")
except Exception as e:
    print(f"{Fore.RED} An error occurred:", e)
    print(f"{Fore.BLUE} Using default data as a fallback.")
    data_user = x
# ---------- calculate means of data -----------
def calculate_mean(data):
    return sum(data) / len(data)
# ---------- calculate variance of data -----------
def calculate_variance(data):
    mean = calculate_mean(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return variance
# ---------- calculate std_dev of data -----------
def calculate_std_dev(variance):
    return variance ** 0.5
mean = calculate_mean(data_user)
variance = calculate_variance(data_user)
std_dev = calculate_std_dev(variance)
# --------- ask to user for draw plot ------------
draw = input(Fore.LIGHTGREEN_EX + '[~]' + Fore.RED + 'would you like draw plot ? Y/N  '+Fore.LIGHTGREEN_EX )
# --------- check user input  for draw plot ------------
if draw.upper() == 'Y':
    try:
        # draw histogam plot 
        plt.hist(data_user, bins='auto', color='skyblue', edgecolor='black')
        # calculate breaks of histogram plot
        breaks = np.histogram_bin_edges(data_user , bins='auto')
        # draw plygon plot
        plt.plot([min(breaks)] + [(breaks[i] + breaks[i + 1]) / 2 for i in range(len(breaks) - 1)] + [max(breaks)], [0] + np.histogram(data_user, bins=breaks)[0].tolist() + [0], linestyle='dashed', linewidth=1.75, color='green')
        # draw and show plots
        plt.show()
    except Exception as e:
        # manage error for user input
        print(f"{Fore.RED} An error occurred while drawing the chart:", e)

# --------- ask to user for draw normal plot ------------
draw_n = input(Fore.LIGHTGREEN_EX + '[~]' + Fore.RED + 'would you like draw normaliza  chart ? Y/N  '+Fore.LIGHTGREEN_EX )
# --------- check user input  for draw normal plot ------------
if draw_n.upper() == 'Y':
    try:
        # input by user for normal sample size
        size = int(input(Fore.LIGHTGREEN_EX + '[~]' + Fore.RED + 'Enter size normal :   '+Fore.LIGHTGREEN_EX ))
        # great normal data 
        data = np.random.normal(mean, std_dev, size)
        # calculate breaks of histogram plot
        breaks_n = np.histogram_bin_edges(data , bins='auto')
        # draw histogam plot
        plt.hist(data, bins='auto', color='skyblue', edgecolor='black')
        # draw plygon plot
        plt.plot([min(breaks_n)] + [(breaks_n[i] + breaks_n[i + 1]) / 2 for i in range(len(breaks_n) - 1)] + [max(breaks_n)], [0] + np.histogram(data, bins=breaks_n)[0].tolist() + [0], linestyle='dashed', linewidth=1.75, color='green')
        # show plots
        plt.show()
    except Exception as e:
        # manage error for user input
        print(f"{Fore.RED} An error occurred while drawing the chart:", e)

# --------- ask to user for draw sample averages plot ------------
draw_s = input(Fore.LIGHTGREEN_EX + '[~]' + Fore.RED + 'How many sample averages do you want to take?'+Fore.LIGHTGREEN_EX )
# --------- check user input  for draw sample averages plot ------------
if draw_s.upper() == 'Y':
    try:
        # input by user for sample averages size
        num_samples= int(input(Fore.LIGHTGREEN_EX + '[~]' + Fore.RED + 'Enter size sample averages :   '+Fore.LIGHTGREEN_EX ))
        # grat value for mean of samples
        sample_means = []

        for _ in range(num_samples):
            sample = np.random.choice(data_user, size=len(data_user), replace=True)
            sample_mean = calculate_mean(sample)
            sample_means.append(sample_mean)
        # draw histogam plot    
        plt.hist(sample_means, bins='auto', color='skyblue', edgecolor='black')
        # calculate breaks of histogram plot
        breaks_s = np.histogram_bin_edges(sample_means , bins='auto')
        # draw plygon plot
        plt.plot([min(breaks_s)] + [(breaks_s[i] + breaks_s[i + 1]) / 2 for i in range(len(breaks_s) - 1)] + [max(breaks_s)], [0] + np.histogram(sample_means, bins=breaks_s)[0].tolist() + [0], linestyle='dashed', linewidth=1.75, color='green')
        # calculate means of data
        mean_data = calculate_mean(sample_means)
        # draw means plot
        plt.axvline(int(mean_data), color='blue', linestyle='dashed', linewidth=2)
        # اضافه کردن متن به عنوان برچسب بالای نمودار
        textstr = '\n'.join(( r'Mean sample =%.2f' % (mean_data),r'Mean data =%.2f' % (mean)))
        # اضافه کردن متن به نمودار
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        plt.text(0.05, 0.95, textstr, transform=plt.gca().transAxes, fontsize=10 ,verticalalignment='top', bbox=props)
        # draw and show plots
        plt.show()
    except Exception as e:
        # manage error for user input
        print(f"{Fore.RED} An error occurred while drawing the chart:", e)
# ------------- enter to exit ----------
while True:
    # user can control code with 'Enter' key
    user_input = input("for exit click Enter : ")
    if user_input == "":
        break
#-------------- End ---------------

