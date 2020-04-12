from Queue.queue import Queue
import random


class Printer(object):
  def __init__(self, ppm):
    self.pagerate = ppm
    self.currenttask = None
    self.timeremaining = 0

  def tick(self):
    """
    Decrements internal timer and set the printer to idle if the task is completed
    :return:
    """
    if not self.currenttask is None:
      self.timeremaining = self.timeremaining - 1
      if self.timeremaining <= 0:
        self.currenttask = None

  def busy(self):
    if not self.currenttask is None:
      return True
    return False

  def startNext(self, newtask):
    self.currenttask = newtask
    self.timeremaining = newtask.getPages() * 60/self.pagerate


class Task(object):
  def __init__(self, time):
    self.timestamp = time
    self.pages = random.randrange(1, 21)

  def getStamp(self):
    return self.timestamp

  def getPages(self):
    return self.pages

  def waitTime(self, currenttime):
    return currenttime - self.timestamp

def newPrintTask():
  """
  Twenty tasks per hour means that on average there will be one task every 180 seconds:
  :return:
  """
  num = random.randrange(1, 181)
  if num is 180:
    return True
  return False


def simulation(numSeconds, pagesPerMinute):
  labprinter = Printer(pagesPerMinute)
  printqueue = Queue()

  waitingtimes = list()

  for currentsecond in range(numSeconds):
    if newPrintTask():
      task = Task(currentsecond)
      printqueue.enqueue(task)

    if (not labprinter.busy()) and (not printqueue.isEmpty()):
      nexttask = printqueue.dequeue()
      waitingtimes.append(nexttask.waitTime(currentsecond))
      labprinter.startNext(nexttask)

    labprinter.tick()

  averageWait = sum(waitingtimes)/len(waitingtimes)
  print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait, printqueue.size()))


for i in range(10):
  simulation(3600, 10)