from data_reader import dataReader
from gui import selectFile
import random
import numpy as np
import string

class Faker():

    def __init__(self, n):
        self.number_of_samples = n

    def synthesize_continuous(self, target_mean, target_stdev):
        """Straight up copy-pasted from https://stackoverflow.com/questions/51515423/generate-sample-data-with-an-exact-mean-and-standard-deviation
        Make sure you don't take any credit for this function"""
        num_samples = self.number_of_samples
        desired_mean = target_mean
        desired_std_dev = target_stdev

        samples = np.random.normal(loc=0.0, scale=desired_std_dev, size=num_samples)

        actual_mean = np.mean(samples)
        actual_std = np.std(samples)

        zero_mean_samples = samples - (actual_mean)

        zero_mean_mean = np.mean(zero_mean_samples)
        zero_mean_std = np.std(zero_mean_samples)

        scaled_samples = zero_mean_samples * (desired_std_dev / zero_mean_std)
        scaled_mean = np.mean(scaled_samples)
        scaled_std = np.std(scaled_samples)

        final_samples = scaled_samples + desired_mean
        final_mean = np.mean(final_samples)
        final_std = np.std(final_samples)

        return final_samples

    def synthesize_boolean(self, percentage=50):
        """Returns 1 and 0 for number_of_samples at a given percentage of time"""
        random.seed()
        i = 0
        samples = []
        while i < self.number_of_samples:
            if random.randrange(0,100) < percentage:
                samples.append(1)
            else:
                samples.append(0)

            i+=1

        return samples

    def synthesize_strings(self):
        strings = []
        letters = string.ascii_letters
        i = 0
        while i < self.number_of_samples:
            strings.append(''.join(random.choice(letters) for i in range(10)))
            i+=1

        return strings






if __name__=='__main__':
    # more legible feedback using the rich library
    from rich.traceback import install
    install(show_locals=True)

    faker = Faker(1000)
    cont = faker.synthesize_continuous(50,5)
    bool = faker.synthesize_boolean(15)
    names = faker.synthesize_strings()

