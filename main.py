from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

fname = input('Enter Your First Name: ').strip().title()
mname = input('Enter Your Middle Name: ').strip().title()
lname = input('Enter Your Last Name: ').strip().title()
name = ' '.join([lname, fname, mname])
cl = input('Enter Class in short(Eg. CO-III-E): ').strip().upper()
en = input('Enter Enrollment Number: ').strip()
sub = input('Enter Full Subject Name(Eg. Python For Datascience 3150713): ').strip().title()
dt = input('Enter Date of Submission(dd/mm/yyyy): ').strip()

img = Image.open('file_certi_template.png')
draw = ImageDraw.Draw(img)
selectFont = ImageFont.truetype('arial.ttf', size=48)

ns = 442
ne = 1440
w, h = selectFont.getsize(name)
draw.text((ns + (ne - ns - w) // 2, 900), name, (0, 0, 0), font=selectFont)

cs = 260
ce = 540
w, h = selectFont.getsize(cl)
draw.text((cs + (ce - cs - w) // 2, 1012), cl, (0, 0, 0), font=selectFont)

es = 890
ee = 1440
w, h = selectFont.getsize(en)
draw.text((es + (ee - es - w) // 2, 1010), en, (0, 0, 0), font=selectFont)

ss = 258
se = 1340
w, h = selectFont.getsize(sub)
draw.text((ss + (se - ss - w) // 2, 1346), sub, (0, 0, 0), font=selectFont)

draw.text((740, 1457), 'November', (0, 0, 0), font=selectFont)
draw.text((1176, 1455), '20', (0, 0, 0), font=selectFont)
draw.text((1325, 1455), '21', (0, 0, 0), font=selectFont)

draw.text((350, 1569), dt, (0, 0, 0), font=selectFont)

img.save('{} file certificate.png'.format(sub), 'PNG', resolution=100.0)
print('Your certificate will be available in the project directory !')