class AirConditioner:
   
    def __init__(self):
        self.__temperature = 24  
        self.__state = "off"   
        self.__mode = "auto"   
        self.valid_modes = ["cool", "heat", "auto"]

    def turn_on(self):
       
        self.__state = "on"
        print("AC is now ON")

    def turn_off(self):
       
        self.__state = "off"
        print("AC is now OFF")

    def set_mode(self, mode):
      
        mode = mode.lower()
        if mode in self.valid_modes:
            self.__mode = mode
            print(f"Mode set to: {self.__mode}")
        else:
            print("Invalid mode")

    def increase_temp(self):
       
        self.__temperature += 1
        print(f"Temperature increased to: {self.__temperature}°C")

    def decrease_temp(self):
      
        self.__temperature -= 1
        print(f"Temperature decreased to: {self.__temperature}°C")

    def get_status(self):
        
        print("\n--- AC Status ---")
        print(f"State:       {self.__state.upper()}")
        print(f"Mode:        {self.__mode.capitalize()}")
        print(f"Temperature: {self.__temperature}°C")
        print("-----------------\n")



my_ac = AirConditioner()

# اختبار الدوال
my_ac.get_status()
my_ac.turn_on()
my_ac.set_mode("heat")
my_ac.increase_temp()
my_ac.decrease_temp()
my_ac.set_mode("fan") # وضع غير صالح
my_ac.get_status()
my_ac.turn_off()