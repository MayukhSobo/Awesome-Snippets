import numpy as np
import click
import random
from time import time
random.seed(int(time()))

def random_array(tc, maxn, minn, length, maxLength):
	sizes = []
	content = []
	for t in range(tc):
		if length == -1:
			s = random.randint(1, maxLength)
		else:
			s = length
		# if s < maxn - minn:
		# 	raise ValueError("Number of elements is larger than the range!")
		nums = random.sample(range(minn, maxn), s)
		sizes.append(s)
		content.append(nums)
	return sizes, content

def print_array(tc, size, content, download):
	# with open(f'test_case_{int(time())}.txt', 'w') as f:
	out = ""
	if download != 'YES':
		out += '-' * 50 + '\n'
	out += str(tc) + '\n'
	for s, c in zip(size, content):
		out += '\n' + str(s) + '\n'
		for each in c:
			out += str(each) + ' '
		out += '\n'
	if download == 'YES':
		with open(f'test_case_{int(time())}.txt', 'w') as f:
			print(out, file=f)
	else:
		print(out)

@click.command()
@click.option('--tc', prompt='Test cases',
			  type=int, default=1,
              help='Mention the number of test cases')
@click.option('--what', prompt='Problem Type',
			  type=click.Choice(['NUM', 'ARR', 'MAT'], case_sensitive=False),
              help='Mention the type of testcase')
@click.option('--maxN', prompt='Maximum value',
			  type=float,
              help='Maximum value of the num, arr or mat')
@click.option('--minN', prompt='Minimum value',
			  type=float,
              help='Minimum value of the num, arr or mat')
@click.option('--fixedLength', prompt='Fixed Length',
			  type=click.Choice(['YES', 'NO'], case_sensitive=False),
              help='Minimum value of the num, arr or mat')
@click.option('--download', prompt='Download tescases',
			  type=click.Choice(['YES', 'NO'], case_sensitive=False),
			  default='NO',
              help='If you want to download the test cases')
def gene(tc, what, maxn, minn, fixedlength, download):
	maxn = int(maxn) if int(maxn) == maxn else maxn
	minn = int(minn) if int(minn) == minn else minn
	length = -1
	if what != 'NUM':
		if fixedlength == 'YES':
			length = int(input('Length: '))
		if what == 'ARR':
			if fixedlength == 'YES':
				maxLength = fixedlength
			else:
				maxLength = int(input('Max Len: '))
			sizes, content = random_array(tc, maxn, minn, length, maxLength)
			print_array(tc, sizes, content, download)


if __name__ == '__main__':
    gene()