import json
import forecasting


with open('corona_situation.json') as f:
    json_file = json.load(f)

current_situation = forecasting.current_day_array_data(json_file)

future_situation = forecasting.expected_value()

#  Nur-Sultan Data
data_01 = {'NoI current': current_situation[0]['NoI'],
           'NoR current': current_situation[0]['NoR'],
           'NoI expected': future_situation[0]['NoI'],
           'NoR expected': future_situation[0]['NoR']}

#  Almaty Data
data_02 = {'NoI current': current_situation[1]['NoI'],
           'NoR current': current_situation[1]['NoR'],
           'NoI expected': future_situation[1]['NoI'],
           'NoR expected': future_situation[1]['NoR']}

#  Shymkent Data
shymkent_13 = {'NoI current': current_situation[3]['NoI'],
               'NoR current': current_situation[3]['NoR'],
               'NoI expected': future_situation[3]['NoI'],
               'NoR expected': future_situation[3]['NoR']}

#  Akmola Region Data
data_03 = {'NoI current': current_situation[4]['NoI'],
           'NoR current': current_situation[4]['NoR'],
           'NoI expected': future_situation[4]['NoI'],
           'NoR expected': future_situation[4]['NoR']}

#  Aktobe Region Data
data_04 = {'NoI current': current_situation[5]['NoI'],
           'NoR current': current_situation[5]['NoR'],
           'NoI expected': future_situation[5]['NoI'],
           'NoR expected': future_situation[5]['NoR']}

#  Almaty Region Data
data_05 = {'NoI current': current_situation[6]['NoI'],
           'NoR current': current_situation[6]['NoR'],
           'NoI expected': future_situation[6]['NoI'],
           'NoR expected': future_situation[6]['NoR']}

#  Atyrau Region Data
data_06 = {'NoI current': current_situation[7]['NoI'],
           'NoR current': current_situation[7]['NoR'],
           'NoI expected': future_situation[7]['NoI'],
           'NoR expected': future_situation[7]['NoR']}

#  VKO Data
data_16 = {'NoI current': current_situation[8]['NoI'],
           'NoR current': current_situation[8]['NoR'],
           'NoI expected': future_situation[8]['NoI'],
           'NoR expected': future_situation[8]['NoR']}

#  Zhambyl Region Data
data_08 = {'NoI current': current_situation[9]['NoI'],
           'NoR current': current_situation[9]['NoR'],
           'NoI expected': future_situation[9]['NoI'],
           'NoR expected': future_situation[9]['NoR']}

#  3KO Data
data_07 = {'NoI current': current_situation[10]['NoI'],
           'NoR current': current_situation[10]['NoR'],
           'NoI expected': future_situation[10]['NoI'],
           'NoR expected': future_situation[10]['NoR']}

#  Qaragandy Region Data
data_09 = {'NoI current': current_situation[11]['NoI'],
           'NoR current': current_situation[11]['NoR'],
           'NoI expected': future_situation[11]['NoI'],
           'NoR expected': future_situation[11]['NoR']}

#  Qostanay Region Data
data_10 = {'NoI current': current_situation[12]['NoI'],
           'NoR current': current_situation[12]['NoR'],
           'NoI expected': future_situation[12]['NoI'],
           'NoR expected': future_situation[12]['NoR']}

#  Qyzylorda Region Data
data_11 = {'NoI current': current_situation[13]['NoI'],
           'NoR current': current_situation[13]['NoR'],
           'NoI expected': future_situation[13]['NoI'],
           'NoR expected': future_situation[13]['NoR']}

#  Mangystau Region Data
data_12 = {'NoI current': current_situation[14]['NoI'],
           'NoR current': current_situation[14]['NoR'],
           'NoI expected': future_situation[14]['NoI'],
           'NoR expected': future_situation[14]['NoR']}

#  Pavlodar Region Data
data_14 = {'NoI current': current_situation[15]['NoI'],
           'NoR current': current_situation[15]['NoR'],
           'NoI expected': future_situation[15]['NoI'],
           'NoR expected': future_situation[15]['NoR']}

#  CKO Region Data
data_15 = {'NoI current': current_situation[16]['NoI'],
           'NoR current': current_situation[16]['NoR'],
           'NoI expected': future_situation[16]['NoI'],
           'NoR expected': future_situation[16]['NoR']}

#  Turkestan Region Data
data_13 = {'NoI current': current_situation[17]['NoI'],
           'NoR current': current_situation[17]['NoR'],
           'NoI expected': future_situation[17]['NoI'],
           'NoR expected': future_situation[17]['NoR']}
