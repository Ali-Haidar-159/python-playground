from apscheduler.schedulers.blocking import BlockingScheduler

def job() :
    print("Hello World")


scheduler = BlockingScheduler()
scheduler.add_job(job,"interval",seconds=5)
scheduler.start()