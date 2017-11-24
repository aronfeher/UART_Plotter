import serial
import time

port_num = 'COM8'
baud = 115200
receive_packet = bytearray([0xF1, 0x05, 0x00, 0x00, 0xF3, 0x0D, 0x0A])
send_packet = bytearray([0xF2, 0x07, 0xFF, 0xFF, 0xFF, 0xFF, 0xF3, 0x0D, 0x0A])

ser = serial.Serial(port=port_num, baudrate=baud)
send_data = False
quit_prog = False

timer = 0

while ser.is_open is True:
    if ser.in_waiting > 0:
        rec = ser.readline()
        if rec[3] == 0x32:
            print("Start received")
            send_data = True
        if rec[3] == 0x31:
            print("Stop received")
            send_data = False
            ser.close()
    if send_data is True:
        if timer < 10:
            send_packet[2] = 0x00
            send_packet[3] = 0x00
        else:
            send_packet[2] = 0xFF
            send_packet[3] = 0xFF

        timer = timer + 1

        if timer >= 20:
            timer = 0


        ser.write(send_packet)
        print(str(send_packet[2] * 8 + send_packet[3]) + " Sent")
        time.sleep(0.1)

def animate():
    global a1
    global plt_array1
    a1.clear()
    a1.plot(plt_array1)
