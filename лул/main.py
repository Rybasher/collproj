from flask import Flask, render_template, request,session
import re
from collections import Counter
import xml.etree.ElementTree as ET

app = Flask(__name__)
k = ""
tokets = []
one = []
choices = []
#________________________________________Вывод документа на экран
@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':

            f = request.files['file']

            tree = ET.parse(f)#Прочитываем xml файл
            root = tree.getroot()# Типа берем начало с первого тега
            for i in root.findall('car'):# в первом теге находим все подтеги тега car
                mark = i.findtext('mark')#Берем содержимое тега mark и всех остальных
                year = i.findtext('Year')
                model = i.findtext('Model')
                distance = i.findtext('distance')
                type = i.findtext('Type')
                vec = i.findtext('Vechicle')
                own = i.findtext('Owner')

                tokets.append({'mark': mark, 'year': year, 'model': model,
                               'dis': distance, 'type': type, 'vec': vec, 'own': own})
            return render_template('index.html', ips=tokets)
    return render_template('index.html')


def main():
    return render_template('main.html', messages=tokets)

@app.route('/addmessage', methods=['POST','GET'])
def parse():

    if request.method == 'POST':
        #f = request.files['file']
        #tree = ET.parse(f)
        #root = tree.getroot()
        tree = ET.parse('cars1.xml')
        root = tree.getroot()
        options = request.form['inlineRadioOptions']#берем значение радиобаттона
        options1 = request.form['inlineRadioOptions']
        options2 = request.form['inlineRadioOptions']
        if options == "option1":#если первый радиобаттон

            own = request.form['owner']#берем значение с текстовой формы владельца
            for i in root.findall('car'):#проходим по всем тегам car
                owner = i.findtext("Owner") #берем текст из тега Владелец
                if owner == own: #если текст соответствует введенному в форму
                    mark = i.findtext('mark') #берем текст марки машины
                    choices.append({'mark': mark})
                    return render_template('index.html', wow=choices)#добавляем его в шаблон
        elif options1 == "option2":
            dis = request.form['dis']
            for i in root.findall('car'):
                owner = i.findtext("distance")
                if owner == dis:
                    mark = i.findtext('mark')
                    choices.append({'mark': mark})
                    return render_template('index.html', wow=choices)
        elif options2 == "option3":

            own = request.form['owner']
            dis = request.form['dis']
            for i in root.findall('car'):
                owner = i.findtext("Owner")
                dist = i.findtext("distance")
                if owner == own and dist == dis:
                    mark = i.findtext('mark')
                    choices.append({'mark': mark})
                    return render_template('index.html', wow=choices)


    return render_template('index.html')








    #text = request.form['text']#Имя пользователя
    #tag = request.form['tag']# Пробег

    #message.append(Message(text, tag))
    #return redirect(url_for('main'))
"""def  find_user(l,u):
    for actor in root.findall('car'):
        if actor.findtext(l) == ch:
            name = actor.find('mark')
            print(name.text)"""




"""f = request.files['file'].read()
        txt = str(f.decode('utf-8'))
        pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        ips = re.findall(pattern, txt)
        result = Counter(ips).most_common(10)
        ban = []
        for key, value in result:
            if value > 100:
                ban.append({'ip': key, 'frequency': value})

        return render_template('index.html', ips=ban)
    return render_template('index.html')"""
"""def main():
    data = open('log').read()
    pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    ips = re.findall(pattern, data)
    result = Counter(ips).most_common(10)
    print(result)
    for key, value in result:
        print(str(key) + ":" + str(value))"""




if __name__ == "__main__":
    app.run(debug=True)
