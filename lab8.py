class AirConditioner:
    """
    فئة لمحاكاة وظائف جهاز تكييف الهواء.
    """
    
    # الخصائص (Attributes)
    def __init__(self, temperature=24, state="off", mode="cool"):
        self._temperature = temperature
        self._state = state
        self._mode = mode

    # الدوال (Methods)
    
    # 1. turn_on()
    def turn_on(self):
        self._state = "on"
        print("AC is now **ON**.")

    # 2. turn_off()
    def turn_off(self):
        self._state = "off"
        print("AC is now **OFF**.")

    # 3. set_mode(mode)
    def set_mode(self, mode):
        valid_modes = {"cool", "heat", "auto"}
        
        if mode.lower() in valid_modes:
            self._mode = mode.lower()
            print(f"Mode set to: **{self._mode.upper()}**.")
        else:
            print(f"'{mode}' is an **Invalid mode!**")

    # 4. increase_temp()
    def increase_temp(self):
        self._temperature += 1
        print(f"Temperature increased. Current temp: **{self._temperature}°C**")

    # 5. decrease_temp()
    def decrease_temp(self):
        self._temperature -= 1
        print(f"Temperature decreased. Current temp: **{self._temperature}°C**")

    # 6. get_status()
    def get_status(self):
        print("\n--- **AC Status** ---")
        print(f"**State:** {self._state.upper()}")
        print(f"**Mode:** {self._mode.upper()}")
        print(f"**Temperature:** {self._temperature}°C")
        print("---------------------\n")


# مثال على الاستخدام (Usage Example)


my_ac = AirConditioner() 
my_ac.turn_on() 
my_ac.set_mode("heat") 
my_ac.increase_temp()
my_ac.decrease_temp()
my_ac.get_status()

