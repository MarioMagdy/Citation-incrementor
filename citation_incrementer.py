import docx
import re

print("""Make sure you understand...
      this program is used to increament the citation meaning if you add more refereces to the start
      of the references list this will help you, you can count how many you will add and run this
      program on the latter one to add the amount to each number in each citation in it
      like if you will add 8 references you will need the referenece number 1 to be 9...
      -------------------------------------------------------------------------------------------------
      IMPORTANT
      this program finds only numbers between brackets like [3] or [21] or [2131]
      it won't work if [231 ] nor [1, 1] nor [123, 213] nor...

      it may remove the images -sorry- :(
      -------------------------------------------------------------------------------------------------
      """)


file = input("""File name?  \t Make sure it's in the same folder as the program and it's ".docx" \n""")
doc = docx.Document(file+".docx")
all_paras = doc.paragraphs
text = ''


amount = int(input("Amount to increament:\n"))

def fix(match):
    return str(int(match.group())+amount)

for para in all_paras:
    print(para.text)
    para.text = re.sub(r"(?<=\[)\d+(?=\])", fix, para.text)


doc.save(file+'increamented.docx')






