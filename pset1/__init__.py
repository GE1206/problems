import check50
import check50.c

@check50.check()
def exists():
    check50.exists("temperature.c")

@check50.check(exists)
def compiles():
    check50.c.compile("temperature.c", lcs50=False)

@check50.check(compiles)
def test_0():
    """0.00 Celsius yields 32.00 Fahrenheit and 273.15 Kelvin"""
    check50.run("./temperature").stdin("0").stdout("0.00 Celsius = 32.00 Fahrenheit").stdout("0.00 Celsius = 273.15 Kelvin").exit(0)

@check50.check(compiles)
def test_100():
    """100.00 Celsius yields 212.00 Fahrenheit and 373.15 Kelvin"""
    check50.run("./temperature").stdin("100").stdout("100.00 Celsius = 212.00 Fahrenheit").stdout("100.00 Celsius = 373.15 Kelvin").exit(0)

@check50.check(compiles)
def test_37():
    """37.00 Celsius yields 98.60 Fahrenheit and 310.15 Kelvin"""
    check50.run("./temperature").stdin("37").stdout("37.00 Celsius = 98.60 Fahrenheit").stdout("37.00 Celsius = 310.15 Kelvin").exit(0)

@check50.check(compiles)
def test_neg40():
    """-40.00 Celsius yields -40.00 Fahrenheit and 233.15 Kelvin"""
    check50.run("./temperature").stdin("-40").stdout("-40.00 Celsius = -40.00 Fahrenheit").stdout("-40.00 Celsius = 233.15 Kelvin").exit(0)

@check50.check(compiles)
def style():
    """temperature.c follows style50"""
    check50.run("style50 temperature.c").exit(0)
