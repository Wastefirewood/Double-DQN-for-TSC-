import random

class Memory:
    def __init__(self, size_max, size_min):
        self._samples = []
        self._size_max = size_max
        self._size_min = size_min


    def add_sample(self, sample):
        """
        Add a sample into the memory
        """
        self._samples.append(sample)
        if self._size_now() > self._size_max:
            self._samples.pop(0)  # if the length is greater than the size of memory, remove the oldest element
            # 如果现在存储内容长度大于经验回放池的话,就删除最早的数据


    def get_samples(self, n):
        """
        Get n samples randomly from the memory
        """
        if self._size_now() < self._size_min:
            return []
        # 只有当经验回放池存储的数据小于经验回放池的最小尺寸时,返回空列表
        if n > self._size_now():
            return random.sample(self._samples, self._size_now())  # get all the samples
        # 如果现在经验回放池的存储数小于取样数,则将目前经验回放池里的所有数据取样
        else:
            return random.sample(self._samples, n)  # get "batch size" number of samples
        # 如果经验回放池的存储数大于取样数,则从经验回放池随机抽取和取样数一样的数据


    def _size_now(self):
        """
        Check how full the memory is
        """
        return len(self._samples)
