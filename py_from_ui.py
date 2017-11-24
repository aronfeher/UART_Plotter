from PyQt5 import uic

fin = open('mainwindow.ui', 'r')
fout = open('mainwindow_alt.py', 'w')
uic.compileUi(fin, fout, execute=False)
fin.close()
fout.close()
