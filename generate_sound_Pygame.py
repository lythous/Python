import pygame
import numpy as np
import matplotlib.pylab as plt          # Plot is not necessary and can be commented.
from matplotlib import interactive      
interactive(True)                       # Need PyQt5 to create an independent window for plot

# Some functions to generate sound waves easier:
def sine(t, freq):
    return np.sin(t*freq*2*np.pi)

def exp(t, dec):
    return np.exp(t/dec)

def zero(t):
    return np.zeros(t.size)

def noise(t):
    return np.random.rand(t.size)

def delay(t, wave, d):
    print(wave.size)
    delay_samples = np.where(t>=d)[0][0]
    new_wave = np.concatenate((np.zeros(delay_samples), wave))
    new_wave = np.delete(new_wave, range(wave.size-delay_samples, wave.size))
    return new_wave

t_end = 10                              # End time
sr = 44100                              # Sample rate
t = np.linspace(0, t_end, t_end*sr)     # Generate time array

# Generate some sound wave
wave = zero(t)
wave += 20*sine(t, 1000)*exp(t, -2)
wave += 10*sine(t, 500)*(1+sine(t, 1))*exp(t, -1)
wave += 0.2*exp(t, -3)*delay(t, wave, 1)

wave = np.stack((wave, wave))           # 2 Dimensional array for 2 channels of stero sound
wave = wave.T                           # Array shape must be Nx2
wave = wave.copy(order='C')             # NP array to be fed to Pygame must be "Contiguous layout"
plt.plot(t, wave.T[0])                  # Plot one of wave channels
wave = wave.astype('int8')              # Array to be fed to Pygame must be integer and between -127...+127

pygame.mixer.init()                     # Initial pygame sound mixer
sound = pygame.sndarray.make_sound(wave)    # Create sound object
sound.play()                            # Play sound object
