from tkinter import *
from tkinter import messagebox
from tkinter.colorchooser import*
from tkinter.filedialog import *
from tkinter.simpledialog import *

#### 변수 설정
canvas_height = 400
canvas_width = 600
canvas_color = "white"
line_color = "black"
fill_color = "white"
line_width = 5
line_length = 5

pen_up = False
current_line = None

#### Functions. 함수

def show():
    messagebox.showinfo("몽구림판 제작", "제작: 몽구스")

def close():
     question_box = messagebox.askquestion(title = "종료 확인", message = "정말로 종료하시겠습니까?")
     if question_box == 'yes':
            window.destroy()
     else:
         pass

def show2():
    messagebox.showinfo(title = "도구", message = "모두지우기: 키보드에서 <E>를 누르시오")

def func_open():
    global filename
    filename = askopenfilename(parent = window, filetypes =(("GIF 파일", "*.gif"), ("모든 파일", "*.*")))
    photo = PhotoImage(file = filename)
    pLabel.configure(image = photo)
    pLabel.image = photo

def func_save():
    global filesave
    filesave = asksaveasfile(parent=window, mode="w",defaultextension=".jpg", filetypes=(("JPG 파일",".jpeg"),("모든 파일","*.*")))
    filesave.close()
        
#모두 지우기 키보드 이벤트 함수
def erase_all(event):
    canvas.delete(ALL)

# 선 굵기 함수
def smaller():
    global line_width
    global line_length
    if (line_width > 5):
        line_width = line_width-5
        line_length = line_length-5

def bigger():
    global line_width
    global line_length
    if (line_width <= 50):
        line_width = line_width+5
        line_length = line_length+5

##도형그리기

# 시작점, 끝점
x1 = None
y1 = None
x2 = None
y2 = None

# 선택=0, 점=1, 선=2, 네모=3, 삼각형=4, 원=5, 글씨=6
draw_mode = 0

# 선택 버튼 함수
def selectButton():
    global draw_mode
    draw_mode = 0

# 점 그리기 버튼 함수
def pointButton():
    global draw_mode
    draw_mode = 1

# 라인 그리기 버튼 함수
def lineButton():
    global draw_mode
    draw_mode = 2

# 네모 그리기 버튼 함수
def rectangleButton():
    global draw_mode
    draw_mode = 3

# 세모 그리기 버튼 함수
def triangleButton():
    global draw_mode
    draw_mode = 4

# 원 그리기 버튼 함수
def circleButton():
    global draw_mode
    draw_mode = 5
    
# 글씨 쓰기 버튼 함수
def textButton():
    global draw_mode
    draw_mode = 6


#지우개
def Eraser():
    global draw_mode, line_color
    draw_mode = 0
    line_color = "white"

def Pancil():
    global draw_mode
    draw_mode = 0
    
def paint(event):
    global x1, y1, x2, y2
    if draw_mode >= 2 and draw_mode <= 5:
        pass
    else:
        width = line_width/2
        x1 = event.x - width
        y1 = event.y - width
        x2 = event.x + width
        y2 = event.y + width
        canvas.create_oval(x1, y1, x2, y2, fill=line_color, outline="")    
    

# 마우스 왼쪽 버튼 눌렀을 때
def mouseLDown(event):
    global x1, y1, draw_mode

    # 점 그리기 모드라면
    if draw_mode == 1:
        #점을 그린다
        canvas.create_oval(event.x-2,event.y-2, event.x+2, event.y+2, fill=line_color, outline=line_color)
    # 글씨 쓰기 모드라면
    elif draw_mode == 6:
        # 글씨를 쓴다
        canvas.create_text(event.x, event.y, text=input_text.get(), fill=line_color)
        
        
    elif draw_mode >= 2 and draw_mode <= 5:
        x1 = event.x
        y1 = event.y

def mouseMove(event):
    global x1, y1        

