def fn(a=0, b=0, c=0):
    print('a:{}, b:{}, c:{}'.format(a, b, c))
    # return "Hello from fn()"

fn(1, 2, 3)
fn(a=1, c=3)

def function(a, *args, **keys):
    print('a:', a)
    print('args:', args)
    print('keys:', keys)
    print('words:', keys['user'])

function(1, True, False, [1, 2, 3], 'emil', user = 'admin', password = 'admin1')

def result(a=0, b=0):
    return a**b

r = result(2, 2)
print(r)