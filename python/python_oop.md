# OOP

- 객체
- 객체지향프로그래밍
- 클래스와 객체

### 객체(Object)
> Python에서 모든 것은 객체이다.
> 
> 모든 객체는 타입, 속성, 조작법을 가진다.


## OOP 기초

```
# 클래스 정의
class MyClass
    pass

# 인스턴스 생성 (객체라고 읽어도 됨.)
my_instance = MyClass()

# 메서드 호출
my_instance.my_thod()

```

### 인스턴스(instance)
- 정의된 클래스(`class`)에 속하는 객체를 해당 클래스의 인스턴스(instance)라고 한다.
- `person` 클래스의 인스턴스는 `Person()`을 호출함으로써 생성된다.


### 인스턴스 변수
- 생성자 메서드에서 `self.변수명` 으로 정의
- 인스턴스가 생성된 이후 `인스턴스.변수명` 으로 접근 및 할당

예시
```
class Person:
    pass

p1 = Person()
p1.name = '이재용'
p1.age = 26
```

### 인스턴스 메서드
- 인스턴스 메서드는 인스턴스가 사용할 메서드이다.
- 클래스 내부에 정의되는 메서드는 기본적으로 인스턴스 메서드로 생성된다.
- 메서드 호출시, 첫번째 인자로 인스턴스 자기자신에 해당하는 `self`가 전달된다.

예시
```
class Person:
    def talk(self):
    print('hi')

p1 = Person()
p2.talk()
-> hi 출력됨
```

- 메서드도 함수이기 때문에 추가 인자 받을 수 있다.

예시
```
class Person:
    def talk(self, arg):
        print('hi', arg)

    def eat(self, menu):
        print('냠냠', menu)

p1 = Person()
p1.talk('안녕!')

e1 = eat()
e1.eat('치킨')
```
## self
> 인스턴스 자신(self)

- 파이썬에서는 인스턴스 메서드 호출 시 첫번째 인자로 인스턴스 자신이 전달되게 설계되었다.
- 보통 매개변수명으로 `self`를 첫번째 인자로 정의한다.

## 생성자(constructor) 메서드
- 인스턴스 객체가 생성될때 자동으로 호출되는 함수
- 반드시 `__init__` 이라는 이름으로 정의한다.

 예시
 ```
 class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def talk(self):
        print(f'안녕 내 이름은 {self.name}이고 나이는 {self.age}이야')

p = Person('이재용', 26)
p.talk()
->안녕 내 이름은 이재용이고 나이는 26이야 출력됨.
 ```

## 클래스(class)
> `class` : 객체들의 분류(class)를 정의할 때 쓰이는 키워드


### 클래스(class) 생성
- 클래스 생성은 `class` 키워드와 정의하려고 하는 `클래스 이름`으로 가능하다.
- 클래스 이름은 `PascalCase`로 정의한다.
- 클래스 내부에는 데이터와 함수를 정의할 수 있고, 이 때 함수는 `메서드라`고 부른다.

### 클래스 변수
- 클래스의 속성
- 모든 인스턴스가 공유
- 클래스 선언 내부에서 정의
- `클래스.변수명` 으로 접근 및 할당

예시
```
class Circle:
    pi = 3.14
    
    def __init__(self,r):
        self.r = r

    def area(self):
        return self.pi * (self.r ** 2)

c1 = Circle(4)
c.area() # 인스턴스 메서드인 area에서 pi값이 없지만 상위 클래스인 Circle 클래스에서 정의되어 있기 때문에 사용할 수 있음.
->출력값 50.24
```

## OOP의 핵심 개념
1. 추상화
2. 상속
3. 다형성
4. 캡슐화

### 1. 추상화
- 여러  클래스가 공통적으로 사용할 속성 및 메서드를 추출하여 기본 클래스로 작성하여 활용한다.
  
예시
  ```
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.socre = score

    def talk(self):
        print(f'안녕하세요 {self.name}입니다.')

    def study(self):
        self.score += 1

class Teacher:
    def __init__(self,name,age,money):
        self.name = name
        self.age = age
        self.money = money

    def talk(self):
        print(f'안녕하세요. {self.name}입니다.')

    def teach(self):
        self.money += 1000

> 두 개의 클래스 내의 공통적으로 사용되는 코드 존재 
> 이 때 추상화 개념 사용


    class Person :
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def talk(self):
            print(f'안녕하세요. {self.name}입니다.')

  ```

### 2. 상속
- 부모 클래스의 모든 속성이 자식 클래스에게 상속되므로 코드 재사용성이 높아진다.

사용법
> class ChildClass(ParentClass):
>
>   [code blocck]

예시
```
class Person :
    pop = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.pop += 1

    def talk(self):
        print(f'안녕하세요. {self.name}입니다.')

class Student(Person):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.socre = score
        Person.pop += 1

    def study(self):
        self.score += 1

s = Student('이재용', 20, 90)
s.talk()
-> 안녕하세요. 이재용입니다.  # 부모 클래스를 상속받았기 때문에 자식 클래스에서 talk() 메서드가 없어도 출력 가능.
```

### super()
- 자식 클래스에 메서드를 추가로 구현할 수 있다.
- 부모 클래스의 내용을 사용하고자 할 때 사용한다.

예시
```
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email

    def greeting(self):
        print(f'안녕, {self.name}')

class Student(Person):
    def __init__(self, name, age, number, email, student_id)
    super().__init__(self, name, age, number, email)
    self.student_id = student_id

p1 = Person('홍교수', 40, '01012345678', hong@naver.com)
s1 = Student('학생', 20, '01012341234' , student@naver.com, '1234')

s1.student_id
-> '1234' 출력됨
```

### 3. 다형성
- 서로 다른 클래스에 속해있는 객체들이 동일한 메시지에 대해 각기 다른 방식으로 응답될 수 있음.

#### 메서드 오버라이딩
> 자식 클래스에서 부모 클래스의 메서드를 재정의하는 것

- 상속 받은 메서드를 `재정의`할 수도 있다.
- 상속 받은 클래스에서 같은 이름의 메서드로 덮어쓴다.
- `__init__`, `__str__`의 메서드를 정의하는 것  역시, 메서드 오버라이딩이다.

예시
```
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email

    def talk(self):
        print(f'안녕, {self.name}')

# 위 Person 클래스를 상속받아 군인답게 말하는 Soldier 클래스 생성 / talk 매서드 재정의(override)

class Soldier(Person):
    def__init__(self, name, age, number, email, army):
        super.__init__(name, age, number, email)
        self.army = army

    def talk(self):
        print(f'충성, 상병 {self.name}')


p1 = Person('이재용', 26, 1234, '123@naver.com')
p1.talk()
-> 안녕, 이재용 출력됨

s = Soldier('김군인', 22, 1234, 'army@naver.com', '육군')
s.talk()
-> 충성, 상병 김군인 출력됨
```

### 캡슐화
- 객체의 일부 구현 내용에 대해 외부로부터의 직접적인 액세스를 차단한다.

