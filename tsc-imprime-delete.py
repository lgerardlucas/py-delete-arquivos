from os import *
import os
def listar_arquivos(caminho=None):
    for arq in listdir(caminho):
    	if len(arq) == 14:
	    print(caminho+'/'+arq)
	    if os.path.exists(caminho+'/'+arq):
            	os.remove(caminho+'/'+arq)

if __name__ == '__main__':
    arquivos = listar_arquivos(caminho="/opt/Trabin-Software/TSC-Trabin/Pedidos/PEDIDO01-Pedidos/Fila-de-Impressao" )
