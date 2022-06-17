from fileinput import close
from pydoc import doc
from turtle import clear
import vglobals

def read_demanda():
    doc = open(vglobals.dirdoc)
    create_dic(doc)
    doc.close()

def create_dic(doc):
    vglobals.dic_demanda.clear()

    doc_l = rdline(doc)
    docsl = lnsplit(doc_l)

    '''
    Configuracion del documento 
    pos 0 -> País
    pos 1 -> Fecha
    pos 2 -> Generacion
    pos 3 -> Consumo
    pos 4 -> Consumo por capita
    '''
    
    # Atendiendo a la configuracion extraeremos los datos
    for line in docsl:
        pais = line[0]
        fecha = line[1]
        generacion = line[2]
        consumo = line[3]
        consumo_cp = line[4]

        vglobals.dic_demanda[(pais,fecha)] = (generacion,consumo,consumo_cp)
    
    


def rdline(doc):
    lines = str.split(doc,"\n")
    return lines

def lnsplit(lines):
    doc = []
    for line in lines:
        val = str.split(line,"\n|\t")
        doc.append(val)