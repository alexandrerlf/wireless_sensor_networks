import json
import utills
from packet import packet
from time import sleep

def analise(routerList,argv):
  data = utills.parseJson(argv)
  for flow in data["flows"]:
    for i in routerList: # i é um roteador
      if(i.ID == flow["target"]): # acha o roteador da vez
        i.AllHellou()#hellou para que cada host saiba quem pe seu vizinho 
        #-----------envio da msg do test flow--------------
        for j in i.hostList: # j é um host do roteador i
          if(j.ID == flow["source"]):
            for count in range(flow["amount"]):
              # sleep(flow["start"]) # tempo de espera da simulação
              dado = packet(flow["source"],flow["destination"],str(count))#encapsula o pacote
              j.send(dado.destination,dado) #faz o envio do pacote
              # j.send(flow["destination"],flow["source"]+str(count))
              if(not j.CheckEnergy()): #verifica se acabou a energia
                i.AllHellou()
            break
        break
