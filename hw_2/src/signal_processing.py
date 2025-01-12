"""Signal Processing Exercise""" 
import numpy as np 
import matplotlib.pyplot as plt 
 
 
def analyze_signal(time, clean, noisy):
    #filtraggio
    kernel = np.ones(5) / 5 #ker del moving avg filter
    filtered = np.convolve(noisy, kernel, mode='same') #convoluzione col ker, filtering nel dom tempo

    #fft
    freqs = np.fft.fftfreq(len(time))
    clean_fft = np.abs(np.fft.fft(clean))
    noisy_fft = np.abs(np.fft.fft(noisy))
    filtered_fft = np.abs(np.fft.fft(filtered))

    #subplot
    fig, axes = plt.subplots(2, 1, figsize=(10, 6))  # 2 rows, 1 column as per original code

    #dom tempo
    axes[0].plot(time, clean, label='Clean')
    axes[0].plot(time, noisy, label='Noisy')
    axes[0].plot(time, filtered, label='Filtered')
    axes[0].set_title('Time Domain')
    axes[0].set_xlabel("Time")
    axes[0].set_ylabel("Amplitude")
    axes[0].legend()

    #dom freq
    axes[1].plot(freqs, clean_fft, label='Clean')
    axes[1].plot(freqs, noisy_fft, label='Noisy')
    axes[1].plot(freqs, filtered_fft, label='Filtered')
    axes[1].set_title('Frequency Domain')
    axes[1].set_xlabel("Frequency")
    axes[1].set_ylabel("Magnitude")
    axes[1].legend()

    plt.tight_layout()
    plt.show()
    print("Plot fatto")

pass

