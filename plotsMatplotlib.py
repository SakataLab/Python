"""
Script for the Python Workshop - Part 10 : Matplotlib
Dec 2017
Just un-comment the part you want to execute
"""

# from pylab import * 
# import numpy as np

# X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
# print(X)
# cosX = np.cos(X)
# sinX = np.sin(X)
# print(cosX)
# print(sinX)

# plot (X, cosX), plot(X, sinX)
# show()

##########################

# from pylab import * 
# import numpy as np

# X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
# cosX = np.cos(X)
# sinX = np.sin(X)

# # Creatation of a new figure of size 8x6 inches, using 80 dots per inch
# figure(figsize=(8,6), dpi=80)

# # Plot cosine using blue color with a continuous line of width 1 (pixels)
# plot(X, cosX, color="blue", linewidth=1.0, linestyle="-")
# # Plot sine using green color with a continuous line of width 1 (pixels)
# plot(X, sinX, color="green", linewidth=2.0, linestyle="-")

# savefig("fig1.png")
# show()

##########################

# from pylab import * 
# import numpy as np

# X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
# cosX = np.cos(X)
# sinX = np.sin(X)

# figure(figsize=(8,6), dpi=80)

# plot(X, cosX, color="blue", linewidth=1.0, linestyle="-")
# plot(X, sinX, color="green", linewidth=2.0, linestyle="--")

# show()

##########################

# from pylab import * 
# import numpy as np

# X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
# cosX = np.cos(X)
# sinX = np.sin(X)

# figure(figsize=(8,6), dpi=80)

# plot(X, cosX, color="blue", linewidth=1.0, linestyle="-")
# plot(X, sinX, color="green", linewidth=2.0, linestyle="--")

# xlim(-4.0, 4.0)
# ylim(-1.5, 1.5)

# show()

##########################

# from pylab import * 
# import numpy as np

# X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
# cosX = np.cos(X)
# sinX = np.sin(X)

# figure(figsize=(8,6), dpi=80)

# plot(X, cosX, color="blue", linewidth=1.0, linestyle="-")
# plot(X, sinX, color="green", linewidth=2.0, linestyle="--")

# xmin, xmax = X.min(), X.max()
# print("xmin=", xmin, "xmax=", xmax)
# ymin, ymax = cosX.min(), cosX.max()
# print("ymin=", ymin, "ymax=", ymax)
# dx = (xmax - xmin) * 0.2
# dy = (ymax - ymin) * 0.2
# xlim(xmin - dx, xmax + dx)
# ylim(ymin - dy, ymax + dy)

# show()

##########################

# from pylab import * 
# import numpy as np

# X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
# cosX = np.cos(X)
# sinX = np.sin(X)

# figure(figsize=(8,6), dpi=80)

# plot(X, cosX, color="blue", linewidth=1.0, linestyle="-")
# plot(X, sinX, color="green", linewidth=2.0, linestyle="--")

# xticks(np.linspace(-5, 5, 9, endpoint=True))
# yticks(np.linspace(-1.5, 1.5, 5, endpoint=True))

# show()

##########################

# from pylab import * 
# import numpy as np

# X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
# cosX = np.cos(X)
# sinX = np.sin(X)

# figure(figsize=(8,6), dpi=80)

# plot(X, cosX, color="blue", linewidth=1.0, linestyle="-")
# plot(X, sinX, color="green", linewidth=2.0, linestyle="--")

# xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
# yticks([-1, 0, +1])

# show()

##########################

# from pylab import * 
# import numpy as np

# X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
# cosX = np.cos(X)
# sinX = np.sin(X)

# figure(figsize=(8,6), dpi=80)

# plot(X, cosX, color="blue", linewidth=1.0, linestyle="-")
# plot(X, sinX, color="green", linewidth=2.0, linestyle="--")

# xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
# yticks([-1, 0, +1], [r'$-1$', r'$0$', r'$+1$'])

# show()

##########################

# from pylab import * 
# import numpy as np

# X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
# cosX = np.cos(X)
# sinX = np.sin(X)

# figure(figsize=(8,6), dpi=80)

# plot(X, cosX, color="blue", linewidth=2.0, linestyle="-")
# plot(X, sinX, color="orange", linewidth=2.5, linestyle="--")

# ax = gca()
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
# ax.spines['bottom'].set_position(('data', 0))
# ax.yaxis.set_ticks_position('left')
# ax.spines['left'].set_position(('data', 0))

# xlim(X.min() * 1.1, X.max() * 1.1)
# ylim(cosX.min() * 1.1, cosX.max() * 1.1)

# xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
# yticks([-1, 0, +1], [r'$-1$', r'$0$', r'$+1$'])

# show()

##########################

# from pylab import * 
# import numpy as np

# X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
# cosX = np.cos(X)
# sinX = np.sin(X)

# figure(figsize=(8,6), dpi=80)

# plot(X, cosX, color="blue", linewidth=2.0, linestyle="-", label="Cosine")
# plot(X, sinX, color="orange", linewidth=2.5, linestyle="--", label="Sine")

# ax = gca()
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
# ax.spines['bottom'].set_position(('data', 0))
# ax.yaxis.set_ticks_position('left')
# ax.spines['left'].set_position(('data', 0))

# xlim(X.min() * 1.1, X.max() * 1.1)
# ylim(cosX.min() * 1.1, cosX.max() * 1.1)

# xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
# yticks([-1, 0, +1], [r'$-1$', r'$0$', r'$+1$'])

# legend(loc='upper left')

# show()

##########################

