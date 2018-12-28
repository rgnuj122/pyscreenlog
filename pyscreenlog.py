#-- include('examples/showgrabfullscreen.py') --#
# import pyscreenshot as ImageGrab
from PIL import ImageGrab
import sched, time, os
if __name__ == '__main__':
    interval_time=1
    if not os.path.exists('./screenshots'):
        os.mkdir("screenshots")



    # https://stackoverflow.com/questions/474528/what-is-the-best-way-to-repeatedly-execute-a-function-every-x-seconds-in-python
    s = sched.scheduler(time.time, time.sleep)
    def do_something(sc):
        # print "Doing stuff..."

        timestr=time.strftime("%Y%m%d-%H%M%S")
        print("take a snapshot: {}".format(timestr.split('-')[1]))
        fn=os.path.join('screenshots','screenshot_'+timestr+'.png')
        # grab fullscreen
        im = ImageGrab.grab()
        im.save(fn)
        # do your stuff
        s.enter(interval_time, 1, do_something, (sc,))
    s.enter(interval_time, 1, do_something, (s,))
    s.run()
    # save image file


    # show image in a window
    # im.show()
#-#
