print("weather condition")
def weather_condition(weather):
    if weather=="rainy":
     print("wear a raincoat")
     if weather=="sunny":
      print("wear a hat")
     if weather=="cloudy":
      print("wear a sweater")
      
weather=input("enter weather as rainy/sunny/cloudy:")
weather_condition(weather)