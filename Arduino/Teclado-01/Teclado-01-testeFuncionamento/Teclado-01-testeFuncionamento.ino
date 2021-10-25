#include <Keypad.h>

const byte ROWS = 4;
const byte COLS = 4;
char keys[ROWS][COLS] = {
  {'1','2','3'},
  {'4','5','6'},
  {'7','8','9'},
  {'*','0','#'}
  };

byte rowPins[ROWS] = {4,5,6,7};
byte colPins[COLS] = {8,9,10};

Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS);

void setup() {
    Serial.begin(9600);
    Serial.println("Vitor teclado teste");
}

void loop() {
    char key = keypad.getKey();

    if(key){
      Serial.println(key);
    }

    if(key == '5'){
      Serial.println("A tecla apertada foi 5");
    }
    
}
