#создай приложение для запоминания информации
from random import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel , QVBoxLayout,QRadioButton, QMessageBox,QHBoxLayout,QGroupBox,QButtonGroup
class Question():
    def __init__(self,question,right_ans,wrong1,wrong2,wrong3):
        self.question = question
        self.right_ans = right_ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

appl = QApplication([])
wind = QWidget()
wind.setWindowTitle('Memory card')
wind.cur_quest = 0
wind.questornot = True
quest = QLabel('Какой национальности не существует?')
btn = QPushButton('Ответить')
GroupBox = QGroupBox('Варианты ответов')
answers = QButtonGroup()
ans1 = QRadioButton('Энцы')
ans2 = QRadioButton('Чулымцы')
ans3 = QRadioButton('Смурфы')
ans4 = QRadioButton('Алеуты')
answers.addButton(ans1)
answers.addButton(ans2)
answers.addButton(ans3)
answers.addButton(ans4)
AnsButtons = [ans1,ans2,ans3,ans4]
layout1 = QHBoxLayout()
layout2 = QVBoxLayout()
layout3 = QVBoxLayout()
layout2.addWidget(ans1)
layout2.addWidget(ans3)
layout3.addWidget(ans2)
layout3.addWidget(ans4)
layout1.addLayout(layout2)
layout1.addLayout(layout3)
GroupBox.setLayout(layout1)
lay1 = QHBoxLayout()
lay2 = QHBoxLayout()
lay3 = QHBoxLayout()
layo = QVBoxLayout()
lay1.addWidget(quest,alignment = Qt.AlignHCenter)
lay2.addWidget(GroupBox,alignment = Qt.AlignHCenter)
lay3.addWidget(btn,stretch = 1.5)
layo.addLayout(lay1)
layo.addLayout(lay2)
layo.addLayout(lay3)
layo.setSpacing(5)
wind.setLayout(layo)
AnsGroupBox = QGroupBox('Результат теста')
result = QLabel('Правильно/Неправильно')
ans = QLabel('Смурфы!')
layou1 = QHBoxLayout()
layou2 = QHBoxLayout()
layou3 = QVBoxLayout()
layou1.addWidget(result)
layou2.addWidget(ans)
layou3.addLayout(layou1)
layou3.addLayout(layou2)
AnsGroupBox.setLayout(layou3)
lay2.addWidget(AnsGroupBox)
AnsGroupBox.hide()
GroupBox.show()
def showAns():
    GroupBox.hide()
    AnsGroupBox.show()
    btn.setText('Следующий вопрос')
def showQuest():
    AnsGroupBox.hide()
    GroupBox.show()
    btn.setText('Ответить')
    answers.setExclusive(False)
    ans1.setChecked(False)
    ans2.setChecked(False)
    ans3.setChecked(False)
    ans4.setChecked(False)
    answers.setExclusive(True)
def ask(question):
    quest.setText(question.question)
    shuffle(AnsButtons)
    AnsButtons[0].setText(question.right_ans)
    AnsButtons[1].setText(question.wrong1)
    AnsButtons[2].setText(question.wrong2)
    AnsButtons[3].setText(question.wrong3)
    showQuest()
def check_answer(quest):
    if AnsButtons[0].isChecked():
        show_correct('Правильно!')
        wind.questright +=1
    else:
        show_correct('Неверно!')
    print('Статистика')
    print('-Всего вопросов:',wind.questotal)
    print('-Правильных ответов:',wind.questright)
    print('-Рейтинг:',round((wind.questright/wind.questotal)*100,2),'%')
    ans.setText(quest.right_ans)
    wind.questornot = False    
def show_correct(res):
    result.setText(res)
    showAns()
def next_question():
    wind.questotal += 1
    if  len(wind.questions) == 0:
        wind.questions = wind.questions_list.copy()
    cur_quest = randint(0,len(wind.questions)-1)
    wind.cur_quest = cur_quest
    ask(wind.questions[cur_quest])
    wind.questornot = True
def click_ok():
    if wind.questornot:
        check_answer(wind.questions[wind.cur_quest])
        wind.questions.remove(wind.questions[wind.cur_quest])
    else:
        next_question() 



wind.questions = list()
problem1 = Question('Какой национальности не существует?','Смурфы','Энцы','Чулымцы','Алеуты') #это коммит
problem2 = Question('Какой государственный язык бразилии?','Португальский','Бразильский','Английский','Испанский')
problem3 = Question('Как зовут людей,живущих в Индии?','Индийцы','Индейцы','Индусы','Иудеи')
wind.questions.append(problem1)
wind.questions.append(problem2)
wind.questions.append(problem3)
wind.questions_list = wind.questions.copy() 
wind.questotal = 1
wind.questright = 0
ask(problem1)
btn.clicked.connect(click_ok)

wind.show()
appl.exec_()
