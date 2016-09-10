import middleware as mw

#-----------------------------------------------------------------------------#
# Declataion                                                                  #
#-----------------------------------------------------------------------------#

FRONT_THRESHOLD = 100	# 臒l(�O��)
LEFT_THRESHOLD = 100	# 臒l(����)
RIGHT_THRESHOLD = 100	# 臒l(�E��)

#-----------------------------------------------------------------------------#
# Function                                                                    #
#-----------------------------------------------------------------------------#
def check_wall_front():
    """ �����Z���T1,2���O���ɕǂ����邩�ǂ����`�F�b�N����
    """
    info = mw.sensorinfo()
    print info[0],info[1],info[2],info[3]
    average = (info[1] + info[2]) / 2
    if average > FRONT_THRESHOLD:
        return 1	# �ǂ���
    else:
        return 0	# �ǂȂ�

def check_wall_left():
    """ �����Z���T0��荶���ɕǂ����邩�ǂ����`�F�b�N����
    """
    info = mw.sensorinfo()
    if info[0] > LEFT_THRESHOLD:
        return 1	# �ǂ���
    else:
        return 0	# �ǂȂ�

def check_wall_right():
    """ �����Z���T3���E���ɕǂ����邩�ǂ����`�F�b�N����
    """
    info = mw.sensorinfo()
    if info[3] > RIGHT_THRESHOLD:
        return 1	# �ǂ���
    else:
        return 0	# �ǂȂ�

#-----------------------------------------------------------------------------#
# Test                                                                        #
#-----------------------------------------------------------------------------#
def test_recognize():
    """ �ǂ���/�Ȃ��`�F�b�N�����{��LED��_������ 
    """	
    led_state = [0,0,0,0]
    print "Type ctrl+C to stop"
    while True:
	# LED_0�_��
        led_state[0] = 1
	# �O���ǃ`�F�b�N(�ǂ���:LED_1�_��)
        if check_wall_front() == 1:
            led_state[1] = 1
        else:
            led_state[1] = 0
	# �����ǃ`�F�b�N(�ǂ���:LED_2�_��)
        if check_wall_left() == 1:
            led_state[2] = 1
        else:
            led_state[2] = 0
        # �E���ǃ`�F�b�N(�ǂ���:LED_3�_��)
        if check_wall_right() == 1:
            led_state[3] = 1
        else:
            led_state[3] = 0
        # LED�ݒ�
        mw.led(led_state)

if __name__ == '__main__':
    test_recognize()
    
