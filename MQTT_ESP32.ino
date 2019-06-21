#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "network nema";
const char* password =  "network pass";
const char* mqttServer = "iot.eclipse.org";
const int mqttPort = 1883;
const char* mqttUser = "";
const char* mqttPassword = "";

int cont = 1;
char mesage[30];

int num = 0;

// Callback function header
void callback(char* topic, byte* payload, unsigned int length);

WiFiClient espClient;
PubSubClient client(mqttServer,mqttPort,callback,espClient);

void setup()
{
  Serial.begin(9600);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
  }

  if (client.connect("arduinoClient")) {
   client.publish("outTopicregis","hello world");
   client.subscribe("inTopicregis");
  
  }

}

// Callback function
void callback(char* topic, byte* payload, unsigned int length) {
    
  if(payload[0] == '1'){
    client.publish("outTopicregis", "Recebido"); 
    num = 0;
    Serial.write(num);
    delay(500);
    num = 1;
    Serial.write(num);
    delay(500);
    }
    
  if (payload[0] == '0'){
    client.publish("outTopicregis", "Light Off");
    }
} // void callback


void loop()
{
  reconectabroker();

  client.loop();
  
  delay(5000);
  
}

void reconectabroker()
{
  client.setServer(mqttServer, mqttPort);
  while (!client.connected())
  {
    if (client.connect("ESP32Client", mqttUser, mqttPassword ))
    {}
    else
    {
      delay(2000);
    }
  }
}
