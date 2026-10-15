class Sensore:
    def __init__(self,codice,grandezza,unita,soglia_massima)
        self.codice = codice
        self.grandezza = grandezza
        self.unita = unita
        self.soglia_massima = soglia_massima
        

class Satellite
    def __init__(self , nome)
        self.nome
        self.sensori = {}
        self.letture = []
        
    def aggiungi_sensore(self , sensore)
        if sensore.codice in self.sensori:
                raise ValueError("codice sensore gia presente")
        self.sensori[sensore.codice] = sensore
        
    def registra_lettura(self , codice_sensore , valore)
        if codice_sensore not in self.sensori:
            raise KeyError("Sensore nonh registrato: " + cocide_sensore)
        sensore = self.sensori[codice_sensore]
        self.lettura.append({
            "sensore": codice_sensore,
            "grandezza":sensore.grandezza,
            "valore":valore,
            "unita": sensore.unita,
            "allarme": valore>sensore.soglia_massima
        })
        
    def letture_in_allarme(self)
        allarmi = []
        for lettura in self.letture
            if lettura["allarme"]:
                allarmi.append(lettura)
            return allarmi
        
    def riepilogo(self)
        print("Telemetria satellite:", self.nome)
        for lettura in self.letture:
            stato = "ALLARME" if lettura["allarme"] else "OK"
            print(lettura["sensore"], lettura["valore"], lettura["unita"], stato)