def rep_char(c, n) :
    print(c * n)

def draw_line_string(Name) :
    msg1 = f'Hello {Name},'
    msg2 = 'Welcome to Seoul.'
    nstr = (len(msg1) if len(msg1) > len(msg2) else len(msg2)) + 2
    print(f'Input his/her name: {Name}')
    rep_char('-', nstr)
    print(f' {msg1} ')
    print(f' {msg2} ')
    rep_char('-', nstr)

draw_line_string('Steve Sueng Jun Yoo')
draw_line_string('Steve Yoo')
