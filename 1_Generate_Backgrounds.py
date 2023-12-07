import urllib.request
import os
import pytesseract
import csv
from PIL import Image



filepath = 'input/urls.txt'
saveimg = 'saveimg/'
basedata=open(filepath).read()
file='bg/'
sizefixed='sizefixed/'

def download_img(image_url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',} 
    request=urllib.request.Request(image_url,None,headers)
    response = urllib.request.urlopen(request)
    #install PIL package to convert the response into a PIL Image object to further save it (Alizaib Comments)
    image=Image.open(response)
    image.save(full_path)
    pass



with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   cnt2 = 1
   while line:
       
       line = line.rstrip('\n')

       print(cnt)
       print(line)
       
       img_name=str(cnt)
       fullfileurl = os.path.join(saveimg, str(cnt)+".jpg")
#       urllib.request.urlretrieve(line, fullfileurl)

       download_img(line,saveimg,img_name)
       pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
       checkdata=pytesseract.image_to_string(fullfileurl)

       resizing = Image.open(fullfileurl)
       
       rwidth, rheight = resizing.size

       # if rwidth < 600 or rheight < 900:
       #    new_image = resizing.resize((1920, 1080))
       #    new_image.save(fullfileurl)


       im = Image.open(fullfileurl)

       width, height = im.size 

       
       standard_width = 600
       standard_height = 900
       wideflow = 0
       highflow = 0

       condition_width = width-standard_width
       condition_height = height-standard_height
       
       print(width)
       print(height)

       if width > 600 and height > 900 and width < 1000 and height < 1500:
    
          while wideflow < condition_width:
             im1 = im.crop((wideflow,highflow,standard_width,standard_height)) 
             im1.save(file+str(cnt)+str(cnt2)+".jpg", "JPEG")
             cnt2+=1
             highflow=highflow+150
             standard_height=standard_height+150
             
             while highflow < condition_height:
                im1 = im.crop((wideflow,highflow,standard_width,standard_height)) 
                im1.save(file+str(cnt)+str(cnt2)+".jpg", "JPEG")
                cnt2+=1
                highflow=highflow+150
                standard_height=standard_height+150

             highflow=0
             standard_height=900 
             cnt2 +=1
             wideflow=wideflow + 150
             standard_width = standard_width + 150



       standard_width = 1000
       standard_height = 1500
       wideflow = 0
       highflow = 0

       condition_width = width-standard_width
       condition_height = height-standard_height
       already_checked=False
       
       if width > 1000 and height > 1500:
    
          while wideflow < condition_width:
             im1 = im.crop((wideflow,highflow,standard_width,standard_height)) 
             im1.save(file+str(cnt)+str(cnt2)+".jpg", "JPEG")
             cnt2+=1
             highflow=highflow+150
             standard_height=standard_height+150
             
             while highflow < condition_height:
                im1 = im.crop((wideflow,highflow,standard_width,standard_height)) 
                im1.save(file+str(cnt)+str(cnt2)+".jpg", "JPEG")
                cnt2+=1
                highflow=highflow+150
                standard_height=standard_height+150

             highflow=0
             standard_height=1500
             cnt2 +=1
             wideflow=wideflow + 150
             standard_width = standard_width + 150
             already_checked=True

       
       standard_width = 600
       standard_height = 900
       wideflow = 0
       highflow = 0

       condition_width = width-standard_width
       condition_height = height-standard_height

       if width > 600 and height > 900 and already_checked==False:
    
          while wideflow < condition_width:
             im1 = im.crop((wideflow,highflow,standard_width,standard_height)) 
             im1.save(file+str(cnt)+str(cnt2)+".jpg", "JPEG")
             cnt2+=1
             highflow=highflow+150
             standard_height=standard_height+150
             
             while highflow < condition_height:
                im1 = im.crop((wideflow,highflow,standard_width,standard_height)) 
                im1.save(file+str(cnt)+str(cnt2)+".jpg", "JPEG")
                cnt2+=1
                highflow=highflow+150
                standard_height=standard_height+150

             highflow=0
             standard_height=900 
             cnt2 +=1
             wideflow=wideflow + 150
             standard_width = standard_width + 150




       if width < 600 and heigh < 900:
          print("Less Priterest Size")
       else:
          print("Less Priterest Size or Inverse")
         


       line = fp.readline()
       cnt2 = 1
       cnt += 1

       

print("Done!")