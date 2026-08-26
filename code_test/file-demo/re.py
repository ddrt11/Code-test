import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, clear_output

# ==========================
# 1. 参数设置
# ==========================
L = 1.0                  # 正方形边长 (m)
Nx = 50                  # x方向网格数
Ny = 50                  # y方向网格数
alpha = 0.01             # 热扩散系数 (m^2/s)

T_top = 100.0            # 上边界温度 (℃)
T_bottom = 0.0           # 下边界温度 (℃)
T_init = 20.0            # 初始温度 (℃)

total_time = 60.0        # 总模拟时间 (s)

# 网格间距
dx = L / Nx
dy = L / Ny

# 显式格式稳定性条件（留安全裕量）
dt = 0.25 * (dx**2 * dy**2) / (alpha * (dx**2 + dy**2))

# 时间步数
Nt = int(total_time / dt)

# ==========================
# 2. 初始化温度场（带Ghost Cell）
# ==========================
# 实际数组大小：(Ny+2) × (Nx+2)
T = np.ones((Ny + 2, Nx + 2)) * T_init

# 设置上下边界
T[0, :] = T_bottom
T[-1, :] = T_top

# 创建绘图
fig, ax = plt.subplots(figsize=(6, 5))
im = ax.imshow(
    T[1:-1, 1:-1],
    origin='lower',
    extent=[0, L, 0, L],
    cmap='hot',
    vmin=0,
    vmax=100
)
plt.colorbar(im, ax=ax, label='Temperature (℃)')
title = ax.set_title("Temperature Field")

# ==========================
# 3. 时间推进
# ==========================
plot_interval = max(1, Nt // 100)

for n in range(Nt):

    # 左右绝热边界（Ghost Cell）
    T[:, 0] = T[:, 1]
    T[:, -1] = T[:, -2]

    # 上下固定温度边界
    T[0, :] = T_bottom
    T[-1, :] = T_top

    # 保存旧温度场
    T_new = T.copy()

    # 显式有限差分更新
    T_new[1:-1, 1:-1] = T[1:-1, 1:-1] + alpha * dt * (
        (T[1:-1, 2:] - 2 * T[1:-1, 1:-1] + T[1:-1, :-2]) / dx**2 +
        (T[2:, 1:-1] - 2 * T[1:-1, 1:-1] + T[:-2, 1:-1]) / dy**2
    )

    T = T_new

    # 动态显示
    if n % plot_interval == 0 or n == Nt - 1:
        current_time = (n + 1) * dt
        im.set_array(T[1:-1, 1:-1])
        title.set_text(f"Temperature at t = {current_time:.2f} s")
        clear_output(wait=True)
        display(fig)

plt.close()
print("模拟完成！")