# from pylab import * 
# import numpy as np

# X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
# cosX = np.cos(X)
# sinX = np.sin(X)

# figure(figsize=(8,6), dpi=80)

# plot(X, cosX, color="blue", linewidth=2.0, linestyle="-", label="Cosine")
# plot(X, sinX, color="orange", linewidth=2.5, linestyle="--", label="Sine")

# ax = gca()
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
# ax.spines['bottom'].set_position(('data', 0))
# ax.yaxis.set_ticks_position('left')
# ax.spines['left'].set_position(('data', 0))

# xlim(X.min() * 1.1, X.max() * 1.1)
# ylim(cosX.min() * 1.1, cosX.max() * 1.1)

# xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
# yticks([-1, 0, +1], [r'$-1$', r'$0$', r'$+1$'])

# t = 2*np.pi/3
# plot([t,t],[0,np.cos(t)], color ='blue',  linewidth=1.5, linestyle="--")
# scatter([t,],[np.cos(t),], 50, color ='blue')
# annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$', xy=(t, np.sin(t)),  xycoords='data',
#          xytext=(+10, +30), textcoords='offset points', fontsize=16,
#          arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

# plot([t,t],[0,np.sin(t)], color ='orange',  linewidth=1.5, linestyle="--")
# scatter([t,],[np.sin(t),], 50, color ='red')
# annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$', xy=(t, np.cos(t)),  xycoords='data',
#          xytext=(-90, -50), textcoords='offset points', fontsize=16,
#          arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

# legend(loc='upper left')

# show()

##########################

# from pylab import * 
# import numpy as np

# X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
# cosX = np.cos(X)
# sinX = np.sin(X)
# coshX = np.cosh(X)
# sinhX = np.sinh(X)

# figure(figsize=(8,6), dpi=80)

# subplot(2, 1, 1)
# plot(X, cosX, color="blue", linewidth=2.0, linestyle="-", label="Cosine")
# subplot(2, 1, 2)
# plot(X, sinX, color="orange", linewidth=2.5, linestyle="--", label="Sine")

# subplot(1, 2, 1)
# plot(X, cosX, color="blue", linewidth=2.0, linestyle="-", label="Cosine")
# subplot(1, 2, 2)
# plot(X, sinX, color="orange", linewidth=2.5, linestyle="--", label="Sine")

# show()

##########################

# from pylab import * 
# import numpy as np

# X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
# cosX = np.cos(X)
# sinX = np.sin(X)
# coshX = np.cosh(X)
# sinhX = np.sinh(X)

# figure(figsize=(8,6), dpi=80)

# subplot(2, 2, 1)
# plot(X, cosX, color="blue", linewidth=2.0, linestyle="-", label="Cosine")
# subplot(2, 2, 2)
# plot(X, sinX, color="orange", linewidth=2.5, linestyle="--", label="Sine")
# subplot(2, 2, 3)
# plot(X, coshX, color="green", linewidth=2.0, linestyle="-.", label="Hyperbolic cosine")
# subplot(2, 2, 4)
# plot(X, sinhX, color="red", linewidth=2.5, linestyle=":", label="Hyperbolic sine")

# show()

##########################

# from pylab import * 
# import numpy as np

# X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
# cosX = np.cos(X)
# sinX = np.sin(X)

# plot (X, cosX, label="Cosine")
# plot(X, sinX, label="Sine")
# legend()
# title("Cosine/Sine plot")
# xlabel("cos/sin")
# ylabel("Result")
# show()

##########################

# from pylab import *

# n = 256
# X = np.linspace(-np.pi, np.pi, n, endpoint=True)
# Y = np.cos(2*X)

# plot (X, Y+1, color='orange', linewidth=3, alpha=1.00)
# fill_between(X, 1, Y+1, color='orange', alpha=.25)

# plot (X, Y-1, color='orange', linewidth=3, alpha=1.00)

# show()

##########################

# from pylab import *

# x = [1, 2, 3, 4, 5, 6, 7]
# y = [10, 56, 45, 25, 19, 45, 67]

# bar(x, y)

# show()

##########################

# from pylab import *

# x = [1, 2, 3, 4, 5, 6, 7]
# y = [10, 56, 45, 25, 19, 45, 67]

# bar(x, y, facecolor='lightblue', edgecolor='blue')

# show()

##########################

# from pylab import *

# x = np.random.randint(1, 10, 50)
# print(x)

# hist(x)

# show()

##########################

# from pylab import *

# x = np.random.randint(1, 10, 50)
# print(x)

# hist(x, bins=5)

# show()

##########################

# from pylab import *

# x = np.random.randint(1, 10, 50)
# print(x)

# hist(x, color="green", edgecolor="darkblue")

# show()

##########################

# from pylab import *

# x = np.random.randint(1, 10, 50)
# print(x)

# hist(x, color="green", edgecolor="darkblue", linewidth=3, hatch='x', orientation='horizontal')

# show()


##########################

# import matplotlib as np
# from pylab import *

# nbVal = 30
# x = np.random.rand(nbVal)
# y = np.random.rand(nbVal)

# scatter(x, y)
# show()

##########################

# import matplotlib as np
# from pylab import *

# nbVal = 30
# x = np.random.rand(nbVal)
# y = np.random.rand(nbVal)

# scatter(x, y, marker='^')
# show()

##########################

# import matplotlib as np
# from pylab import *

# nbVal = 30
# x = np.random.rand(nbVal)
# y = np.random.rand(nbVal)

# scatter(x, y, marker='^', color='orange', edgecolor='blue')
# show()






