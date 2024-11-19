from machine import Pin, PWM
import time

# Configurar el pin del servo
servo_pin = Pin(0)  # Cambia este número según tu conexión
pwm = PWM(servo_pin)
pwm.freq(50)  # Frecuencia típica para servos

def set_angle(angle):
    duty = int((angle / 180) * 102 + 26)  # Mapeo de ángulo a duty cycle
    pwm.duty_u16(duty)

try:
    while True:
        for angle in range(0, 180, 5):  # De 0 a 180 grados
            set_angle(angle)
            time.sleep(0.1)
        for angle in range(180, 0, -5):  # De 180 a 0 grados
            set_angle(angle)
            time.sleep(0.1)
except KeyboardInterrupt:
    pwm.deinit()  # Detener PWM al finalizar
