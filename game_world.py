# 게임 월드 관리 모듈

# 게임 월드의 표현
# 두 개의 layer를 갖는 게임월드로 구현
objects = [ [] , [] ]

def add_object(o, depth = 0):
    objects[depth].append(o)

def add_objects(o, depth = 0):
    objects[depth] += o

# 월드를 업데이트하는, 객체들을 모두 업데이트하는 함수
def update():
    for layer in objects:
        for o in layer:
            o.update()

# 월드 객체들을 모두 그리기
def render():
    for layer in objects:
        for o in layer:
            o.draw()

# 월드 객체 삭제
def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            return
    raise ValueError('Cannot delete non existing object')