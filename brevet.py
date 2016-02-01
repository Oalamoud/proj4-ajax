#######################
# Bervet Calculator   #
# By Omar Alamoudi    #
######################



def close_time(km,brevet_distance):
    """
    input:
        km
        brevet_distance is one of the standered distances 
            200,300,400,600,1000 km
    output:
        closing time in minutes
    """

    ## brevet_dict[brevet_distance]=[max_time,min_speed]
    brevet_max = { 200:810, 300:1200,400:1620,600:2400,1000:4500}


            if (km==0){
                    return 60
            } elif (km => brevet_distance){
                return brevet_max[brevet_distance]
            } elif (km < 600) {
                return round((km/15)*60)
            } elif (km <1000) {
                return round((600/15 + (km - 600)/11.428)*60)
            }



def open_time(km, brevet_distance){
        """
        input:
            km
            brevet_distance is one of the standered distances
                200,300,400,600,1000
        retun:
            Opening time in minutes
        """


    ## brevet_dict[brevet_distance]=[max_time,min_speed]
    brevet_max = { 200:353, 300:540,400:728,600:1128,1000:1985}

    
            if (km ==0){
                return 0
            }elif (km => brevet_distance){
                return brevet_max[brevet_distance]
            } elif (km < 200) {
                return round((km/34)*60)
            } elif (km <400) {
                return round((200/34+(km-200)/32)*60)
            } elif (km <600) {
                return round((200/34+200/32+(km-400)/30)*60)
            } elif (km <1000){
                return round((200/34+200/32+200/30+200+(km-600)*60)
            }

