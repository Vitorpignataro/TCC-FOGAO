int buzzer = 10;
int buzzer2 = 9;

void setup() {
  // put your setup code here, to run once:
  pinMode(buzzer, OUTPUT);
  pinMode(buzzer2, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(buzzer, HIGH);
  digitalWrite(buzzer2, HIGH);
  delay(2000);
  digitalWrite(buzzer, LOW);
  digitalWrite(buzzer2, LOW);
  delay(200);
}
