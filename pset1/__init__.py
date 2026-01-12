import check50
import check50.c

@check50.check()
def exists():
    """temperature.c exists"""
    check50.exists("temperature.c")

@check50.check(exists)
def compiles():
    """temperature.c compiles"""
    # lcs50=False means we do not link the CS50 library
    check50.c.compile("temperature.c", lcs50=False)

@check50.check(compiles)
def test_freezing():
    """converts 0 Celsius correctly"""
    check50.run("./temperature")\
        .stdin("0")\
        .stdout("0.00 Celsius = 32.00 Fahrenheit")\
        .stdout("0.00 Celsius = 273.15 Kelvin")\
        .exit(0)

@check50.check(compiles)
def test_boiling():
    """converts 100 Celsius correctly"""
    check50.run("./temperature")\
        .stdin("100")\
        .stdout("100.00 Celsius = 212.00 Fahrenheit")\
        .stdout("100.00 Celsius = 373.15 Kelvin")\
        .exit(0)

@check50.check(compiles)
def test_negative():
    """converts -40 Celsius correctly"""
    check50.run("./temperature")\
        .stdin("-40")\
        .stdout("-40.00 Celsius = -40.00 Fahrenheit")\
        .stdout("-40.00 Celsius = 233.15 Kelvin")\
        .exit(0)

@check50.check(compiles)
def test_body_temp():
    """converts 37 Celsius (body temp) correctly"""
    check50.run("./temperature")\
        .stdin("37")\
        .stdout("37.00 Celsius = 98.60 Fahrenheit")\
        .stdout("37.00 Celsius = 310.15 Kelvin")\
        .exit(0)

@check50.check(exists)
def style():
    """temperature.c follows style guide"""
    check50.run("style50 temperature.c").exit(0)