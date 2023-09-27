import time
import android

# ایجاد یک شیء از کلاس Android
droid = android.Android()

while True:
    try:
        # درخواست موقعیت موس
        mouse_position = droid.readLocation()

        # اگر موقعیت موس در دسترس باشد
        if mouse_position.result:
            x = mouse_position.result["gps"]["latitude"]
            y = mouse_position.result["gps"]["longitude"]
            print(f"موقعیت موس: x={x}, y={y}")
    except Exception as e:
        print(f"Error: {e}")

    time.sleep(1)  # منتظر یک ثانیه بمانید تا موقعیت موس به‌روز شود
