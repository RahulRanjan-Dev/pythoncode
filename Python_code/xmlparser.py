import csv
import xml.etree.ElementTree as ET

# parse the XML file
tree = ET.parse('xml_test_data.xml')
# get the root element
root = tree.getroot()
print(root)
# create a list to store the data
data = []
# iterate through each catalog item
for catalog_item in root.iter('catalog_item'):
    gender = catalog_item.attrib['gender']
    print(gender)
    item_number = catalog_item.find('item_number').text
    print(item_number)
    price = catalog_item.find('price').text
    print(price)
    # iterate through each size
    for size in catalog_item.iter('size'):
        size_description = size.attrib['description']
        # iterate through each color swatch
        for color_swatch in size.iter('color_swatch'):
            color = color_swatch.text
            image = color_swatch.attrib['image']
            # add the data to the list
            data.append([gender, item_number, price, size_description, color, image])
            print(data)
    # write the data to a CSV file
    with open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Gender', 'Item Number', 'Price', 'Size', 'Color', 'Image'])
        writer.writerows(data)









    #tx1 = ET.fromstring(root)
    #print(tx1)
    #if resl1.tag =="course":






