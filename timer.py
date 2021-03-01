import time

startTime = time.time()

print("main program")

time.sleep(3)

print("durée: %.2f secondes" % (time.time() - startTime))

penalty = 2
print("durée totale: %.2f secondes" % (time.time() - startTime + penalty))
