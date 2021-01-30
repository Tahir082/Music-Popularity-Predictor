import pandas as pd
import statistics
import csv
import numpy as np

def true_probability(col_name, value, check_value):
    value_len=len(value)
    this_list=df[col_name].tolist()
    pos=0
    neg=0
    for m in range(0, col_size):
        if(this_list[m]==check_value and target_list[m]==1):
            pos=pos+1

    tp=pos/total_true
    return tp


def false_probability(col_name, value, check_value):
    value_len=len(value)
    this_list=df[col_name].tolist()
    pos=0
    neg=0
    for m in range(0, col_size):
        if(this_list[m]==check_value and target_list[m]==0):
            neg=neg+1

    fp=neg/total_false
    return fp


def calculate_unique(check_col):
    this_list=df[check_col].tolist()
    unique_values=np.array(this_list)
    unique=np.unique(unique_values)
    unique_len=len(unique)
    return unique


def naive_bayes(nodes, p_pos, p_neg):
    test_col_list=nodes
    df3=pd.read_csv("test.csv", usecols=test_col_list)
    a_list=df3[test_col_list[2]].tolist()
    len_test_list=len(a_list)
    check_node_len=len(test_col_list)
    tp_check_list=[]
    fp_check_list=[]
    song_target_val=[]
    test_target_list=[]

    for a in range(0, len_test_list):
        true_prob=1
        false_prob=1
        for i in range(0, check_node_len):
            if(test_col_list[i]=='DURATION'):
                check='DURATION'
                value=calculate_unique(check)
                len_of_unique=len(value)
                check_list=df3[test_col_list[i]].tolist()
                check_value=check_list[a]
                tp=true_probability(check, value, check_value)
                fp=false_probability(check, value, check_value)


            elif(test_col_list[i]=='Genre'):
                check='Genre'
                value=calculate_unique(check)
                len_of_unique=len(value)
                check_list=df3[test_col_list[i]].tolist()
                check_value=check_list[a]
                tp=true_probability(check, value, check_value)
                fp=false_probability(check, value, check_value)

            elif(test_col_list[i]=='Acousticness'):
                check='Acousticness'
                value=calculate_unique(check)
                len_of_unique=len(value)
                check_list=df3[test_col_list[i]].tolist()
                check_value=check_list[a]
                tp=true_probability(check, value, check_value)
                fp=false_probability(check, value, check_value)

            elif(test_col_list[i]=='Loudness'):
                check='Loudness'
                value=calculate_unique(check)
                len_of_unique=len(value)
                check_list=df3[test_col_list[i]].tolist()
                check_value=check_list[a]
                tp=true_probability(check, value, check_value)
                fp=false_probability(check, value, check_value)

            elif(test_col_list[i]=='Liveness'):
                check='Liveness'
                value=calculate_unique(check)
                len_of_unique=len(value)
                check_list=df3[test_col_list[i]].tolist()
                check_value=check_list[a]
                tp=true_probability(check, value, check_value)
                fp=false_probability(check, value, check_value)

            elif(test_col_list[i]=='Instrumentality'):
                check='Instrumentality'
                value=calculate_unique(check)
                len_of_unique=len(value)
                check_list=df3[test_col_list[i]].tolist()
                check_value=check_list[a]
                tp=true_probability(check, value, check_value)
                fp=false_probability(check, value, check_value)

            elif(test_col_list[i]=='Energy'):
                check='Energy'
                value=calculate_unique(check)
                len_of_unique=len(value)
                check_list=df3[test_col_list[i]].tolist()
                check_value=check_list[a]
                tp=true_probability(check, value, check_value)
                fp=false_probability(check, value, check_value)

            elif(test_col_list[i]=='Tempo'):
                check='Tempo'
                value=calculate_unique(check)
                len_of_unique=len(value)
                check_list=df3[test_col_list[i]].tolist()
                check_value=check_list[a]
                tp=true_probability(check, value, check_value)
                fp=false_probability(check, value, check_value)

            else:
                check='Rating'
                value=calculate_unique(check)
                len_of_unique=len(value)
                check_list=df3[test_col_list[i]].tolist()
                check_value=check_list[a]
                tp=true_probability(check, value, check_value)
                fp=false_probability(check, value, check_value)

            true_prob=true_prob*tp
            false_prob=false_prob*fp
        insert_tp=true_prob*p_true
        insert_fp=false_prob*p_false
        tp_check_list.append("{:.5f}".format(insert_tp))
        fp_check_list.append("{:.5f}".format(insert_fp))
    print("\n\n\n")
    print("\n Check List of True Probability: ",tp_check_list)
    print("\n Check List of False Probability: ",fp_check_list)
    target_value=0
    for g in range(0, len_test_list):
        if(tp_check_list[g]>fp_check_list[g]):
            target_value=1
            test_target_list.append(target_value)
        else:
            target_value=0
            test_target_list.append(target_value)

    print("\n\n\n Analyzing the data given in test.csv file: \n")
    for u in range(0, len_test_list):
        print(" For Song", u+1, "Target Value is:", test_target_list[u])

    print("\n\n 1= Can be a Popular Song\n 0= Can be a flop")

    len_target_test= len(test_target_list)
    counter=0
    for q in range (0, len_target_test):
        if(test_target_list[q]==1 and target_list[q]==1):
            counter=counter+1
        elif(test_target_list[q]==0 and target_list[q]==0):
            counter=counter+1

    accuracy=(counter/q)*100
    print("\n\n Program accuracy: ", "{:.2f}".format(accuracy),"%\n\n\n\n")

