import os
import xml
from pyproj import Transformer

folder="E:\\island"
f=os.listdir(folder)
ty=[]
for x in f:
    kml_file=xml.dom.minidom.parse(folder+'\\'+x)
    coordinates=kml_file.getElementsByTagName("coordinates")    
    trans=[]
    transfor=Transformer.from_crs(4326, 32649,always_xy=True)#108-114
    #num_ex=0
    for coordinate in coordinates:
        coor_text=coordinate.firstChild.nodeValue
        coords = coor_text.split(' ')
        for coord in coords:
            if len(coord)>1:
                lon,lat,_=coord.split(',')
                x,y=transfor.transform(float(lon), float(lat))
                trans.append(str(x)+','+str(y))                 
    ty.append(trans)       

def save_as_txt(extracted_coordinates, output_file):
    with open(output_file, 'w') as f:
        f.write(f'COAST\n')
        f.write(f'{len(extracted_coordinates)}\n')
        for x in extracted_coordinates:
            f.write(f'{len(x)} 0\n')
            for a in x:
                a=a.split(",")
                f.write(a[0] +" " +a[1]+ "\n")

output_file = "E:\\island.txt"
save_as_txt(ty, output_file)

#if kml is not in order
folder="E:\***\land"
ff=os.listdir(folder)
sx=[]
for f in ff:
    num,kml=f.split('.')
    sx.append(num)
for i in range(len(sx)-1):
    for j in range(i+1,len(sx)):
        if int(sx[i])>int(sx[j]):
            a=sx[j]
            sx[j]=sx[i]
            sx[i]=a


#creat one kml with standard rule
def create_combined_kml():
  combined_kml = """<?xml version="1.0" encoding="UTF-8"?>
        <kml xmlns="http://www.opengis.net/kml/2.2">
        <Document>"""
    return combined_kml


#other way to open kml
import glob
from bs4 import BeautifulSoup
def get_kml_files():
    kml_files = glob.glob("E:/***/land/*.kml")  # 将路径修改为您的实际路径
    return kml_files

def parse_kml_files(kml_files):
    combined_kml = create_combined_kml()

    for kml_file in kml_files:
        with open(kml_file, "r", encoding="utf-8") as f:
            # 解析KML文件
            soup = BeautifulSoup(f, "xml")

            # 获取Placemark元素
            placemarks = soup.find_all("Placemark")

            # 将每个Placemark元素的内容添加到合成KML文件中
            for placemark in placemarks:
                combined_kml += str(placemark)

    combined_kml += "</Document></kml>"
    return combined_kml
def main():
    kml_files = get_kml_files()
    combined_kml = parse_kml_files(kml_files)
    save_combined_kml(combined_kml)

if __name__ == "__main__":
    main()





