
.. getthecode:: fft.py
    :language: python


========================
 Fast Fourier Transform
========================

This examples shows how to compute a FFT of a signal using the Scientific Python package.


.. code-block:: python

    import numpy as np
    
    from scipy import signal
    from scipy.fftpack import fft
    
    import matplotlib.pyplot as plt
    


We will first compute the spectrum of the sum of two sinusoidal waveforms.


.. code-block:: python

    N = 1000 # number of sample points
    dt = 1. / 500 # sample spacing
    
    frequency1 = 50.
    frequency2 = 80.
    
    t = np.linspace(0.0, N*dt, N)
    y = np.sin(2*np.pi * frequency1 * t) + .5 * np.sin(2*np.pi * frequency2 * t)
    
    yf = fft(y)
    tf = np.linspace(.0, 1./(2.*dt), N/2)
    spectrum = 2./N * np.abs(yf[0:N/2])
    
    figure1 = plt.figure(1, (20, 10))
    plt.plot(tf, spectrum, 'o-')
    plt.grid()
    for frequency in frequency1, frequency2:
        plt.axvline(x=frequency, color='red')
    plt.title('Spectrum')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Amplitude')
    


.. image:: fft-sum-of-sin.png
  :align: center


Now we will compute the spectrum of a square waveform.

The Fourier series is given by:

.. math::

  \frac{4}{\pi} \sum_{n=1, 3, 5, \ldots}^{\inf} \frac{1}{n} \sin(n 2\pi f t)


.. code-block:: python

    N = 1000 # number of sample points
    dt = 1. / 1000 # sample spacing
    
    frequency = 5.
    
    t = np.linspace(.0, N*dt, N)
    y = signal.square(2*np.pi*frequency*t)
    
    figure2 = plt.figure(2, (20, 10))
    
    plt.subplot(211)
    plt.plot(t, y)
    y_sum = None
    for n in range(1, 20, 2):
        yn = 4/(np.pi*n)*np.sin((2*np.pi*n*frequency*t))
        if y_sum is None:
            y_sum = yn
        else:
            y_sum += yn
        if n in (1, 3, 5):
            plt.plot(t, y_sum)
    plt.plot(t, y_sum)
    plt.xlim(0, 2/frequency)
    plt.ylim(-1.5, 1.5)
    
    yf = fft(y)
    tf = np.linspace(.0, 1./(2.*dt), N/2)
    spectrum = 2./N * np.abs(yf[0:N/2])
    
    plt.subplot(212)
    plt.plot(tf, spectrum)
    n = np.arange(1, 20, 2)
    plt.plot(n*frequency, 4/(np.pi*n), 'o', color='red')
    plt.grid()
    plt.title('Spectrum')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Amplitude')
    


.. image:: fft-square-waveform.png
  :align: center


.. code-block:: python

    plt.show()

