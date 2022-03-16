def bmi(kilo, boy):
    boy = boy / 100
    return kilo / boy ** 2

kilo = float(input())
boy = float(input())

bmi_result = bmi(kilo, boy)
print("%.3f" % bmi_result)