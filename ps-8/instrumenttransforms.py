import numpy as np
import matplotlib.pyplot as plt
num_coefficients = 10000
def read_waveform_from_file(file_path):
    with open(file_path, 'r') as file:
        waveform = np.loadtxt(file)
    return waveform

def plot_fft_magnitude(waveform, num_coefficients):
    # Perform FFT
    fft_result = np.fft.fft(waveform)
    
    # Take magnitude of coefficients
    magnitude = np.abs(fft_result)[:num_coefficients]

    # Plot magnitude
    plt.figure(figsize=(10, 6))
    plt.plot(magnitude)
    plt.title('FFT Magnitude of Waveform (trumpet)')
    plt.xlabel('Coefficient Index')
    plt.ylabel('Magnitude')
    plt.grid(True)
    print(np.where(magnitude==max(magnitude)))
    plt.show()

if __name__ == "__main__":
    file_path = 'trumpet.txt'
    waveform = read_waveform_from_file(file_path)
    plot_fft_magnitude(waveform, num_coefficients)