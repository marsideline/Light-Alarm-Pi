#!/usr/bin/env python

import scrollphathd
import time

# Declaration of constants
LUMINANCE_RESOLUTION = 0.01
BRIGHTNESS_INCREASE_CYCLE_SEC = 15

#
# Main routine
#
try:
    # Brighten the LED module little by little to express the sunrise.
    # minimum x value should be 9
    # because it is the value that becomes the minimum illuminance
    # that the LED lights up.
    for x in range(9, 101):
        scrollphathd.fill(x * LUMINANCE_RESOLUTION, 0, 0, 18, 7)
        scrollphathd.show()
        time.sleep(BRIGHTNESS_INCREASE_CYCLE_SEC)

    # Maintain maximum brightness for a while
    time.sleep(60)
    scrollphathd.fill(0)
    scrollphathd.show()

except KeyboardInterrupt:
    scrollphathd.fill(0)
    scrollphathd.show()