from Python_Problems import joseph


def test_kill_people():

    assert joseph.kill_people(total=10,killing_position=2,start=1,kill_direction='r') == 8