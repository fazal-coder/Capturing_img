import multiprocessing
import datetime
import numpy as np
import cv2
import schedule


only_store = True

def get_blue(now_time):
    width, height, count_img = 800, 800, 2
    blueimg = []
    for i in range(count_img):
        img = np.zeros((height, width, 3), dtype=np.uint8)
        img[:,:,i] = 255
        filename = f"C:\\Users\\AI-Team\\Desktop\\num\\Saveblue\\{now_time}_{i}.png"
        cv2.imwrite(filename, img)
        blueimg.append(img)
    return blueimg

def store_On():
    global only_store
    only_store = True

def store_Off():
    global only_store
    only_store = False

def capturing(param):
    if param:
        now_time = datetime.datetime.now().strftime("%H_%M_%S")
        get_blue(now_time)

if __name__ == "__main__":
    multiprocessing.freeze_support()

    print("start programming "+ datetime.datetime.now().strftime("%H:%M:%S"))
    
    schedule.every().day.at("21:41").do(store_On)
    schedule.every().day.at("23:00").do(store_Off)

    
    def start():
            chan1 = multiprocessing.Process(target=capturing, args=(only_store,))
            chan2 = multiprocessing.Process(target=capturing, args=(only_store,))

            chan1.start()
            chan2.start()

            chan1.join()
            chan2.join()
    
    
    schedule.every(1).second.do(start)
    while True:
        schedule.run_pending()


