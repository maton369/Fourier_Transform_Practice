import numpy as np
import matplotlib.pyplot as plt

# テストデータの生成
N = 1000
ts = 0.0
te = 1.0
t = np.linspace(ts, te, N)

x = (
    1.0 * np.sin(2.0 * np.pi * 100.0 * t)
    + 0.5 * np.cos(2.0 * np.pi * 10.0 * t)
    + 0.05 * np.random.randn(N)
)

# DFT
X = np.fft.fft(x)
dt =t[1] - t[0]  # 時間刻み
f = np.fft.fftfreq(N, dt)  # 周波数軸

# データをプロット
fig, (ax01, ax02) = plt.subplots(nrows=2, figsize=(6, 8))
plt.subplots_adjust(wspace=0.0, hspace=0.6)

# 時間領域信号
ax01.set_xlabel("time (s)")
ax01.set_ylabel("x")
ax01.plot(t, x)

# 周波数領域（振幅スペクトル）
ax02.set_xlabel("frequency (Hz)")
ax02.set_ylabel("|X|/N")
ax02.plot(f, np.abs(X) / N)

plt.show()
