#PLOTTING
dataREF='https://stackoverflow.com/questions/6365623/improving-fft-performance-in-python'
import numpy as np 
import matplotlib.pyplot as plt  
data=np.loadtxt("fft_computation_time.data")
x=data[:,0]
y=data[:,1]
labels=['padded_fft','numpy_fft', 'scipy_fft', 'czt','fftw_fft']
markers=['-s','-o','-v','-x','-*']
colors=['r','k','b','g','y']

#my_xticks = ['20000 prime=False','20011 prime=True','21803 prime=True','21804 prime=False','21997 prime=True','32768 prime=False']  
xv=(x[0],x[5],x[10],x[15],x[20],x[25])
#plt.xticks(xv, my_xticks)

for i in range(0,5):
        #plt.plot((x[0+i],x[5+i],x[10+i],x[15+i],x[20+i],x[25+i]),(y[0+i],y[5+i],y[10+i],y[15+i],y[20+i],y[25+i]),markers[i],label=labels[i])
        plt.plot(xv,(y[0+i],y[5+i],y[10+i],y[15+i],y[20+i],y[25+i]),markers[i],label=labels[i])

plt.legend()    
  
plt.ylabel("Computation Time (s)")        
plt.xlabel("Number of Elements")
plt.title("FFT Computation Time")
plt.savefig("FFT_Computation_Time_v1.pdf")
plt.show()
