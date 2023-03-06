from src.schedule.decorators import logger, schedule
from src.logic.app import App
from os import getenv


@schedule(int(getenv('PERIOD_TIME')))
@logger
def refresh_offer(app: App):
    app.refresh_offers()