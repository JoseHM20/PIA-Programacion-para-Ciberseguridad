# Function to display the LAN IP
lan_search(){
    sleep 3
    echo -e "\nObtaining the IP of the current LAN..."
    echo -e "\nThe IP of your LAN is:"
    if [ "$(uname)" = "Darwin" ]; then
       ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'
    elif [ "$(uname -s)" = "Linux" ]; then
       ip addr show | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'
    else
       echo "OS not supported"
       exit 1
    fi
}

# Function to view your current location
geoapi(){
   echo -e "\nLooking for location..."
   echo "Your location is:"
   # The link used will give us the geolocation data.
   content=$(wget http://ip-api.com/line/?fields=query,city,region,country,zip,isp -q -O -)
   echo $content
}

# Function to view active IPs
function is_alive_ping() {
         ping -c 1 $1 > /dev/null 2>&1
         [ $? -eq 0 ] | echo "Node with IP: $i is up."
}
for i in 192.168.1.{1..5} # Scrolling through the IPs
do
           is_alive_ping $i
done

# We call the functions
lan_search
geoapi