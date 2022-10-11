import csv
from bs4 import BeautifulSoup

# initialize the first row with each column name
data_list = [["itemName", "calories", "totalFat", "saturatedFat", "transFat", "polyFat", "monoFat", "cholesterol", "sodium", "totalCarbs", "dietaryFiber", "totalSugar", "includes", "protein", "vitaD", "calcium", "iron", "potassium"]]

with open('./home.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')

    item_name = soup.find('h1').text
    
    # find all divs that have a specific class
    item_calories = soup.find_all("div", {"class": "Item_characteristics__text__dcfEC"})[1].text

    # grab all data from table containing nutritional facts
    item_nutrition = soup.find_all('td')

    # create a list of text values from table content in the item_nutrition list, using the step argument in the slice operator to get every other nth value
    nutrition = [item_info.text for item_info in item_nutrition][1::3]

    # append the item_name to start of the list


    formatted_nutrition = []
    # insert the item name at the beginning of the list
    formatted_nutrition.insert(0, item_name.strip())
    # insert the calories as the second value of the list
    formatted_nutrition.insert(1, item_calories.strip())

    for nutritional_fact in nutrition:
        formatted_nutrition.append(nutritional_fact.strip())

    # append the newly generated list, that is stripped of new line characters, to the data_list of lists that will be used to generate the csv file containing the data
    data_list.append(formatted_nutrition)


with open('foodData1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data_list)
    print(writer)