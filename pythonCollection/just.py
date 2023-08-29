import os
import sys

m_path = os.getcwd()


print(os.getcwd())

path = os.path.abspath("pythonCollection")
print(path)
print(os.path.exists(path))
sys.path.append(path)

excel_path = r'media/output/test.xlsx'
#os.remove(excel_path)
