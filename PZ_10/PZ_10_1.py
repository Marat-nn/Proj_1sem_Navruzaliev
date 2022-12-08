# Туристические агенства предлагают следующие туры. Вояж - Мексика,Канада,Израиль,
# Италия,США. РейнаТур - Англия,Япония,Канада,ЮАР. Радуга - США,Испания,Швеция,Австралия.
# Определить в каких турагенствах можно приобрести туры в Канаду, а в каких в США.

tours = {"Вояж": ["Мексика", "Канада", "Израиль", "Италия", "США"],
         "РейнаТур": ["Англия", "Япония", "Канада", "ЮАР"],
         "Радуга": ["США", "Испания", "Швеция", "Австралия"]}


def findtoursincanada():
    mlist = []
    for i in tours:
        for e in tours[i]:
            if e == "Канада":
                mlist.append(i)
    return mlist


def findtoursinusa():
    mlist = []
    for i in tours:
        for e in tours[i]:
            if e == "США":
                mlist.append(i)
    return mlist


print(findtoursincanada())
print(findtoursinusa())