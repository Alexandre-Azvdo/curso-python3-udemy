from log import LogFileMixin, LogPrintMixin


lp = LogPrintMixin()
lp.log_error('Log não executado')
lp.log_success('Log bem sucedido')
lf = LogFileMixin()
lf.log_error('Log não executado')
lf.log_success('Log bem sucedido')
