"""
This is Python and it's a joy <3

Pro tip (skip if you are lazy):
    Python should always be used in a virtual environment. Before running the
    script, make a virtual environment by running the following command in a
    terminal:

    python -m venv my_alg_env

    Activate the environment by running:

    source my_alg_env/bin/activate

    Now you can do all you Python shenanigans (such as installing packages)
    without doing it in the global environment.

    When you are done, type `deactivate` to exit the environment. If you wanna
    remove it all completely, go to the directory where you created it and run

    rm -rf my_alg_env

To run this file:
    Download (or copy) the `names.txt` file from https://raw.githubusercontent.com/bjerva/bjerva.github.io/master/danskenavne.txt
    Install matplotlib by running `pip install matplotlib` in a terminal
    Set PATH_TO_NAMES to point to your file
    Run `python hashing.py` in a terminal

"""
import matplotlib.pyplot as plt


# set to <path/to/my/names-file.txt>
PATH_TO_NAMES = './names.txt'

# read the file and store names in `names`
with open(PATH_TO_NAMES, 'r') as f:
    names = f.read().splitlines()


# write a function the implements the division method for hashing
# hint: it probably needs to take two input arguments...
def h(key, m):
    return key % m


# write a function that calculate the sum of ASCII values in `name`
# hint: use the built-in function `ord(c)` to get the ASCII value of the
# character `c`
def get_ascii_sum(name):
    return sum(ord(l) for l in name)


# write a function that calculates the number of vowels in a string
# hint: maybe make a list of all vowels and either remember to add both lower
# case and upper case letters or just call `.lower()` on your input string
def get_num_vowels(name):
    vowels = ['a','e','i','o','u','y']
    total = 0
    for c in name:
        if c in vowels:
            total += 1
    return total


# division method on val = s[0] + s[1] * p + s[2] * p^2 + ... + s[n-1] * p^(n-1)
# write a function that implements Polynomially Rolling Hashing. This is a an
# actual method used for hashing strings, and it works by converting an input
# string `s` to a key by taking the sum of s[i] * p^i for all i < len(s), with p
# being some positive integer, and then hashing that key using the division method.
#
# Ie.\ key = s[0] + s[1] * p + # s[2] * p^2 + ... + s[n-1] * p^(n-1) for a
# string s of size n.
#
# hint: experiment with different values of p as it can greatly affect
# performance (in terms of quality). If it doesn't work properly, try something
# in the range of [25,35]
# hint 2: make your life easier by converting the input string to lower case
# hint 3: ignore characters that are not letters --- in ascii, the lower case
# letters start at 97
def polynomially_rolling_hash(name, m, p):
    key = 0
    s = name.lower()
    for i in range(len(s)):
        pos = ord(s[i]) - 96

        # skip characters such as '-'
        if pos > 0:
            key += pos * p**i

    return h(key, m)


# set m (this is a good default, but you can experiment with it
m = 701

# this is not a good default, so experience with it
p = 1

col1_data = []

fig = plt.figure()

gs = fig.add_gridspec(3, 2)
ax1 = fig.add_subplot(gs[0,0])
ax2 = fig.add_subplot(gs[0,1])
ax3 = fig.add_subplot(gs[1,0])
ax4 = fig.add_subplot(gs[1,1])
ax5 = fig.add_subplot(gs[2,:])

try:
    ascii_sums = [get_ascii_sum(name) for name in names]
    ax1.hist(ascii_sums, max(ascii_sums))
    ax1.set_title('ASCII sums')
    col1_data.append((ascii_sums, 'ASCII sums hashed', ax2))
except NotImplementedError:
    pass

try:
    num_vowels = [get_num_vowels(name) for name in names]
    ax3.hist(num_vowels, max(num_vowels))
    ax3.set_title('Number of vowels')
    col1_data.append((num_vowels, 'Number of vowels hashed', ax4))
except NotImplementedError:
    pass

try:
    for data, title, ax in col1_data:
        hashes = [h(k,m) for k in data]
        ax.hist(hashes, max(hashes))
        ax.set_title(title)
except NotImplementedError:
    pass

try:
    pol_rol_hash = [polynomially_rolling_hash(name, m, p) for name in names]
    ax5.hist(pol_rol_hash, m)
    ax5.set_title('Polynomially rolling hashes')
except NotImplementedError:
    pass

plt.show()
