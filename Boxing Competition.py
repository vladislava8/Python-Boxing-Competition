#**********************  Boxing Competition.py  *********************
#
# Name: Vladislava Sicicorez
#
# Course: CSCI 1470
#
# Assignment: Homework #5
#
# Algorithm:
#   Get weight inputs
#   Create dictionary for weights
#   Declare variables that will represent weight categories
#   Check for values to meet the requirements (>0, not less than 51, not more than 64)
#   Update the dictionary with categories that are less than 51 and more than 64
#   Print dictionary of weights with new categories
#   Create tuple with number of weight  in each category exclusive of less than 51 and more than 64
#   Print number of weight in each category that meets the requirements
#   Update number of weigh in each catergory that meets the requiresnts according to given conditions
#   Print updated values of categories of weight
#   Calculate total weight exclusive of the weights that are not (less than 1, less than 51 and more than 64)
#   Remove all zero and non-qualified weights
#   Add total number of weights that meet the conditions
#   Find avereage weight by divinging total qualified weight by number of total qualified weights
#   Print average weight

#**********************************************************
weight = list(map(int, input('Enter weigth(s):\n').split(","))) #   Get weight inputs
print()
weight_dic ={                               #   Create dictionary for weights
    'Welterweight' : [ 61, 62, 63, 64 ],
    'Lightweigh' : [58, 59, 60],
    'Featherweight': [55,56,57],
    'Bantamweight': [51, 52, 53, 54],
 }
#   Declare variables that will represent weight categories
w = 0
l = 0
f = 0
b = 0
i = 0
while weight[i] >0: #   Check for values to meet the requirements (>0, not less than 51, not more than 64)
    if weight[i] in weight_dic['Welterweight']:
        w+=1
    elif weight[i] in weight_dic['Lightweigh']:
         l+=1
    elif weight[i] in weight_dic['Featherweight']:
        f+=1
    elif weight[i] in weight_dic['Bantamweight']:
        b+=1
    else: #   Update the dictionary with categories that are less than 51 and more than 64
        if weight[i]<51:
            weight_dic['Too Low'] = [weight[i]]
        elif weight[i]>64:
            weight_dic['Too High'] = [weight[i]]
        else:
            break
    i+=1
j = 0
#   Print dictionary of weights with new categories
for key, value in weight_dic.items():
    print (key, ':', value)
print()
#   Create tuple with number of weight  in each category exclusive of less than 51 and more than 64
category_totals = (w,l,f,b)
#   Print number of weight in each category that meets the requirements
print("Initial Categories (exclusive of Too High, Too Low and weight less than 1kg):")
print()
print ("Total in Welterweight category:{:d}".format(w))
print("Total in Lightweight category:{:d}".format(l))
print("Total in Featherweight catgory:{:d}".format(f))
print("Total in Bantamweight category:{:d}".format(b))
#   Update number of weigh in each catergory that meets the requiresnts according to given conditions
for j in range (len(category_totals)-1):
    if (b==1) and (f>=1):
        f+=1
        b-=1
    elif (f==1) and (l>=1):
        l+=1
        f-=1
    elif (l==1) and (w>=1):
        w+=1
        l-=1
    else:
        break
print()
#   Print updated values of categories of weight
print ("Updated Categories:\n")
if w>0:
    print ("Total in Welterweight category:{:d}".format(w))
if l>0:
    print("Total in Lightweight category:{:d}".format(l))
if f>0:
    print("Total in Featherweight catgory:{:d}".format(f))
if b>0:
    print("Total in Bantamweight category:{:d}".format(b))
k = 0
#Remove all zero and non-qualified weights
counted_weights = []
while (weight[k])>0:
    counted_weights.append(weight[k])
    k+=1
z = 0
while z in range (len(counted_weights)-1):
    if ((counted_weights[z])<51) or ((counted_weights[z])>64):
        counted_weights.pop(z)
        z+=1
    else:
        z+=1
#   Add total number of weights that meet the conditions
total_weight = sum(counted_weights)
#   Find avereage weight by divinging total qualified weight by number of total qualified weight
average = total_weight/(len(counted_weights))
print()
#   Print average weight
print ("Average weight: {:.2f} kg".format(average))









