import sys, os
INTERP = os.path.join(os.environ['HOME'], 'chess.chadgh.com', 'bin', 'python')
if sys.executable != INTERP:
	os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())
from chess.app import app as application

if True: # debug
	from werkzeug.debug import DebuggedApplication
	application = DebuggedApplication(application, evalex=True)
