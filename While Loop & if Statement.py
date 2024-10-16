''' CHOLESTOROL CHECKUP PROGRAM'''

'''          LDL      HDL     TRI      result 
    Good    <100      >60     <150      <200
    BLine  100-130   50-60   150-200   200-240
    Bad     >130      <50      >200      >240'''

while True:
    HDL = int(input(" Enter the amount of HDL:_ "))
    LDL = int(input(" Enter the amount of LDL:_ "))
    TRI = int(input(" Enter the amount of Triglyceride:_ "))
    result = HDL + LDL + (TRI/5)
    if HDL<60 and LDL < 100 and TRI < 150 and result < 200:
        print('Cholesterol looks good! It is ', result)
    elif result > 240:
        print("Warning: Cholesterol looks bad! It is " , result)
    else:
        print('Border line!! BE CAREFUL! It is ' , result)
    break

