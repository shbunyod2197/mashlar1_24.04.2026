# 1
class Salom:
    def hello(self):
        print("Hello")

    def how_are_you(self):
        self.hello()
        print("Qalaysiz")

    def bye(self):
        self.how_are_you()
        print("Xayr")

salom = Salom()
salom.bye()

# 2
class Sonlar:
    def bir(self):
        print(1)

    def ikki(self):
        self.bir()
        print(2)

    def uch(self):
        self.ikki()
        print(3)

a = Sonlar()
a.uch()

# 3
class Hayvon:
    def ovqat(self):
        print("Hayvon ovqat yeydi")

    def uxla(self):
        self.ovqat()
        print("Hayvon uxlaydi")

    def yur(self):
        self.uxla()
        print("Hayvon yuradi")

a = Hayvon()
a.yur()

# 4
class Talaba:
    def ism(self):
        print("Sabr")

    def yosh(self):
        self.ism()
        print(19)

    def kurs(self):
        self.yosh()
        print(3)

a = Talaba()
a.kurs()

# 5
class Mashina:
    def start(self):
        print("Mashina ishga tushdi")

    def drive(self):
        self.start()
        print("Mashina harakatlandi")

    def stop(self):
        self.drive()
        print("Mashina to'xtadi")


a = Mashina()
a.stop()

# 6
class Telefon:
    def yoq(self):
        print("Telefon yoniq")

    def qongiroq(self):
        self.yoq()
        print("Qo'ng'iroq qilinyapotio")

    def ochir(self):
        self.qongiroq()
        print("Telefon o'chirildi")

a = Telefon()
a.ochir()

# 7
class Kitob:
    def och(self):
        print("Kitob ochildi")

    def oqi(self):
        self.och()
        print("Kitob o'qilmoqda")

    def yop(self):
        self.oqi()
        print("Kitob yopildi")


a = Kitob()
a.yop()

# 8
class Ovqat:
    def tayyor(self):
        print("Ovqat tayyor")

    def ye(self):
        self.tayyor()
        print("Ovqat yeyildi")

    def yuv(self):
        self.ye()
        print("Idishlar yuvildi")


a = Ovqat()
a.yuv()

# 9
class Dars:
    def boshlandi(self):
        print("Dars boshlandi")

    def tushuntirish(self):
        self.boshlandi()
        print("MAVZU TUSHINTIRILDI")

    def yakunlash(self):
        self.tushuntirish()
        print("Darsa tugadi")

a = Dars()
a.yakunlash()

# 10
class Kompuyuter:
    def yoq(self):
        print("Kompuyuter yoqildi")

    def ishla(self):
        self.yoq()
        print("Kompuyuter ishlamoqda")

    def ochir(self):
        self.ishla()
        print("Kompuyuter ochirildi")


a = Kompuyuter()
a.ochir()
