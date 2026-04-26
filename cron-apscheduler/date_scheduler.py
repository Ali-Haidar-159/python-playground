from apscheduler.schedulers.blocking import BlockingScheduler

def job() :
    print("this is job with date scheduler")
    
scheduler = BlockingScheduler()
scheduler.add_job(job,trigger="date")
scheduler.start()