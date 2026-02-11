def compute_reward(on_road, speed, brake, sensors=None):
    """
    Reward function for 5-sensor autonomous driving
    sensors = [far_left, left, center, right, far_right]
    """

    if not on_road:
        return -100

    reward = 1.0  

    reward += speed * 0.1

    if speed < 0.1:
        reward -= 1.0

    if sensors is not None and len(sensors) == 5:
        far_left, left, center, right, far_right = sensors

        danger = 0
        if far_left < 0.25:
            danger += 1
        if left < 0.25:
            danger += 1
        if right < 0.25:
            danger += 1
        if far_right < 0.25:
            danger += 1

        reward -= danger * 0.4

        center_balance = abs(left - right)
        reward -= center_balance * 0.3

    return reward