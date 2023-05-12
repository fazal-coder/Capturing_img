import numpy as np
import cv2
import multiprocessing
import schedule
import datetime


def get_images(current_time):
        width, height, num_images=800, 800, 4
        
        blue_images = []

        for i in range(num_images):
            image = np.zeros((height, width, 4), dtype=np.uint8)
            image[:,:,i] = 255
            #file path
            filename = f"C:\\Users\\AI-Team\\Desktop\\num\\Saveblue\\{current_time}.png"
            cv2.imwrite(filename, image)
            blue_images.append(image)
        return blue_images


current_time = datetime.datetime.now().strftime("%H_%M_%S")
#print(current_time)
#get_blue_images(current_time)

def start():
      chan1 = multiprocessing.Process()
      chan2 = multiprocessing.Process()

      chan1.start()
      chan2.start()

      chan1.join()
      chan2.join()


      schedule.every(1).second.do(start)


while True:
      schedule.run_pending()
