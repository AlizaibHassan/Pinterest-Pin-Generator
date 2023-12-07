import urllib.request
import os
import pytesseract
import csv
import cv2
import numpy as np
import random
from PIL import Image , ImageEnhance , ImageFont, ImageDraw , ImageColor
import glob
import re



def change_brightness(img, value):
   hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
   h, s, v = cv2.split(hsv)
   v = cv2.add(v,value)
   v[v > 255] = 255
   v[v < 0] = 0
   final_hsv = cv2.merge((h, s, v))
   img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
   return img



cnt=0

file='pin/'
Text_titles = 'titles/titles_list.txt'

f = open(Text_titles, "r")
all_titles = f.readlines()
f.close()

bg_colors = 'titles/bg_colors.txt'

f = open(bg_colors, "r")
all_colors = f.readlines()
f.close()


images=glob.glob('bg/*.jpg')

fonts_list=glob.glob('fonts/*.ttf')

file1 = open("result.csv","w")

loc=os.path.dirname(__file__)
file_n = loc+'/pin/'

for image in images:

   image = cv2.imread(image)

   value=random.randint(-30, 30)
   image = change_brightness(image, value)


   font = fonts_list[random.randint(0, 5)]

   
   bg_color = all_colors[random.randint(0, 6)]

   bg_color = bg_color.rstrip('\n')


   path_to_save = file_n+str(cnt)+".jpg"
   towrite=path_to_save+','+all_titles[cnt]
   file1.writelines(towrite)


   res = len(all_titles[cnt].split())
   long_word = max(all_titles[cnt].split(), key=len)
   
   if res <= 1:

      #### overlay space
      rand_point = random.randint(20,200)
      x = rand_point 
      y = rand_point
      h = 90
      if len(long_word) > 9:
         w = 600
         rand_point = random.randint(20,150)
         x = rand_point 
         y = rand_point
      else:
         w=450

   elif res <= 2:

      #### overlay space
      rand_point = random.randint(20,200)
      x = rand_point 
      y = rand_point
      h = 120
      if len(long_word) > 9:
         w = 600
         rand_point = random.randint(20,150)
         x = rand_point 
         y = rand_point
      else:
         w=450
    
   elif res <= 3:

      #### overlay space
      rand_point = random.randint(20,190)
      x = rand_point 
      y = rand_point
      h = 150
      if len(long_word) > 9:
         w = 600
         rand_point = random.randint(20,150)
         x = rand_point 
         y = rand_point
      else:
         w=500


   
   elif res <= 4:
      #### overlay space
      rand_point = random.randint(20,190)
      x = rand_point 
      y = rand_point
      h = 190
      if len(long_word) > 9:
         w = 600
         rand_point = random.randint(20,150)
         x = rand_point 
         y = rand_point
      else:
         w=500
   
   elif res <= 5:
      #### overlay space (Alizaib Comment)
      rand_point = random.randint(20,190)
      x = rand_point 
      y = rand_point
      h = 280
      if len(long_word) > 9:
         w = 600
         rand_point = random.randint(20,150)
         x = rand_point 
         y = rand_point
      else:
         w=500


   elif res <= 6:
      #### overlay space
      rand_point = random.randint(20,190)
      x = rand_point 
      y = rand_point
      h = 250
      if len(long_word) > 9:
         w = 600
         rand_point = random.randint(20,150)
         x = rand_point 
         y = rand_point
      else:
         w=500

   elif res <= 7:
      #### overlay space
      rand_point = random.randint(20,190)
      x = rand_point 
      y = rand_point
      h = 250
      if len(long_word) > 9:
         w = 600
         rand_point = random.randint(20,150)
         x = rand_point 
         y = rand_point
      else:
         w=500

   elif res <= 8:
      #### overlay space
      rand_point = random.randint(20,190)
      x = rand_point 
      y = rand_point
      h = 250
      if len(long_word) > 9:
         w = 600
         rand_point = random.randint(20,150)
         x = rand_point 
         y = rand_point
      else:
         w=500

   elif res <= 9:
      #### overlay space
      rand_point = random.randint(20,190)
      x = rand_point 
      y = rand_point
      h = 300
      if len(long_word) > 9:
         w = 600
         rand_point = random.randint(20,150)
         x = rand_point 
         y = rand_point
      else:
         w=500
   
   elif res <= 10:
      #### overlay space
      rand_point = random.randint(20,190)
      x = rand_point 
      y = rand_point
      h = 300
      if len(long_word) > 9:
         w = 600
         rand_point = random.randint(20,150)
         x = rand_point 
         y = rand_point
      else:
         w=500

   elif res <= 11:
      #### overlay space
      rand_point = random.randint(20,190)
      x = rand_point 
      y = rand_point
      h = 300
      if len(long_word) > 9:
         w = 600
         rand_point = random.randint(20,150)
         x = rand_point 
         y = rand_point
      else:
         w=500
   
   elif res <= 12:
      #### overlay space
      rand_point = random.randint(20,190)
      x = rand_point 
      y = rand_point
      h = 330
      if len(long_word) > 9:
         w = 600
         rand_point = random.randint(20,150)
         x = rand_point 
         y = rand_point
      else:
         w=500

   elif res <= 13:
      #### overlay space
      rand_point = random.randint(20,190)
      x = rand_point 
      y = rand_point
      h = 350
      if len(long_word) > 9:
         w = 600
         rand_point = random.randint(20,150)
         x = rand_point 
         y = rand_point
      else:
         w=500
  

   elif res > 14:
      continue



   #### alpha, the 4th channel of the image
   alpha = random.uniform(0.5, 0.7)

   overlay = image.copy()
   output = image.copy()


   RGB_Color = ImageColor.getcolor(bg_color, "RGB")

   #bluring The Background Images
   blur_value=random.randint(1, 3)
   overlay = cv2.blur(overlay,(blur_value,blur_value))


   ##### corner
   cv2.rectangle(overlay, (x, x), (x + w, y+ h), RGB_Color, -1)




   ##### putText
   #cv2.putText(overlay, "HELLO WORLD..", (x + int(w/10),y + int(h/1.5)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)

   # Convert the image to RGB (OpenCV uses BGR)  
   cv2_im_rgb = cv2.cvtColor(overlay,cv2.COLOR_BGR2RGB)
   # Pass the image to PIL 
   pil_im = Image.fromarray(cv2_im_rgb)
   draw = ImageDraw.Draw(pil_im)
  


   font_size = 46
   font = ImageFont.truetype(font, font_size)


   
   all_titles[cnt] = re.sub(r"[^a-zA-Z0-9\s\.\-]",'',all_titles[cnt])
   

   #all_titles[cnt] = all_titles[cnt].replace(' ' , '\n')

   

   #all_titles[cnt] = re.sub(r'([a-zA-Z]{8,}?)\s', r'\1\n',all_titles[cnt])

   #all_titles[cnt] = re.sub(r'([a-zA-Z]{8,}.[a-zA-Z0-9]{3}?)\s', r'\1\n',all_titles[cnt]) (Alizaib Commented)


   
   all_titles[cnt] = re.sub(r'([a-z|\s|A-Z|\s|0-9|.(a-z-A-Z-0-9){3}]{10,}?)\s', r'\1\n',all_titles[cnt])


  # all_titles[cnt] = re.sub(r'([a-z\sA-Z]{9,10}?)\s', r'\1\n',all_titles[cnt])
  
   #all_titles[cnt] = re.sub(r'(\s\S*?)\s', r'\1\n ',all_titles[cnt])


   #removing spaces at start of line
   all_titles[cnt] = re.sub(r'(^\s+)', r'\1'' ',all_titles[cnt])

   print(all_titles[cnt])

   draw.text((x + int(w/10),y + int(h/20)), all_titles[cnt], font=font)
   
   # Get back the image to OpenCV
   overlay = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)

   #### apply the overlay
   cv2.addWeighted(overlay, alpha, output, 1 - alpha,0, output)



   cv2.rectangle(overlay, (10, 860), (220 + 30, 890 + 27), (0,0,0), -1)
   cv2.putText(overlay, 'www.gartenleidenschaft.de', (30,885), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255,255,255), 1, cv2.LINE_AA) 
   cv2.addWeighted(overlay, alpha, output, 1 - alpha,0, output)

   scale_percent = 166.7 # percent of original size
   width = int(overlay.shape[1] * scale_percent / 100)
   height = int(overlay.shape[0] * scale_percent / 100)
   dim = (width, height)
   print(dim)
  
   # resize image
   output = cv2.resize(overlay, dim, interpolation = cv2.INTER_AREA)
 

   path_to_save = file+str(cnt)+".jpg"
   cv2.imwrite(path_to_save, output)




   cnt+=1

file1.close()
