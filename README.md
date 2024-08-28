# how to use
* clone repo
* create new conda env like so (you can name it what you like, I will call it 'vf23'):
```
conda create --name vf23 --file requirements.txt
```
* activate your new env like so:
```
conda activate vf23
```  
* run trait_creator in console like so:
```
  trait_creator.py [num drivers to create] [outputfilename]
```
* enjoy

# example call
to create traits for 50 drivers in 'driver_traits.csv' run :
```
  trait_creator.py 50 driver_traits.csv
```
