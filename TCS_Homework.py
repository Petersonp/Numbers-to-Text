#Formatting
def format(user_input,commas,length):
          user_input=("0"*(commas*3-length))
          return user_input

def group(commas,user_input):
          tmp = []
          s=''
          for i in range(commas*3):
                    s+=user_input[i]
                    if ((i+1)%3==0):
                              tmp.append(s)
                              s=''
                              
          return tmp

#Converting
def convert(user_input):
          length = len(user_input) 
          commas = (length//3)+(length%3>0)
          user_input = format(user_input,commas,length)+user_input
          li = []
          li = group(commas,user_input)
          to_words =''
          ref2 = {1:"",2:"libo ",3:"milyon ",4:"bilyon "}
          if (int(user_input)!=0):
                    for i in range(commas):
                               x = commas-i
                               tmp = ref2[x]
                               addon = place(li[i],x)
                               if (addon == ""):
                                         tmp = ("")
                               to_words+=(addon)+tmp
          return(to_words)
def place(group,i):
          ref = {'1':'isa','2':'dalawa','3':'tatlo','4':'apat','5':'lima','6':'anim','7':'pito','8':'walo','9':'siyam'}
          na = ['4','6','9']
          tmp = ''
          for x in range(3):
                    pos = group[x]
                    if pos == '0':
                              continue
                    digit = ref[pos]
                    #Hundreds
                    if (x == 0):
                              if (pos in na):
                                        tmp += (digit+" na daan ")
                              else:
                                        tmp += (digit+"ng daan ")
                    #Tens
                    elif (x == 1):
                              if (pos == '1'):
                                        if (group[x+1] == '0'):
                                                  tmp += ("sampung ")
                                                  break
                                        else:
                                                  tmp += (digit+" labing ")
                              elif (pos in na):
                                        tmp += (digit+" na pu ")
                              else:
                                        tmp += (digit+"ng pu ")
                    #Ones
                    elif (i>1):
                              if (pos in na):
                                        tmp += (digit+" na ")
                              else:
                                        tmp += (digit+"ng ")
                    else:
                              tmp += (digit)

          return tmp

def decimal(user_input1,user_input2):
          addon = "at "
          if (len(user_input1)==0 or (not('0') not in user_input1)):
                    addon = ""
          for i in range(2):
                    if(user_input2[i] != '0'):
                              x = user_input2+('0'*(2-len(user_input2)))
                              x=('0'*(3-len(x))+x)
                              return (addon+place(x,2)+"sentimo")
          
          return("")
          
          
          
                    
#Seperate
def seperate(user_input):
          if ('.' not in user_input):
                    user_input += ".00"
          tmp = []
          s=''
          for i in user_input:
                    if (i == '.'):
                              tmp.append(s)
                              s=''
                              continue
                    s+=i
          tmp.append(s)
          return tmp
                    
                    
while True:
          user_input = input("Magpasok ng isang numero: ")
          try:
                    test_input = float(user_input)
          except ValueError:
                    print("Hindi isang numero!")
                    continue
          else:
                    li = seperate((user_input))
                    if (len(li[1])>2):
                              print("Hindi isang numero!")
                              continue
                    elif ((len(li[0])>12)):
                              print("Masyadong malaki!")
                              continue
                    print(convert(li[0]),decimal(li[0],li[1]))
