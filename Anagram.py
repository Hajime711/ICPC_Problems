def checkAnagram(line1,line2):
    if len(line2)>len(line1):
        return 'not possible'
    #sort strings
    line1 = sorted(line1)
    line2 = sorted(line2)
    for i in range(0, len(line2)):
        if line2[i] not in line1:
          return 'Not Possible'
    return 'Possible'
case_no = int(input())
for i in range(case_no):
  line1 = input()
  line2 = input()
  #remove white spaces from both lines
  line1 = line1.replace(" ", "")
  line2 = line2.replace(" ", "")
  #check if these strings are anagram
  print(checkAnagram(line1,line2))