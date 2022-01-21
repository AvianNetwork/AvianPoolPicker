import pools
import platform
GPU = pools.GPU()
print(GPU.idworkersGPU(pool="ZergPool", id="I_Love_Zergpool"))
print(GPU.get_miners(miner="T-Rex Miner", platform=platform.system()))