# 마우스 왼쪽 버튼 뗄 때
def mouseLUp(event):
    global x1, y1, draw_mode

    # 직선 그리기 모드
    if draw_mode == 2:
        canvas.create_line(x1, y1, event.x, event.y, width=line_width, fill=line_color)
    # 네모 그리기 모드
    elif draw_mode == 3:
        canvas.create_rectangle(x1, y1, event.x, event.y,width=line_width, outline=line_color, fill=fill_color)
    # 세모 그리기    
    elif draw_mode == 4:
        canvas.create_polygon(x1,y1,event.x,event.y, event.x-40, event.y+45, width=line_width, outline=line_color, fill=fill_color)
    # 원 그리기 모드
    elif draw_mode == 5:
        canvas.create_oval(x1, y1, event.x, event.y, width=line_width, outline=line_color,fill=fill_color)


## 색상 함수
def get_color():
    global line_color
    color = askcolor()
    line_color = color[1]

def get_fill():
    global fill_color
    color = askcolor()
    fill_color = color[1]

def get_width():
    global line_width
    line_width = askinteger("선 두께", "선 두께(1~100)를 입력하세요", minvalue = 1, maxvalue = 100)
        
def black_color():
        global line_color, now_color
        line_color = "black"
        now_color = "검정색"
        canvas.config(cursor = "pencil")
       
def white_color():
        global line_color, now_color
        line_color = "white"
        now_color = "흰색"
        canvas.config(cursor = "pencil")
        

def skyblue_color():
        global line_color, now_color
        line_color = "skyblue"
        now_color = "하늘색"
        canvas.config(cursor = "pencil")
           

def blue_color():
        global line_color, now_color
        line_color = "blue"
        now_color = "파랑색"
        canvas.config(cursor = "pencil")


def green_color():
        global line_color, now_color
        line_color = "green"
        now_color = "초록색"
        canvas.config(cursor = "pencil")
           

def yellowgreen_color():
        global line_color, now_color
        line_color = "yellowgreen"
        now_color = "연두색"
        canvas.config(cursor = "pencil")
            
        
def yellow_color():
        global line_color, now_color
        line_color = "yellow"
        now_color = "노란색"
        canvas.config(cursor = "pencil")
        

def orange_color():
        global line_color, now_color
        line_color = "orange"
        now_color = "주황색"
        canvas.config(cursor = "pencil")
        

def red_color():
        global line_color, now_color
        line_color = "red"
        now_color = "빨간색"
        canvas.config(cursor = "pencil")
        

def pink_color():
        global line_color, now_color
        line_color = "pink"
        now_color = "핑크색"
        canvas.config(cursor = "pencil")
        
def purple_color():
        global line_color, now_color
        line_color = "purple"
        now_color = "보라색"
        canvas.config(cursor = "pencil")
           
def func_zoom() :   # 확대 함수
    value = askinteger("확대배수", "확대할 배수를 입력하세요(2~8)", minvalue = 2, maxvalue = 8) # 확대할 배수 입력
    photo = PhotoImage(file = filename) # func_open에서 선택된 파일
    photo = photo.zoom(value,value) # 이미지 확대
    pLabel.configure(image = photo) # 윈도창에 나타내기
    pLabel.image = photo
    
def func_subsample() :   # 축소 함수
    value = askinteger("축소배수", "축소할 배수를 입력하세요(2~8)", minvalue = 2, maxvalue = 8) # 축소할 배수 입력
    photo = PhotoImage(file = filename) # func_open에서 선택된 파일
    photo = photo.subsample(value,value) # 이미지 축소
    pLabel.configure(image = photo) 
    pLabel.image = photo
    
## 메인코드
window = Tk()
window.title("몽구림판")
window.geometry("800x600")
canvas = Canvas(bg=canvas_color,height=400, width=600, highlightthickness=0)
canvas.pack()

photo = PhotoImage()
pLabel = Label(window, image =photo)
pLabel.pack()


##키보드 키
window.bind("e", erase_all)

##메뉴 설정
mainMenu = Menu(window)
window.config(menu =mainMenu)
fileMenu = Menu(mainMenu)
plusMenu = Menu(mainMenu)

mainMenu.add_cascade(label = "기능찾기", menu = plusMenu)
plusMenu.add_command(label="선 색상 선택", command=get_color)
plusMenu.add_command(label="선 두께 설정", command=get_width)
plusMenu.add_separator()
plusMenu.add_command(label = "모두지우기", command = show2)

