import re
import imgkit
def clearHTML(path):
   fr = open(path,'r')
   fHTML = fr.read()
   #loai bo header
   r= re.search('''<header.*>[\s\S\d\w\W]*<div xmlns="" id="idm92303861" style="display: none;" class="table-wrapper ">''',fHTML)
   #loai bo floot
   r1 = re.search('''<div xmlns="" style="height: 40.*[\s\S\d\w\W]*</div>''',fHTML)
   r2 = re.search('''<div class="clear"></div>
</div>
<span[\s\S\d\w\W]*<div xmlns="" id="idm92303861" style="display: none;" class="table-wrapper ">''',fHTML)
   
   if r:
      replace=r.group()
      fHTML=fHTML.replace(replace,"")
   if r1:
      replace=r1.group()
      fHTML=fHTML.replace(replace,"")
   if r2 :
      replace=r2.group()
      fHTML=fHTML.replace(replace,"")
   t = '''<span onclick="toggle('idm92303861');" class="button" style="margin-top: 20px">Hide</span><div class="clear"></div>'''
   fHTML = fHTML.replace(t,'')
   fw = open('''../html/nessus3.html''','w')
   fw.write(fHTML)
clearHTML('../html/nessus2.html')
imgkit.from_url('../html/nessus3.html','../img/img.png')
