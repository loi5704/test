import matplotlib.pyplot as plt
x = [1,2,3,4]  #Step 1
y = [10,20,25,30] 
fig = plt.figure() #Step 2
ax = fig.add_subplot(111) #Step 3
ax.plot(x, y, color= 'lightblue', linewidth=3)  #Step 3, 4
ax.scatter([2,4,6],
          [5,15,25],
          color= 'darkgreen',
          marker= '^' )
ax.set_xlim(1, 6.5)
plt.plot(x, x, x, x**2, x, x** 3)
ax.plot(x, y, alpha = 0.4)
ax.plot(x, y, c= 'k')
fig.colorbar(im, orientation= 'horizontal')
im = ax.imshow(img,
            cmap= 'seismic' )
plt.show()