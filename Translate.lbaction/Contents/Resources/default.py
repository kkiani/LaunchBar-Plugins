import goslate
import sys


arguments = ' '.join(sys.argv[1:])
scriptOutput = []


def translte(){
	gs = goslate.Goslate()
	result = gs.translate('arguments', 'fa')
	scriptOutput.append({'title' : result, 'icon' : 'DuckDuckGo'})
}

translte()