import matplotlib.pyplot as plt
import cities_data

#  Nur-Sultan visualization Bar Char
def nursultan_bar_char(data):
    names = list(data.keys())
    values = list(data.values())
    plt.bar(range(len(data)), values, tick_label=names)
    plt.show()


def almaty_bar_char(data):
    names = list(data.keys())
    values = list(data.values())
    plt.bar(range(len(data)), values, tick_label=names)
    plt.show()


def shymkent_bar_char(data):
    names = list(data.keys())
    values = list(data.values())
    plt.bar(range(len(data)), values, tick_label=names)
    plt.show()


def akmola_bar_char(data):
    names = list(data.keys())
    values = list(data.values())
    plt.bar(range(len(data)), values, tick_label=names)
    plt.show()


def aktobe_bar_char(data):
    names = list(data.keys())
    values = list(data.values())
    plt.bar(range(len(data)), values, tick_label=names)
    plt.show()


def almaty_region_bar_char(data):
    names = list(data.keys())
    values = list(data.values())
    plt.bar(range(len(data)), values, tick_label=names)
    plt.show()


def atyrau_bar_char(data):
    names = list(data.keys())
    values = list(data.values())
    plt.bar(range(len(data)), values, tick_label=names)
    plt.show()


def vko_bar_char(data):
    names = list(data.keys())
    values = list(data.values())
    plt.bar(range(len(data)), values, tick_label=names)
    plt.show()


def zhambyl_bar_char(data):
    names = list(data.keys())
    values = list(data.values())
    plt.bar(range(len(data)), values, tick_label=names)
    plt.show()


def zko_bar_char(data):
    names = list(data.keys())
    values = list(data.values())
    plt.bar(range(len(data)), values, tick_label=names)
    plt.show()


def karanganda_bar_char(data):
    names = list(data.keys())
    values = list(data.values())
    plt.bar(range(len(data)), values, tick_label=names)
    plt.show()


def qostanay_bar_char(data):
    names = list(data.keys())
    values = list(data.values())
    plt.bar(range(len(data)), values, tick_label=names)
    plt.show()


def qyzylorda_bar_char(data):
    names = list(data.keys())
    values = list(data.values())
    plt.bar(range(len(data)), values, tick_label=names)
    plt.show()


def mangystau_bar_char(data):
    names = list(data.keys())
    values = list(data.values())
    plt.bar(range(len(data)), values, tick_label=names)
    plt.show()


def pavlodar_bar_char(data):
    names = list(data.keys())
    values = list(data.values())
    plt.bar(range(len(data)), values, tick_label=names)
    plt.show()


def sko_bar_char(data):
    names = list(data.keys())
    values = list(data.values())
    plt.bar(range(len(data)), values, tick_label=names)
    plt.show()


def turkestan_bar_char(data):
    names = list(data.keys())
    values = list(data.values())
    plt.bar(range(len(data)), values, tick_label=names)
    plt.show()


print(nursultan_bar_char(cities_data.data_01))
print(almaty_bar_char(cities_data.data_02))
print(shymkent_bar_char(cities_data.shymkent_13))
print(akmola_bar_char(cities_data.data_03))
print(aktobe_bar_char(cities_data.data_04))
print(almaty_region_bar_char(cities_data.data_05))
print(atyrau_bar_char(cities_data.data_06))
print(vko_bar_char(cities_data.data_16))
print(zhambyl_bar_char(cities_data.data_08))
print(zko_bar_char(cities_data.data_07))
print(karanganda_bar_char(cities_data.data_09))
print(qostanay_bar_char(cities_data.data_10))
print(qyzylorda_bar_char(cities_data.data_11))
print(mangystau_bar_char(cities_data.data_12))
print(pavlodar_bar_char(cities_data.data_14))
print(sko_bar_char(cities_data.data_15))
print(turkestan_bar_char(cities_data.data_13))

