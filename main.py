import csv
from bs4 import BeautifulSoup


data_list = [["itemName", "calories", "totalFat", "saturatedFat", "transFat", "polyFat", "monoFat", "cholesterol", "sodium", "totalCarbs", "dietaryFiber", "totalSugar", "includes", "protein", "vitaD", "calcium", "iron", "potassium"]]

with open('./home.html', 'r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, 'lxml')
    item_name = soup.find('h1').text

    div_classes = soup.find_all('div')
    item_calories = ''
    for div_class in div_classes:
        if div_class == "Item_characteristics__text__dcfEC":
            print(div_class)

    # data_list.append()


# with open('foodData.csv', 'w', newline='') as file:
#     writer = csv.writer(file, delimiter='|')
#     writer.writerows(data_list)
#     print(writer)