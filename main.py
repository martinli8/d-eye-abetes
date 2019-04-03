import os
import PySpin
import camAc
def main() :

    testF() ;
    spinStp() ;
    setupCam() ;


    clearCam




def testF() :
    ## Creates a test file to make sure python has access to current directory
    try:
        test_file = open('test.txt', 'w+')
    except IOError:
        print 'Unable to write to current directory. Please check permissions.'
        raw_input('Press Enter to exit...')
        return False

        test_file.close()
        os.remove(test_file.name)

        result = True

def spinStp() :
    ## Sets up PySpin

    # Retrieve singleton reference to system object
    system = PySpin.System.GetInstance()
    # Get current library version
    version = system.GetLibraryVersion()
    #print 'Library version: %d.%d.%d.%d' % (version.major, version.minor, version.type, version.build)
    # Retrieve list of cameras from the system
    cam_list = system.GetCameras()
    num_cameras = cam_list.GetSize()

    if num_cameras == 0:
        cam_list.Clear()
        system.ReleaseInstance()
        #print 'Not enough cameras!'
        return False
    else :
        return cam_list


def setupCam(cam_list) :
    cam = cam_list[0]
    try:
        result = True
        # Retrieve TL device nodemap and print device information
        nodemap_tldevice = cam.GetTLDeviceNodeMap()
        #result &= print_device_info(nodemap_tldevice)
        # Initialize camera
        cam.Init()
        # Retrieve GenICam nodemap
        nodemap = cam.GetNodeMap()

        #Run application
        camAc.runApp(cam, nodemap, nodemap_tldevice)
        # Acquire images
        #result &= camAc.acquire_images(cam, nodemap, nodemap_tldevice)
        # Deinitialize camera
        cam.DeInit()

    except PySpin.SpinnakerException as ex:
        print 'Error: %s' % ex
        result = False

    return result


def clearCam(cam) :
    del cam
    # Clear camera list before releasing system
    cam_list.Clear()
    # Release system instance
    system.ReleaseInstance()
    return False



if __name__ == '__main__':
    main()
