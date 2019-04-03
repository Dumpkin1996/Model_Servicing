# Extremely brutal-force.
# In need of some refactoring to make the code more concide, simple and clever.

cd src/machine_1
python3 machine_1.py &
sleep 0.5

cd ../machine_2
python3 machine_2.py &
sleep 0.5

cd ../machine_3
python3 machine_3.py &
sleep 0.5

cd ../machine_4
python3 machine_4.py &
sleep 1.5

cd ../machine_5
python3 machine_5.py &
sleep 0.5

cd ../machine_6
python3 machine_6.py &
sleep 1.5

cd ../machine_0
python3 machine_0.py

lsof -n -i4TCP:8000 | grep LISTEN | awk '{ print $2 }' | xargs kill
lsof -n -i4TCP:9000 | grep LISTEN | awk '{ print $2 }' | xargs kill
lsof -n -i4TCP:11000 | grep LISTEN | awk '{ print $2 }' | xargs kill
lsof -n -i4TCP:12000 | grep LISTEN | awk '{ print $2 }' | xargs kill
lsof -n -i4TCP:13000 | grep LISTEN | awk '{ print $2 }' | xargs kill
lsof -n -i4TCP:14000 | grep LISTEN | awk '{ print $2 }' | xargs kill
