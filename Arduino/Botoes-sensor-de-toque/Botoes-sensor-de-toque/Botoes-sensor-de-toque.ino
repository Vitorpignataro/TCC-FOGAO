#include <CapacitiveSensor.h>

CapacitiveSensor ligaFogao = CapacitiveSensor(3, 2);
CapacitiveSensor aumentaTemp = CapacitiveSensor(6, 5);
CapacitiveSensor diminuiTemp = CapacitiveSensor(9, 8);


int valorMIN = 2400;



void setup() {
  Serial.begin(9600);
}

void loop() {
 
  long valorLiga = ligaFogao.capacitiveSensor(30);
  long valorAume = aumentaTemp.capacitiveSensor(30);
  long valorDimi = diminuiTemp.capacitiveSensor(30);
  
  
  if (valorLiga > valorMIN) {
    Serial.println("FogaoLigado");
  }
  else{
    Serial.println("BotaoOFF");
  }
  
  if (valorAume > valorMIN) {
    Serial.println("Aumenta");
  }
  else{
    Serial.println("BotaoOFF");
  }
  
  if (valorDimi > valorMIN) {
    Serial.println("Diminui");
  }
  else{
    Serial.println("BotaoOFF");
  }

  

  delay(200);
}
