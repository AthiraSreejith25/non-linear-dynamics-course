import matplotlib.pyplot as py

def tent(x):
    return 1 - 1.999*abs(x - 1/2)

def shift(x):
    return (2*x)%1


def map_plot(compo,name,f):
    steps = 1000
    ip = [i/steps for i in range(0,steps)]
    op = []
    for k in ip:
        for j in range(compo):
            k = f(k)
        op.append(k)

    py.plot(ip,op,'.')
    py.plot(ip,ip)
    py.savefig(name.format(compo))
    py.show()


for l in range(1,5):
    map_plot(l,"Tent_map{}.png",tent)
    map_plot(l,"Shift_map{}.png",shift)


#x0 = 0.4356754332
x0 = 0.999
ts = [x0]
sh = [x0]
number = 100
for i in range(number):
    ts.append(tent(ts[-1]))
    sh.append(shift(sh[-1]))

py.plot([i for i in range(number+1)], ts)
py.savefig("Time_series_tent.png")
py.show()


py.plot([i for i in range(number+1)], sh)
py.savefig("Time_series_Shift.png")
py.show()


