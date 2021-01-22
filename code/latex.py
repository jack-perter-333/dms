import csv
import imgkit
def inputs(a):
    with open('latex/nessus3.csv', newline='',encoding="utf8") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
def output(str):
    pass
    return
def save():
    header = '''
⧹documentclass{article}
⧹usepackage{pythontex}
⧹begin{document}
'''
    loop='''
⧹end{document}
'''

    return
def main():
    pass
    return

path_wkthmltoimage = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltoimage.exe'
config = imgkit.config(wkhtmltoimage=path_wkthmltoimage)
imgkit.from_url('https://www.youtube.com','img.png',config=config)
