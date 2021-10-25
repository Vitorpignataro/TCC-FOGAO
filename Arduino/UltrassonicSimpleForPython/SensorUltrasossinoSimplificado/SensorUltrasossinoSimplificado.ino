const int trigPin = 10;
const int echoPing = 11;

long duration;
int distance;


void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPing, INPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(10);
  
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(100);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPing, HIGH);
  distance = duration*0.034/2;
  delay(600);

  Serial.println(distance);

  

}
