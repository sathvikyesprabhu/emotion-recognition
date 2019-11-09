from biosspy.signals import ecg

def post_processing(data):
  signal = ecg.ecg(signal=data, sampling_rate=256.0, show=False)
  processed_signal = ecg.correct_rpeaks(signal=data, rpeaks=out[3], sampling_rate=256.0)
  wd, m = hp.process(signal[1], 256.0)

if __name__ == "__main__":
  plt.figure(figsize=(20, 4))
  hp.plotter(wd, m)