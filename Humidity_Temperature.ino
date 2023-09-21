#include <ArduinoJson.h>
#include <DHT.h>
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

#define DHTTYPE DHT11 
#define DHTPIN D1 // DIGITAL PIN

DHT dht(DHTPIN, DHTTYPE);

const char* ssid = "TP-Link_CA9C";
const char* password = "69025051";
const char* SERVER_URI = "http://192.168.1.217:5000/data";

void setup() {
  Serial.begin(9600);
  dht.begin();
  WiFi.begin(ssid, password);


  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting... ");
  }
}

void loop() {
  static const size_t capacity = JSON_OBJECT_SIZE(6);
  static StaticJsonDocument<capacity> jsonDoc;

  float humid = dht.readHumidity();
  float temp = dht.readTemperature();

  if (isnan(humid) || isnan(temp)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
  printf("%s\n", SERVER_URI);

  // Compute heat index in Celsius (isFahreheit = false)
  float heatIndex = dht.computeHeatIndex(temp, humid, false);

  jsonDoc["reporter"] = "cip";
  jsonDoc["temp"] = temp;
  jsonDoc["humidity"] = humid;
  jsonDoc["heatIndex"] = heatIndex;

  printJsonToSerial(jsonDoc);
  sendJsonToServer(jsonDoc);

  delay(2000); // Wait a few seconds 
}

void printJsonToSerial(JsonDocument& jsonDoc) {
  String jsonString;
  serializeJsonPretty(jsonDoc, jsonString);
  Serial.println(jsonString);

}

void sendJsonToServer(JsonDocument& jsonDoc) {
  static HTTPClient http;
  WiFiClient wifiClient;
  String jsonString;
  serializeJson(jsonDoc, jsonString);

  http.begin(wifiClient, SERVER_URI); 
  http.addHeader("Content-Type", "application/json");

  int httpResponseCode = http.POST(jsonString);

  if (httpResponseCode > 0) {
    String response = http.getString();
    Serial.println(httpResponseCode);
    Serial.println(response);
  } else {
    Serial.println("Error sending POST request");
  }
  http.end();
}
