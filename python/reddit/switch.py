def case_10_handler():
    print('It is too hot to go outside today. Stay inside!')

def case_9_handler():
    print('It is really hot out there, be careful!')

def case_8_handler():
    print('It is very warm, but no extreme heat today!')

def case_7_handler():
    print('It is very pleasant today. You should pack a picnic!')

def default_handler():
    print('It is cool today. You should take a jacket.')

def switch_function(switch):
    print('Switching off {} which is a {}'.format(switch, type(switch)))
    handler = {
        10: case_10_handler,
        9: case_9_handler,
        8: case_8_handler,
        7: case_7_handler,
    }
    return handler.get(switch, default_handler)() #extra parentheses for executing function

def main():
    celsius = float(input("What is the Celsius temperature? "))
    fahrenheit = 9.0 / 5.0 * celsius + 32
    conditions = int(fahrenheit/10)
    print("It is in the {}0's".format(conditions))
    switch_function(conditions)  

if __name__ == '__main__':
  main()
