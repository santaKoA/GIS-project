


from django.shortcuts import render, redirect
from webApp.models import Embassy




def index(response):
    if response.method == 'POST':

        ### VULENARABLE INPUT FIELD ###
        if response.POST.get('search-bar-submit'):
            return search_results(response)

        return redirect('/home')

    all_embassies = Embassy.objects.all()

    id_link_map = {
        1: 'https://www.google.com/maps/dir/32.0858631,34.8181464/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%90%D7%95%D7%A7%D7%A8%D7%90%D7%99%D7%A0%D7%94,+%D7%99%D7%A8%D7%9E%D7%99%D7%94%D7%95+50,+%D7%AA%D7%9C+%D7%90%D7%91%D7%99%D7%91-%D7%99%D7%A4%D7%95%E2%80%AD/@32.0890109,34.8314895,13z/data=!3m1!4b1!4m9!4m8!1m1!4e1!1m5!1m1!1s0x151d4bf45c55e589:0xdae0d5cfb0f879a5!2m2!1d34.7780662!2d32.0948482',
        2: 'https://www.google.com/maps/dir/31.7587456,35.2190464/%D7%A7%D7%95%D7%A0%D7%A1%D7%95%D7%9C%D7%99%D7%94+%D7%90%D7%99%D7%A1%D7%9C%D7%A0%D7%93,+%D7%91%D7%99%D7%AA+%D7%A6%D7%A8%D7%A4%D7%AA,+%D7%AA%D7%95%25D',
        3: 'https://www.google.com/maps/dir/31.7587456,35.2190464/Embassy+of+Estonia,+%D7%93%D7%A8%D7%9A+%D7%9E%D7%A0%D7%97%D7%9D+%D7%91%D7%92%D7%99%D7%9F+125+HaYovel+Tower,+24.+korrus,+%D7%AA%D7%9C+%D7%90%D7%91%D7%99%D7%91-%D7%99%D7%A4%D7%95,+6107120%E2%80%AD/@31.9140601,35.2789873,10z/data=!3m1!4b1!4m9!4m8!1m1!4e1!1m5!1m1!1s0x151d4b305d83db67:0x9a169094ea35d1e2!2m2!1d34.7891529!2d32.0729969',
        4:'https://www.google.com/maps/dir/31.7587456,35.2190464/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%91%D7%95%D7%9C%D7%92%D7%A8%D7%99%D7%94,+%D7%AA%D7%9C+%D7%90%D7%91%D7%99%D7%91-%D7%99%D7%A4%D7%95%EF%BF%BD',
        5:'https://www.google.com/maps/dir/31.7587456,35.2190464/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%91%D7%9C%D7%92%D7%99%D7%94%E2%80%AD%E2%80%AD/@31.923713,35.2861297,10z/data=!3m1!4b1!4m9!4m8!1m1!4e',
        6:'https://www.google.com/maps/dir/31.7587456,35.2190464/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%91%D7%9C%D7%90%D7%A8%D7%95%D7%A1,+%D7%A8%D7%99%D7%99%D7%A0%D7%A1,+%D7%AA%D7%9C+%D7%90%D7%91%D7%99%25D',
        7:'https://www.google.com/maps/dir//%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%91%D7%A8%D7%99%D7%98%D7%A0%D7%99%D7%94%E2%80%AD/data=!4m6!4m5!1m1!4e2!1m2!1m1!1s0x151d4c7660842867:0x8a8a45546eb44983?sa=',
        8:'https://www.google.com/maps/dir/31.7587456,35.2190464/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%92%D7%A8%D7%9E%D7%A0%D7%99%D7%94,+%D7%94%D7%A9%D7%9C%D7%95%D7%A9%D7%94,+%D7%AA%D7%9C+%D7%90%D7%91%25D',
        9:'https://www.google.com/maps/dir/31.7587456,35.2190464/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%93%D7%A0%D7%9E%D7%A8%D7%A7,+%D7%AA%D7%9C+%D7%90%D7%91%D7%99%D7%91-%D7%99%D7%A4%D7%95%E2%80%AD/@31.9',
        10:'https://www.google.com/maps/dir/31.7587456,35.2190464/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%94%D7%95%D7%9C%D7%A0%D7%93,+%D7%90%D7%91%D7%90+%D7%94%D7%99%D7%9C%D7%9C,+%D7%A8%D7%9E%D7%AA+%D7%92%25',
        11:'https://www.google.com/maps/dir/31.7587456,35.2190464/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%94%D7%95%D7%A0%D7%92%D7%A8%D7%99%D7%94,+%D7%A4%D7%A0%D7%A7%D7%A1,+%D7%AA%D7%9C+%D7%90%D7%91%D7%99%25D',
        12:'https://www.google.com/maps/dir/31.6801024,34.586624/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%99%D7%95%D7%95%D7%9F,+%D7%93%D7%A0%D7%99%D7%90%D7%9C+%D7%A4%D7%A8%D7%99%D7%A9,+%D7%AA%D7%9C+%D7%90%25D',
        13:'https://www.google.com/maps/dir/32.0859292,34.8181587/%D7%A9%D7%93%D7%A8%D7%95%D7%AA+%D7%A8%D7%95%D7%98%D7%A9%D7%99%D7%9C%D7%93+119,+%D7%AA%D7%9C+%D7%90%D7%91%D7%99%D7%91-%D7%99%D7%A4%D7%95%E2%80%AD/@',
        14:'https://www.google.com/maps/dir/31.7587456,35.2190464/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%9C%D7%98%D7%91%D7%99%D7%94+-,+%D7%95%D7%99%D7%99%D7%A6%D7%9E%D7%9F,+%D7%AA%D7%9C+%D7%90%D7%91%D7%99',
        15:'https://www.google.com/maps/dir/31.7587456,35.2190464/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%9C%D7%99%D7%98%D7%90,+Abba+Hillel+Silver+St.,+%D7%A8%D7%9E%D7%AA+%D7%92%D7%9F%E2%80%AD/@31.920085,3',
        16:'https://www.google.com/maps/dir/31.7587456,35.2190464/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%9E%D7%95%D7%9C%D7%93%D7%95%D7%91%D7%94+%D7%91%D7%99%D7%A9%D7%A8%D7%90%D7%9C,+%D7%A8%D7%9E%D7%91%EF%BF%BD%25',
        17:'https://www.google.com/maps/dir/31.7587456,35.2190464/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%9E%D7%9C%D7%98%D7%94,+%D7%93%D7%99%D7%96%D7%A0%D7%92%D7%95%D7%A3,+%D7%AA%D7%9C+%D7%90%D7%91%D7%99%25D',
        18:'https://www.google.com/maps/dir/31.7587456,35.2190464/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%A0%D7%95%D7%A8%D7%91%D7%92%D7%99%D7%94,+%D7%90%D7%99%D7%99%D7%A0%D7%A9%D7%98%D7%99%D7%99%D7%9F,+%EF%BF%BD',
        19:'https://www.google.com/maps/dir/31.7587456,35.2190464/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%A1%D7%9C%D7%95%D7%91%D7%A7%D7%99%D7%94,+%D7%A8%D7%97%D7%95%D7%91+%D7%96%D7%90%D7%91+%D7%96%D7%91%25D',
        20:'https://www.google.com/maps/dir/31.7587456,35.2190464/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%A1%D7%A4%D7%A8%D7%93,+%D7%93%D7%A0%D7%99%D7%90%D7%9C+%D7%A4%D7%A8%D7%99%D7%A9,+%D7%AA%D7%9C+%D7%90%25',
        21:'https://www.google.com/maps/dir/31.7587456,35.2190464/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%A1%D7%A8%D7%91%D7%99%D7%94,+%D7%93%22%D7%A8+%D7%91%D7%95%D7%93%D7%A0%D7%94%D7%99%D7%99%D7%9E%D7%A8,',
        22:'https://www.google.com/maps/dir/31.7587456,35.2190464/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%A4%D7%95%D7%9C%D7%99%D7%9F,+%D7%A1%D7%95%D7%98%D7%99%D7%9F,+%D7%AA%D7%9C+%D7%90%D7%91%D7%99%D7%91-%25',
        23:'https://www.google.com/maps/dir/31.7587456,35.2190464/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%A4%D7%95%D7%A8%D7%98%D7%95%D7%92%D7%9C,+%D7%93%D7%A0%D7%99%D7%90%D7%9C+%D7%A4%D7%A8%D7%99%D7%A9,+%25D',
        24:'https://www.google.com/maps/dir/31.7587456,35.2190464/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%A4%D7%99%D7%A0%D7%9C%D7%A0%D7%93,+%D7%94%D7%A9%D7%9C%D7%95%D7%A9%D7%94,+%D7%AA%D7%9C+%D7%90%D7%91%25D',
        25:'https://www.google.com/maps/dir/31.7587456,35.2190464/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%A6%D7%9B%D7%99%D7%94%E2%80%AD%E2%80%AD/@31.9170396,35.2796844,10z/data=!3m1!4b1!4m9!4m8!1m1!4e1!1m',
        26:'https://www.google.com/maps/dir/31.7587456,35.2190464/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%A6%D7%A8%D7%A4%D7%AA,+Herbert+Samuel,+%D7%AA%D7%9C+%D7%90%D7%91%D7%99%D7%91-%D7%99%D7%A4%D7%95%EF%BF%BD%258',
        27:'https://www.google.com/maps/dir/31.7587456,35.2190464/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%A7%D7%A4%D7%A8%D7%99%D7%A1%D7%99%D7%9F,+%D7%93%D7%99%D7%96%D7%99%D7%A0%D7%92%D7%95%D7%A3,+%D7%AA%EF%BF%BD',
        28:'https://www.google.com/maps/dir/31.7587456,35.2190464/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%A8%D7%95%D7%9E%D7%A0%D7%99%D7%94,+%D7%90%D7%93%22%D7%9D+%D7%94%D7%9B%D7%94%D7%9F,+%D7%AA%D7%9C+%EF%BF%BD%25',
        29:'https://www.google.com/maps/dir/31.7587456,35.2190464/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%A7%D7%A8%D7%95%D7%90%D7%98%D7%99%D7%94,+%D7%95%D7%99%D7%A6%D7%9E%D7%9F%E2%80%AC+2,+%D7%AA%D7%9C+%EF%BF%BD',
        30:'https://www.google.com/maps/dir/31.7587456,35.2190464/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%A9%D7%95%D7%95%D7%93%D7%99%D7%94,+%D7%94%D7%A9%D7%9C%D7%95%D7%A9%D7%94,+%D7%AA%D7%9C+%D7%90%D7%91%25D',
        31:'https://www.google.com/maps/dir/31.7587456,35.2190464/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%A9%D7%95%D7%95%D7%99%D7%99%D7%A5,+%D7%94%D7%99%D7%A8%D7%A7%D7%95%D7%9F,+%D7%AA%D7%9C+%D7%90%D7%91%25D',
        32:'https://www.google.com/maps/dir/31.7587456,35.2190464/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%A7%D7%A0%D7%93%D7%94,+%D7%A0%D7%99%D7%A8%D7%99%D7%9D,+%D7%AA%D7%9C+%D7%90%D7%91%D7%99%D7%91-%D7%99%25',
        33:'https://www.google.com/maps/dir/31.7587456,35.2190464/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%90%D7%A8%D7%A6%D7%95%D7%AA+%D7%94%D7%91%D7%A8%D7%99%D7%AA+%D7%91%D7%99%D7%A9%D7%A8%D7%90%D7%9C,+%EF%BF%BD',
        34:'https://www.google.com/maps/dir/32.0929073,34.8072158/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%90%D7%9C+%D7%A1%D7%9C%D7%91%D7%93%D7%95%D7%A8+%D7%91%D7%99%D7%A9%D7%A8%D7%90%D7%9C%E2%80%AD%EF%BF%BD%25A',
        35:'https://www.google.com/maps/dir/32.0929073,34.8072158/%D7%9E%D7%93%D7%99%D7%A0%D7%AA+%D7%94%D7%99%D7%94%D7%95%D7%93%D7%99%D7%9D+103,+%D7%94%D7%A8%D7%A6%D7%9C%D7%99%D7%94%E2%80%AD/@32.1338823,34.839631',
        36:'https://www.google.com/maps/dir/32.0929073,34.8072158/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%95%D7%A0%D7%A6%D7%95%D7%90%D7%9C%D7%94,+%D7%A8%D7%97%D7%95%D7%91+%D7%90%D7%A8%D7%99%D7%94+%D7%A9%EF%BF%BD',
        37:'https://www.google.com/maps/dir/31.7587456,35.2190464/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%9E%D7%A7%D7%A1%D7%99%D7%A7%D7%95,+%D7%94%D7%9E%D7%A8%D7%93,+%D7%AA%D7%9C+%D7%90%D7%91%D7%99%D7%91-%25',
        38:'https://www.google.com/maps/dir/32.0929073,34.8072158/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%A4%D7%A0%D7%9E%D7%94+%D7%91%D7%99%D7%A9%D7%A8%D7%90%D7%9C,+%D7%A7%D7%A8%D7%9C%D7%99%D7%91%D7%9A,+%25D',
        39:'https://www.google.com/maps/dir/32.0929073,34.8072158/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%A7%D7%95%D7%A1%D7%98%D7%94+%D7%A8%D7%99%D7%A7%D7%94,+%D7%93%D7%A8%D7%9A+%D7%90%D7%91%D7%90+%D7%94%25D',
        40:'https://www.google.com/maps/dir/32.0929073,34.8072158/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%94%D7%A8%D7%A4%D7%95%D7%91%D7%9C%D7%99%D7%A7%D7%94+%D7%94%D7%93%D7%95%D7%9E%D7%99%D7%A0%D7%A7%D7%99',
        41:'https://www.google.com/maps/dir/32.0929073,34.8072158/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%90%D7%95%D7%A8%D7%95%D7%92%D7%95%D7%95%D7%90%D7%99,+%D7%A8%D7%97%D7%95%D7%91+%D7%90%D7%A8%D7%99%EF%BF%BD%25',
        42:'https://www.google.com/maps/dir/32.0929073,34.8072158/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%90%D7%A7%D7%95%D7%95%D7%90%D7%93%D7%95%D7%A8,+%D7%94%D7%90%D7%A8%D7%91%D7%A2%D7%94,+%D7%AA%D7%9C+%25D',
        43:'https://www.google.com/maps/dir/32.0929073,34.8072158/Embajada+Argentina,+%D7%9E%D7%93%D7%99%D7%A0%D7%AA+%D7%94%D7%99%D7%94%D7%95%D7%93%D7%99%D7%9D+85,+%D7%94%D7%A8%D7%A6%D7%9C%D7%99%D7%94%E2%80%AD/@3',
        44:'https://www.google.com/maps/dir/32.0929073,34.8072158/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%91%D7%95%D7%9C%D7%99%D7%91%D7%99%D7%94,+%D7%9B%D7%A8%D7%9E%D7%9C,+%D7%9E%D7%91%D7%A9%D7%A8%D7%AA+%25D',
        45:'https://www.google.com/maps/dir/32.0929073,34.8072158/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%91%D7%A8%D7%96%D7%99%D7%9C,+%D7%90%D7%9C%D7%99%D7%A2%D7%96%D7%A8+%D7%A7%D7%A4%D7%9C%D7%9F,+%D7%AA%25D',
        46:'https://www.google.com/maps/dir/32.0929073,34.8072158/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%A6%D7%99%D7%9C%D7%94,+%D7%94%D7%91%D7%A8%D7%96%D7%9C,+%D7%AA%D7%9C+%D7%90%D7%91%D7%99%D7%91-%D7%99',
        47:'https://www.google.com/maps/dir/32.0929073,34.8072158/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%A4%D7%A8%D7%92%D7%95%D7%95%D7%90%D7%99+%D7%91%D7%99%D7%A9%D7%A8%D7%90%D7%9C%E2%80%AD%E2%80%AD/@32.0',
        48:'https://www.google.com/maps/dir/32.0929073,34.8072158/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%A4%D7%A8%D7%95,+%D7%9E%D7%93%D7%99%D7%A0%D7%AA+%D7%94%D7%99%D7%94%D7%95%D7%93%D7%99%D7%9D,+%D7%94%25D',
        49:'https://www.google.com/maps/dir/32.0929073,34.8072158/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%A7%D7%95%D7%9C%D7%95%D7%9E%D7%91%D7%99%D7%94,+%D7%93%D7%A8%D7%9A+%D7%90%D7%91%D7%90+%D7%94%D7%9C%EF%BF%BD',
        50:'https://www.google.com/maps/dir/32.0929073,34.8072158/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%90%D7%95%D7%96%D7%91%D7%A7%D7%99%D7%A1%D7%98%D7%9F,+%D7%9E%D7%A9%D7%94+%D7%A9%D7%A8%D7%AA,+%D7%A8%25D',
        51:'https://www.google.com/maps/dir/32.0929073,34.8072158/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%90%D7%A8%D7%9E%D7%A0%D7%99%D7%94+%D7%99%D7%A9%D7%A8%D7%90%D7%9C+%E2%80%A2+Embassy+of+the+Republic+o',
        52:'https://www.google.com/maps/dir/32.0929073,34.8072158/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%92%D7%90%D7%95%D7%A8%D7%92%D7%99%D7%94,+%D7%93%D7%A0%D7%99%D7%90%D7%9C+%D7%A4%D7%A8%D7%99%D7%A9,+%25D',
        53:'https://www.google.com/maps/dir/32.0929073,34.8072158/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%94%D7%95%D7%93%D7%95,+%D7%94%D7%99%D7%A8%D7%A7%D7%95%D7%9F,+%D7%AA%D7%9C+%D7%90%D7%91%D7%99%D7%91-%25',
        54:'https://www.google.com/maps/dir/32.0929073,34.8072158/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%95%D7%99%D7%99%D7%98%D7%A0%D7%90%D7%9D,+%D7%95%D7%99%D7%A6%D7%9E%D7%9F%E2%80%AC,+%D7%AA%D7%9C+%EF%BF%BD%259',
        55:'https://www.google.com/maps/dir/32.0929073,34.8072158/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%99%D7%A8%D7%93%D7%9F,+%D7%93%D7%A8%D7%9A+%D7%90%D7%91%D7%90+%D7%94%D7%9C%D7%9C,+%D7%A8%D7%9E%D7%AA+',
        56:'https://www.google.com/maps/dir/32.0929073,34.8072158/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%99%D7%A4%D7%9F,+%D7%AA%D7%9C+%D7%90%D7%91%D7%99%D7%91-%D7%99%D7%A4%D7%95%E2%80%AD%E2%80%AD/@32.0849',
        57:'https://www.google.com/maps/dir/32.0929073,34.8072158/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%90%D7%99%D7%97%D7%95%D7%93+%D7%9E%D7%99%D7%90%D7%A0%D7%9E%D7%90%D7%A8,+%D7%AA%D7%9C+%D7%90%D7%91%EF%BF%BD',
        58:'https://www.google.com/maps/dir/32.0929073,34.8072158/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%A0%D7%A4%D7%90%D7%9C,+%D7%A7%D7%90%D7%95%D7%A4%D7%9E%D7%9F,+%D7%AA%D7%9C+%D7%90%D7%91%D7%99%D7%91-%25',
        59:'https://www.google.com/maps/dir/32.0929073,34.8072158/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%A1%D7%99%D7%9F,+%D7%91%D7%9F+%D7%99%D7%94%D7%95%D7%93%D7%94,+%D7%AA%D7%9C+%D7%90%D7%91%D7%99%D7%91-',
        60:'https://www.google.com/maps/dir/32.0929073,34.8072158/Consulate-General+of+the+Republic+of+Singapore+(Tel+Aviv),+(5th+floor)+6971052,+%D7%94%D7%91%D7%A8%D7%96%D7%9C+34,+%D7%AA%D7%9C+%D7%90%D7%91%D7%99',
        61:'https://www.google.com/maps/dir/32.0929073,34.8072158/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%A4%D7%99%D7%9C%D7%99%D7%A4%D7%99%D7%A0%D7%99%D7%9D,+%D7%91%D7%A0%D7%99+%D7%93%D7%9F,+%D7%AA%D7%9C+%25',
        62:'https://www.google.com/maps/dir/32.0929073,34.8072158/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%A7%D7%95%D7%A8%D7%99%D7%90%D7%94,+%D7%94%D7%A1%D7%93%D7%A0%D7%90%D7%95%D7%AA,+%D7%94%D7%A8%D7%A6%EF%BF%BD',
        63:'https://www.google.com/maps/dir/32.0929073,34.8072158/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%A8%D7%95%D7%A1%D7%99%D7%94,+%D7%94%D7%99%D7%A8%D7%A7%D7%95%D7%9F,+%D7%AA%D7%9C+%D7%90%D7%91%D7%99%25D',
        64:'https://www.google.com/maps/dir/32.0929073,34.8072158/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%AA%D7%90%D7%99%D7%9C%D7%A0%D7%93,+%D7%9E%D7%A9%D7%9B%D7%99%D7%AA,+%D7%94%D7%A8%D7%A6%D7%9C%D7%99%EF%BF%BD',
        65:'https://www.google.com/maps/dir/32.0929073,34.8072158/Angola+Embassy+Tel+Aviv,+%D7%A1%D7%9E%D7%98%D7%AA+%D7%91%D7%99%D7%AA+%D7%94%D7%A9%D7%95%D7%90%D7%91%D7%94+14,+%D7%AA%D7%9C+%D7%90%D7%91%D7%99%EF%BF%BD%259',
        66:'https://www.google.com/maps/dir/32.0929073,34.8072158/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%90%D7%A8%D7%99%D7%AA%D7%A8%D7%99%D7%90%D7%94,+%D7%A0%D7%99%D7%A8%D7%99%D7%9D,+%D7%AA%D7%9C+%D7%90%25D',
        67:'https://www.google.com/maps/dir/32.0929073,34.8072158/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%90%D7%AA%D7%99%D7%95%D7%A4%D7%99%D7%94,+%D7%93%D7%A8%D7%9A+%D7%9E%D7%A0%D7%97%D7%9D+%D7%91%D7%92%EF%BF%BD',
        68:'https://www.google.com/maps/dir/32.0929073,34.8072158/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%92%D7%90%D7%A0%D7%94,+%D7%93%D7%A8%D7%9A+%D7%90%D7%91%D7%90+%D7%94%D7%9C%D7%9C,+%D7%A8%D7%9E%D7%AA+',
        69:'https://www.google.com/maps/dir/32.0929073,34.8072158/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%93%D7%A8%D7%95%D7%9D+%D7%90%D7%A4%D7%A8%D7%99%D7%A7%D7%94,+%D7%93%D7%A8%D7%9A+%D7%90%D7%91%D7%90+%25D',
        70:'https://www.google.com/maps/dir/32.0929073,34.8072158/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%97%D7%95%D7%A3+%D7%94%D7%A9%D7%A0%D7%94%D7%91,+%D7%A8%D7%97%D7%95%D7%91+%D7%96%D7%90%D7%91+%D7%96%25',
        71:'https://www.google.com/maps/dir/32.0929073,34.8072158/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%9E%D7%A6%D7%A8%D7%99%D7%9D,+%D7%91%D7%96%D7%9C,+%D7%AA%D7%9C+%D7%90%D7%91%D7%99%D7%91-%D7%99%D7%A4%25',
        72:'https://www.google.com/maps/dir/32.0929073,34.8072158/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%A0%D7%99%D7%92%D7%A8%D7%99%D7%94,+%D7%92%D7%95%D7%A8%D7%93%D7%95%D7%9F,+%D7%AA%D7%9C+%D7%90%D7%91%25D',
        73:'https://www.google.com/maps/dir/32.0929073,34.8072158/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%A7%D7%A0%D7%93%D7%94,+%D7%A0%D7%99%D7%A8%D7%99%D7%9D,+%D7%AA%D7%9C+%D7%90%D7%91%D7%99%D7%91-%D7%99%25',
        74:'https://www.google.com/maps/dir/32.0929073,34.8072158/%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA+%D7%90%D7%95%D7%A1%D7%98%D7%A8%D7%9C%D7%99%D7%94,+%D7%99%D7%94%D7%95%D7%93%D7%94+%D7%94%D7%9C%D7%95%EF%BF%BD%25',
        75:'https://www.google.com/maps/dir//Embassy+of+Israel+36+Brandon+Street+Wellington+Central,+Wellington+6146+%D7%A0%D7%99%D7%95+%D7%96%D7%99%D7%9C%D7%A0%D7%93%E2%80%AD%E2%80%AD/@-41.2831046,174.7760751,18',
        

    }

    return render(response, "webApp/index.html", {'Embassies': all_embassies, 'id_link_map': id_link_map})





def search_results(response):  
    query = response.POST.get('search-bar')
    all_embassies = Embassy.objects.filter(name=query)

    return render(response, "webApp/search_results.html", {'results':[all_embassies]})






def emassyMap(request):
    return render(request, "webApp/map.html")


def about(request):
    return render(request, "webApp/about.html")



