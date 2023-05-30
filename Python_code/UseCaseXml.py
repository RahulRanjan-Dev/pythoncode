import xml.etree.ElementTree as ET
import csv

# Parse the XML file
tree = ET.parse('UseCaseTestData.xml')
root = tree.getroot()

# Extract the data from the XML elements
fileHeader = root.find('fileHeader')
fileFormatVersion = fileHeader.get('fileFormatVersion')
vendorName = fileHeader.get('VendorName')
dnPrefix = fileHeader.get('dnPrexix')
elementType = fileHeader.find('fileSender').get('elementType')
beginTime = fileHeader.find('measCollec').get('beginTime')

measData = root.find('measData')
measInfoList = []
for measInfo in measData.findall('measInfo'):
    measInfoId = measInfo.get('measInfoId')
    for measType in measInfo.findall('measType'):
        measTypeVal = measType.text
        for measValue in measInfo.findall('measValue'):
            measValueVal = measValue.find('r').text
            measInfoList.append([measInfoId, measTypeVal, measValueVal])

footer = root.find('footer')
endTime = footer.find('measCollect').get('endTime')

# Write the data to a CSV file
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    #writer.writerow(['fileFormatVersion', 'VendorName', 'dnPrefix', 'elementType', 'beginTime'])
    writer.writerow([fileFormatVersion, vendorName, dnPrefix, elementType, beginTime])
    writer.writerow(['measInfoId', 'measType', 'measValue'])
    for measInfo in measInfoList:
        writer.writerow(measInfo)
    #writer.writerow(['endTime'])
    writer.writerow([endTime])
