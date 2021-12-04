import requests, json
import random
from flask import Flask

# create instance of flask app
app = Flask(__name__)

# temp unit conversion
def kelvin_to_fahrenheit(kelvin):
    return kelvin * 1.8 - 459.67


# returns temp in fahrenheit for a given city
def temp_from_city(city):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = city
    API_KEY = "f14b789860ff7970a1fcf249986fbbdd"
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        main = data["main"]
        k_temp = main["temp"]
        f_temp = kelvin_to_fahrenheit(k_temp)
    return int(f_temp)


# randomly chooses one of two sides to show phrase text
def choose_side_with_phrase(city1, city2):
    sides = [city1, city2]
    chosen_side = random.choice(sides)
    return chosen_side


# calculates difference between two F temperatures, and returns severity score 1-5
def compare_temp(temp1, temp2):

    # comparing two temperatures to find the winner, and the difference
    if temp1 - temp2 > 0:
        winner = temp1
        difference = temp1 - temp2
    elif temp1 - temp2 < 0:
        winner = temp2
        difference = temp2 - temp1
    elif temp1 - temp2 == 0:
        winner = "no winner"
        difference = 0

    # dictionary for assigning a serverity score 1-5 based on the difference
    options = {
        0: difference == 0,
        1: 0 < difference <= 7,
        2: 7 < difference <= 14,
        3: 14 < difference <= 21,
        4: 21 < difference <= 28,
        5: 28 < difference <= 35,
    }
    # using the dictionary to assign a rating
    for key, value in options.items():
        if value == True:
            score = key

    return winner, score


def create_payload(dict_1, dict_2):
    payload = {"data": [dict_1, dict_2]}
    return payload

def main():
    city_1 = "San Francisco"
    city_2 = "Boston"

    winning_phrases_sf = [
        "dumpstered on!",
        "get absolutely rekt shitters!",
        "humiliating.",
        "what a pile'a dumpsters lmao",
        "wow our lives are so cool and we're rich and the weather is bad over there hehe",
    ]

    losing_phrases_sf = [
        "dang",
        "we got trashed on :(",
        "i cant believe we made this stupid app",
        "i am a puny pathetic excuse for a man",
        "shucks!!!!!!!!!!!!!~!!!!!!!~1111111!!!!",
    ]

    winning_phrases_bos = [
        "go sox",
        "have fun stepping on shit and broken glass all day, dweebs!",
        "absolutely tr444shed on sh!tters!!!!",
        "boston - toston - tossin up a coupla victory royales baby!",
        "SAN FRAN SAN FRAN haha flows off the tongue but u can't say it",
    ]

    losing_phrases_bos = [
        "damn its pretty cold over here, seems like we r bad at choosing where to live geographically",
        "We lost our boots and our shoes got all slushy :(",
        "kinda feels like living here is a giant waste of a life",
        "wow, we are just a bunch of absolutely massive dumpsters, aren't we :(",
        "its so cold, our faces are literally in pain. ow.",
    ]

    sf_temp, bos_temp = temp_from_city(city_1), temp_from_city(city_2)

    winning_temp, score = compare_temp(sf_temp, bos_temp)

    phrase_side = choose_side_with_phrase(city_1, city_2)

    final_data_dict_1 = {"name": city_1, "temp": sf_temp, "phrase": None}

    final_data_dict_2 = {"name": city_2, "temp": bos_temp, "phrase": None}

    if phrase_side == city_1:
        if winning_temp == sf_temp:
            final_data_dict_1["phrase"] = winning_phrases_sf[score - 1]
        elif winning_temp == bos_temp:
            final_data_dict_1["phrase"] = losing_phrases_sf[score - 1]
    elif phrase_side == city_2:
        if winning_temp == bos_temp:
            final_data_dict_2["phrase"] = winning_phrases_bos[score - 1]
        elif winning_temp == sf_temp:
            final_data_dict_2["phrase"] = losing_phrases_bos[score - 1]

    payload = create_payload(final_data_dict_1, final_data_dict_2)
    return payload

final_data = main()

# data API route
@app.route("/data")
def get_data():
    return final_data

if __name__ == "__main__":
    app.run(debug=True)