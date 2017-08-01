
from docstringtest.examples.goodclass import GoodClass
import docstringtest

def test_generateAllDocstrings_class():
	docstrings = docstringtest.generateAllDocstrings(GoodClass)
	expected = [
	 '------------------------------',
	 '__init__',
	 '"""',
	 ':param varA: description',
	 ':param varB: description',
	 ':param varC: description',
	 ':type varA: type description',
	 ':type varB: type description',
	 ':type varC: type description',
	 '"""',
	 '------------------------------',
	 '_shouldBeIgnored',
	 '"""',
	 ':param varA: description',
	 ':param varB: description',
	 ':type varA: type description',
	 ':type varB: type description',
	 '"""',
	 '------------------------------',
	 'basicMethod',
	 '"""',
	 ':param varA: description',
	 ':param varB: description',
	 ':type varA: type description',
	 ':type varB: type description',
	 '"""',
	 '------------------------------',
	 'basicMethodWithReturn',
	 '"""',
	 ':param varA: description',
	 ':param varB: description',
	 ':type varA: type description',
	 ':type varB: type description',
	 ':return: return description',
	 ':rtype: the return type description',
	 '"""',
	 '------------------------------',
	 'basicMethodWithYield',
	 '"""',
	 ':param varA: description',
	 ':param varB: description',
	 ':type varA: type description',
	 ':type varB: type description',
	 ':return: return description',
	 ':rtype: the return type description',
	 '"""',
	 '------------------------------',
	 'staticMethod',
	 '"""',
	 ':param varA: description',
	 ':type varA: type description',
	 '"""',
	 '------------------------------',
	 'staticMethodNoVariables',
	 '"""',
	 '',
	 '"""',
	 '------------------------------',
	 'staticMethodNoVariablesWithReturn',
	 '"""',
	 ':return: return description',
	 ':rtype: the return type description',
	 '"""',
	 '------------------------------',
	 'staticMethodNoVariablesWithYield',
	 '"""',
	 ':return: return description',
	 ':rtype: the return type description',
	 '"""',
	 '------------------------------',
	 'staticMethodWithReturn',
	 '"""',
	 ':param varA: description',
	 ':type varA: type description',
	 ':return: return description',
	 ':rtype: the return type description',
	 '"""',
	]
	assert docstrings.split('\n') == expected


