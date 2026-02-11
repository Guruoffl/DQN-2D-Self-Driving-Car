def decide(sensor_values):
    left, center, right = sensor_values

    if left < 0.15 and center < 0.15 and right < 0.15:
        return "SLOW_FORWARD"

    if center > 0.4:
        if left - right > 0.15:
            return "RIGHT"   
        elif right - left > 0.15:
            return "LEFT"   
        else:
            return "FORWARD"

    
    if left > right:
        return "LEFT"
    else:
        return "RIGHT"