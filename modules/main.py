# main.py -- put your code here!

from system.scheduler import scheduler
from system.hexpansion.app import HexpansionManagerApp
from system.notification.app import NotificationService
from system.launcher.app import Launcher

from frontboards.twentyfour import TwentyTwentyFour

# Start front-board interface
scheduler.start_app(TwentyTwentyFour())

# Start expansion interface
scheduler.start_app(HexpansionManagerApp())

# Start root app
scheduler.start_app(Launcher(), foreground=True)

# Start notification handler
scheduler.start_app(NotificationService(), always_on_top=True)

scheduler.run_forever()
