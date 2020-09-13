echo "Installation of wlke starts..."

if [ docker -v ] 
then
    echo "starting containers..."
    cd wlke && docker-compose up --build -d
    sleep 100.0
    echo "Installation finished"
fi
else
    echo "Install docker"
