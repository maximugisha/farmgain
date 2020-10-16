import requests as rq
import pygal

from pygal.style import Style

#URLS to open

PRICES = "http://localhost:8000/prices/?format=json"

# MAKE AN API call to url to retrieve data
p = rq.get(PRICES)


#store the json-encoded content in the retrieved data
response = p.json()


#print(json.dumps(response, indent=4)) #make json pretty on output


#count the number of keys presented in data
prices = []
[prices.append(price) for price in response]
#print("number of Prices here: %s" % (len(prices)))
#print(prices)


#Retrieve crop names
crops = []
[crops.append(price["crop_name"]) for price in prices]
#print(crops)

#Retrieve market names
markets = []
[markets.append(price["market_name"]) for price in prices]
#print(markets)

#retrieve wholesaaleprice
wholesale = []
[wholesale.append(price["wholesale_price"]) for price in prices]
#print(wholesale)

#retrieve retailprice
retail = []
[retail.append(price["retail_price"]) for price in prices]
#print(retail)




#time to make visualizations
# define simple style so we add  a pygal.style import
custom_style = Style(
    background='transparent',
    plot_background='transparent',
    foreground='#53E89B',
    foreground_strong='#53A0E8',
    foreground_subtle='#630C0D',
    opacity='.6',
    opacity_hover='.9',
    transition='400ms ease-in',
    colors=('#E853A0', '#E8537A', '#E95355', '#E87653', '#E89B53'))


bar_chart = pygal.Bar(style=custom_style, x_label_rotation=45, show_legend=True)
bar_chart.title = "Visual Interpretation for %s Prices" % (len(prices))

bar_chart.x_labels = crops

bar_chart.add("Retail Price ", retail)
bar_chart.add("Whole Sale Price ", wholesale)

bar_chart.render_in_browser()  # You can either view in browser
#bar_chart.render_to_file("pricesviz.svg")  # or view as an svg file

# Several other output options exists, check them out Pygal's documentation