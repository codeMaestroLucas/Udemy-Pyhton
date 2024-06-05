from log import LogFileMixin, LogPrintMixin
from eletronic import Tv

lp = LogPrintMixin()
lp.log_error('trying to log.')
lp.log_sucess('trying to log.')

lf = LogFileMixin()
lf.log_error('trying to log.')
lf.log_sucess('trying to log.')

tv = Tv('Samsung Tv')
tv.turn_off()
tv.turn_on()
tv.log_error('trying to log.')
tv.log_sucess('trying to log.')
tv.turn_off()