def get_gini(column):
    mylist=df[column].tolist()
    uv=np.array(mylist)
    values=np.unique(uv)
    print("\n For Column: ", column)
    print(values)
    values_len=len(values)
    gini_this_col=0
    for y in range(0, values_len):
        p=0
        n=0
        total_found=0
        check=values[y]
        for i in range(0, col_size):
            if(mylist[i]==check and target_list[i]==1):
                p=p+1
            elif(mylist[i]==check and target_list[i]==0):
                n=n+1
        print(" ", values[y],": ", "T=",p, "and F=",n)
        total_found=p+n
        gini_val=1-(((p/total_found)**2)+((n/total_found)**2))
        gini_this_col=gini_this_col+(gini_val*total_found)

    gini=gini_this_col/col_size
    print(" Gini index for column:", column, "= ", "{:.4f}".format(gini))
    return gini

col_list=["DURATION","Genre","Acousticness","Loudness","Liveness","Instrumentality","Energy","Tempo","Rating", "Target"]
col_list_wt=["DURATION","Genre","Acousticness","Loudness","Liveness","Instrumentality","Energy","Tempo","Rating"]
df=pd.read_csv("train_data.csv", usecols=col_list)
print("\n\n Features that are in the train data: \n ", col_list_wt)
duration_list = df['DURATION'].tolist()
genre_list = df['Genre'].tolist()
acous_list = df['Acousticness'].tolist()
loudness_list = df['Loudness'].tolist()
liveness_list = df['Liveness'].tolist()
ins_list = df['Instrumentality'].tolist()
energy_list = df['Energy'].tolist()
tempo_list = df['Tempo'].tolist()
rating_list = df['Rating'].tolist()
target_list = df['Target'].tolist()
col_size=len(duration_list)
columns=[]
columns.append(acous_list)
columns.append(loudness_list)
columns.append(liveness_list)
columns.append(ins_list)
columns.append(energy_list)
columns.append(tempo_list)
gini_index=[]
get_len= len(col_list_wt)
for i in range(0, get_len):
    if(col_list_wt[i]=='DURATION'):
        col_name='DURATION'
        gini=get_gini(col_name)
        gini_index.append("{:.5f}".format(gini))
    elif(col_list_wt[i]=='Genre'):
        col_name='Genre'
        gini=get_gini(col_name)
        gini_index.append("{:.5f}".format(gini))
    elif(col_list_wt[i]=='Acousticness'):
        col_name='Acousticness'
        gini=get_gini(col_name)
        gini_index.append("{:.5f}".format(gini))
    elif(col_list_wt[i]=='Liveness'):
        col_name='Liveness'
        gini=get_gini(col_name)
        gini_index.append("{:.5f}".format(gini))
    elif(col_list_wt[i]=='Genre'):
        col_name='Genre'
        gini=get_gini(col_name)
        gini_index.append("{:.5f}".format(gini))
    elif(col_list_wt[i]=='Loudness'):
        col_name='Loudness'
        gini=get_gini(col_name)
        gini_index.append("{:.5f}".format(gini))
    elif(col_list_wt[i]=='Energy'):
        col_name='Energy'
        gini=get_gini(col_name)
        gini_index.append("{:.5f}".format(gini))
    elif(col_list_wt[i]=='Tempo'):
        col_name='Tempo'
        gini=get_gini(col_name)
        gini_index.append("{:.5f}".format(gini))
    elif(col_list_wt[i]=='Rating'):
        col_name='Rating'
        gini=get_gini(col_name)
        gini_index.append("{:.5f}".format(gini))
    else:
        col_name='Genre'
        gini=get_gini(col_name)
        gini_index.append("{:.5f}".format(gini))

gini_list=[]
gini_list=gini_index
print("\n\n Final Gini Index LIST: ", gini_list)
zipped_lists=list(zip(gini_list, col_list_wt))
sorted_zip=sorted(zipped_lists)
new_col_list = [element for _, element in sorted_zip]
gini_index.sort()
print("\n\n Final Sorted Gini Index LIST: ", gini_index)
print("\n\n\n  Resulting FEATURES by sorting Gini:")
print(new_col_list)
median_point= statistics.median(gini_index)
print("\n\n MEDIAN: ",median_point)
new_node_list=[]
k=0
while(gini_index[k]<=median_point):
    new_node_list.append(new_col_list[k])
    k=k+1

print("\n\n\n THESE FEATURES WILL BE TAKEN FOR CALCULATION Consequetively: ")
print(new_node_list)

p=0
n=0
for i in range(0,col_size):
    if(target_list[i]==1):
        p=p+1
    else:
        n=n+1
print("\n Total number of positive: ",p)
print("\n Total number of negative: ",n)
total_true=p
total_false=n
p_true= p/col_size
p_false= n/col_size

print("\n Probability of Postive: ", "{:.4f}".format(p_true))
print("\n Probability of Negative: ", "{:.4f}".format(p_false))

naive_bayes(new_node_list, p_true, p_false)