mainMenu.add_cascade(label = "메뉴", menu = fileMenu)
fileMenu.add_command(label = "제작",command = show)
fileMenu.add_separator()
fileMenu.add_command(label = "다른 이름으로 저장", command = func_save)
fileMenu.add_separator()
fileMenu.add_command(label = "종료", command = close)

imageMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "이미지", menu = imageMenu)
imageMenu.add_command(label = "이미지 불러오기", command = func_open)
imageMenu.add_separator()
imageMenu.add_command(label = "확대하기", command = func_zoom)
imageMenu.add_command(label = "축소하기", command = func_subsample)

## 상단 프레임
topframe = Frame(window)
topframe.pack()

## 상단 버튼
Button(topframe, command = get_color, cursor = "pencil", bg = "SystemButtonFace", width=3).pack(side=LEFT,fill ="x")
Button(topframe, command = black_color, cursor = "pencil", bg = "black", width=3).pack(side=LEFT,fill ="x")
Button(topframe, command = white_color, cursor = "pencil", bg = "white", width=3).pack(side=LEFT,fill ="x")
Button(topframe, command = skyblue_color, cursor = "pencil", bg = "skyblue",width=3).pack(side=LEFT,fill ="x")
Button(topframe, command = blue_color, cursor = "pencil", bg = "blue",width=3).pack(side=LEFT,fill ="x")
Button(topframe, command = green_color, cursor = "pencil", bg = "green",width=3).pack(side=LEFT,fill ="x")
Button(topframe, command = yellowgreen_color, cursor = "pencil", bg = "yellowgreen",width=3).pack(side=LEFT,fill ="x")
Button(topframe, command = yellow_color, cursor = "pencil", bg = "yellow",width=3).pack(side=LEFT,fill ="x")
Button(topframe, command = orange_color, cursor = "pencil", bg = "orange",width=3).pack(side=LEFT,fill ="x")
Button(topframe, command = red_color, cursor = "pencil", bg = "red",width=3).pack(side=LEFT,fill ="x")
Button(topframe, command = pink_color, cursor = "pencil", bg = "pink",width=3).pack(side=LEFT,fill ="x")
Button(topframe, command = purple_color, cursor = "pencil", bg = "purple",width=3).pack(side=LEFT,fill ="x")
Button(topframe, command = bigger,text="↑",width=3).pack(side=LEFT)
Button(topframe, command = smaller,text="↓",width=3).pack(side=LEFT)
Button(topframe, command= get_fill, text="fill", width=3).pack(side=LEFT,fill="x")

## 하단 버튼 이미지
circle = PhotoImage(file="circle.gif")
rectangle = PhotoImage(file="rectangle.gif")
triangle = PhotoImage(file="triangle.gif")
line = PhotoImage(file="line.gif")
text = PhotoImage(file="text.gif")
pencil = PhotoImage(file="pencil.gif")
eraser = PhotoImage(file="eraser.gif")

## 하단 프레임.
bottomframe = Frame(window)
bottomframe.pack()

## 하단 버튼
Button(bottomframe, image=circle, command=circleButton).pack(side=LEFT)
Button(bottomframe, image=rectangle,command=rectangleButton).pack(side=LEFT)
Button(bottomframe, image=triangle, command=triangleButton).pack(side=LEFT)
Button(bottomframe, image=line, command=lineButton).pack(side=LEFT)
Button(bottomframe, image=text, command=textButton).pack(side=LEFT)
Button(bottomframe, image=pencil,command=Pancil).pack(side=LEFT)
Button(bottomframe, image=eraser, command=Eraser, cursor = "dotbox").pack(side=LEFT)

# 텍스트 라벨
input_label = Label(topframe, text="Text:")
input_label.pack(side=LEFT)

# 텍스트 엔트리
input_text = StringVar()
input_entry = Entry(topframe, textvariable=input_text, width=18)
input_entry.pack(side=LEFT)

##  함수에 마우스 움직임을 연결
canvas.bind("<B1-Motion>", paint)
canvas.bind("<Button-1>", mouseLDown)
canvas.bind("<ButtonRelease-1>", mouseLUp)

canvas.pack()

window.mainloop()
