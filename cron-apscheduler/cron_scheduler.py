from apscheduler.schedulers.blocking import BlockingScheduler

def job () :
    print("this is cron trigger scheduler")
    
scheduler = BlockingScheduler()
scheduler.add_job(job,trigger="cron",second="*/10")
scheduler.start()
