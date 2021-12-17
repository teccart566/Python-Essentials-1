T_s=int(input("Give me the start time hour:"))
T_b=int(input("Give me the start time minute:"))
T_h=int(input("Give me the duration in minutes:"))            
T_h=(T_s*60)+T_b+T_h
print("The finish time is: ",end="")
print(T_h//60,T_h%60,sep=" : ")           
