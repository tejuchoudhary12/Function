def driver_speed(speed):
    if range_of_speed<=70:
        print("OKAY")
    elif range_of_speed>70:
        a=speed*70
        print(a)
        b=a%5
        if b==0:
            print(a//5, "point")
            if a>12:
                print("license suspended")
range_of_speed=int(input("enter the speed"))
driver_speed(range_of_speed)